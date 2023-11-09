import json
from datetime import datetime
import urllib.request
from jose import jwk, jwt
from jose.utils import base64url_decode
import pytz
import boto3

region = ''
userpool_id = ''
app_client_id = ''
keys_url = ''.format(region, userpool_id)
PREFIX = 'Bearer '
# instead of re-downloading the public keys every time
# we download them only on cold start
# https://aws.amazon.com/blogs/compute/container-reuse-in-lambda/
with urllib.request.urlopen(keys_url) as f:
  response = f.read()
keys = json.loads(response.decode('utf-8'))['keys']

def lambda_handler(event, context):
    auth = event['headers']["authorization"]
    # auth=event["token"]
    if not auth.startswith(PREFIX):
        return {
                    'statusCode': 400,
                    'body': json.dumps({"error": True, 
                        "message": "Invalid token",
                })}

    token = auth[len(PREFIX):]
    if len(token)==0:
       return {
                    'statusCode': 400,
                    'body': json.dumps({"error": True, 
                        "message": "Token is not present",
                })}
    
    token = str(token)

    client = boto3.client('cognito-idp')
    details=client.get_user(AccessToken=token)["UserAttributes"]

    email = None
    tags = []

    for obj in details:
        name = obj["Name"]
        val  = obj["Value"]
        if name == "custom:tag":
            tags.extend(val.split(";"))
        elif name=="email":
            email=val

    # get the kid from the headers prior to verification
    headers = jwt.get_unverified_headers(token)
    kid = headers['kid']
    # search for the kid in the downloaded public keys
    key_index = -1
    for i in range(len(keys)):
        if kid == keys[i]['kid']:
            key_index = i
            break
    if key_index == -1:
        return {
        'statusCode': 401,
        'body': json.dumps({
            "success": False, 
            "message": "No public key found in cognito", 
        })
        }
    # construct the public key
    public_key = jwk.construct(keys[key_index])
    # get the last two sections of the token,
    # message and signature (encoded in base64)
    message, encoded_signature = str(token).rsplit('.', 1)
    # decode the signature
    decoded_signature = base64url_decode(encoded_signature.encode('utf-8'))
    # verify the signature
    if not public_key.verify(message.encode("utf8"), decoded_signature):
        return {
        'statusCode': 401,
        'body': json.dumps({
            "success": False, 
            "message": "Signature verification failed", 
        })
        }
    # since we passed the verification, we can now safely
    # use the unverified claims
    try:
        claims = jwt.get_unverified_claims(token)

    except Exception as e: 
        return {
        'statusCode': 500,
        'body': json.dumps({
            "success": False, 
            "message": str(e), 
        })
    }
    
    if ("client_id" in claims and claims['client_id'] != app_client_id) or ("aud" in claims and claims["aud"] != app_client_id):
            return {
            'statusCode': 401,
            'body': json.dumps({
                "success": False, 
                "message": "Token was not issued for this audience", 
            })
            }
    
    # additionally we can verify the token expiration
    exp_time=claims["exp"]
    utc_dt=datetime.utcfromtimestamp(float(exp_time))

    local_tz = pytz.timezone('Singapore') # use your local timezone name here
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    print(local_dt)
    print(datetime.now(tz=local_tz))

    if datetime.now(tz=local_tz)<local_dt:
        return {
            'statusCode': 200,
            'body': json.dumps({
                "success": True, 
                "message": "User is authenticated", 
                "data":{
                "username": claims["username"],
                "email": email,
                "tag": tags
                }
            })
        }
    else:
        return {
            'statusCode': 401,
            'body': json.dumps({
                "success": False, 
                "message": "JWT expired", 
            })
        }
        
