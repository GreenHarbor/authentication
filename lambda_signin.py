import boto3
import botocore.exceptions
import hmac
import hashlib
import base64
import json
# USER_POOL_ID = 'us-east-2_cv8NhC3FK'
# CLIENT_ID = '1iafjm3k7sgm1diiio0gr4gvvs'
# CLIENT_SECRET = '1lpb1ruib9hl5smv4u045gr67u1p55o60k27smv6n4ur29066108'

USER_POOL_ID = ""
COGNITO_CLIENT_ID = ""
COGNITO_CLIENT_SECRET= ""

def get_secret_hash(username):
  msg = username + CLIENT_ID 
  dig = hmac.new(str(CLIENT_SECRET).encode('utf-8'),
  msg = str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
  d2 = base64.b64encode(dig).decode()
  return d2

def lambda_handler(event, context):
    client = boto3.client('cognito-idp')
    body = json.loads(event['body'])
    for field in ["username","password"]:
        if body.get(field) is None:
                return {
                    'statusCode': 400,
                    'body': json.dumps({"error": True, 
                        "message": f"{field} is not present",
                })}
    username=body["username"]
    password=body["password"]
    try:
        res=client.initiate_auth(
                    ClientId=CLIENT_ID,
                    AuthFlow='USER_PASSWORD_AUTH',
                    AuthParameters={
                        'USERNAME': username,
                        'PASSWORD': password,
                        'SECRET_HASH': get_secret_hash(username),
        
                    }
                )
    except client.exceptions.NotAuthorizedException:
            return {
            'statusCode': 400,
            'body': json.dumps({"error": True, 
                "message": "The username or password is incorrect",
            })}
    except client.exceptions.UserNotConfirmedException:
            return {
            'statusCode': 400,
            'body': json.dumps({"error": True, 
                "message": "Username not confirmed",
            })}
    except Exception as e:
                return {
        'statusCode': 500,
        'body': json.dumps({"error": False, 
                "success": True, 
                "message": str(e),})
    }
    return {
        'statusCode': 200,
        'body': json.dumps({
            "success": True, 
            "message": "Sign up sucessful", 
            "data": {
                "id_token": res["AuthenticationResult"]["IdToken"],
                "refresh_token": res["AuthenticationResult"]["RefreshToken"],
                "access_token": res["AuthenticationResult"]["AccessToken"],
                "expires_in": res["AuthenticationResult"]["ExpiresIn"],
                "token_type": res["AuthenticationResult"]["TokenType"]
            }
        })
    }