# the following is useful to make this script executable in both
# AWS Lambda and any other local environments
if __name__ == '__main__':
    # for testing locally you can enter the JWT ID Token here
    # event = {'token': 'Bearer eyJraWQiOiJScHByQWo2QlhwT1k5UHRidEhOMkIxb240ZkRDVEFSbDVaaVoyamJldE5vPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJiOGJlODU4My01NGEyLTQ2NzQtOWVmMS01YjIwNTBiMGVkY2EiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV9rQ2xaMGxvZ0kiLCJjb2duaXRvOnVzZXJuYW1lIjoidGVzdF91c2VyIiwib3JpZ2luX2p0aSI6IjBkMjQzYTZiLTQ0ZjQtNDllZC04YTJlLTYzNjJiM2VkMGQzMyIsImF1ZCI6IjVuZWdkamFlZGZtNGhnY3RycXA2dWRuZTM2IiwiZXZlbnRfaWQiOiIxNzNjZTUwMi1mZDVmLTQwZDQtOTM5OS04Yzk1NmIwMzBjZDAiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY5OTA3MDM4MiwiZXhwIjoxNjk5MDczOTgxLCJpYXQiOjE2OTkwNzAzODIsImp0aSI6IjEwYTM2Mjg5LTlkYzctNGMxYS1hMjEwLWNiMmQ2YjMyZjI2NiIsImVtYWlsIjoiemR3b25nLjIwMjFAdS5lZHUuc2cifQ.ci2uzMMztRkTDOodz_Tv4T9eYf13-vazFEd-HhSLm0GA0USI7BZxZitD8gHqZp9KSscgmHDl5XNj8Bm9L_apLM5zoioWoBs8ad8C_BLS47Jj5zDSXhyrTq0HC3klKJIpqxQBLAHUcS_CFlPckN67nU_C0y2SRp9GdXfDh6MCddDpSx9ADtPlq609canyYfzOmNJ8YYcg4DB0kGjKg_g4qsRdHVJ_gAjOSgsILZsxUvD7oJkfuZaBpePGWJDAN301iw9Z-9chsG-iXep2scZcVYin2_p1Fxo2Do0_5ieDq1u2Ra-IZxKpOj9Ni7mCOEAN9y8fFin9SRQ03iFkSSyONw'}
    event = {'token': 'Bearer eyJraWQiOiJKNDZBNnR1d0lWSTRWcnV2K05tK1dsSWc3QzVMVDlHZUFRdGQrTm45V0FFPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJiOGJlODU4My01NGEyLTQ2NzQtOWVmMS01YjIwNTBiMGVkY2EiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTFfa0NsWjBsb2dJIiwiY2xpZW50X2lkIjoiNW5lZ2RqYWVkZm00aGdjdHJxcDZ1ZG5lMzYiLCJvcmlnaW5fanRpIjoiYzMwYzBkMTItNzU0NS00ZjU0LWJmOGEtMTY1OTcwOGY3YWY3IiwiZXZlbnRfaWQiOiIxZTRmNzIzOC0xOTgwLTRlNjUtOWJhNS04M2NjM2FhZjBmNmQiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjk5MDcwNzcxLCJleHAiOjE2OTkwNzQzNzAsImlhdCI6MTY5OTA3MDc3MSwianRpIjoiMmFhYmIxMjUtODU0NC00ZGU1LWIxMmItN2ZiNjE5ZDUxMWE2IiwidXNlcm5hbWUiOiJ0ZXN0X3VzZXIifQ.lRzUYH4rZAEm1Oa2zzltDIq-hkNgoBHVw7jcnz3froO33yAozcbrHEsPp9_xcahTC8bgsvqnwcgN_QQ19YBg7D1Hpvxw2RwGGAimaLInKRtFLNlQIvxKDgbCprVMbk0uEYHIklczqQbD_FXScW0c0Ckx2p-7jmu3rbsXZp5QpWitguA2axGDpnQrnoIVyoQElTh3u141TagbTLd50Wb7GkPxy-Rg-QeCBAQELQRrY3AeUvNa0TX86q8qEMgOXyUzsZYMNp553aUejT4MgTAVsBmMo1tx4aLlYX9OVq97aqlRdqMNWaQ6GOduwheg_usFxPH-p4EtvEi5_Ki7zEF0tg'}
    print(lambda_handler(event, None))