import boto3
import hmac
import hashlib
import base64
import json

USER_POOL_ID = ""
COGNITO_CLIENT_ID = ""
COGNITO_CLIENT_SECRET= ""

def get_secret_hash(username):
    msg = username + COGNITO_CLIENT_ID
    dig = hmac.new(str(COGNITO_CLIENT_SECRET).encode('utf-8'), 
        msg = str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
    d2 = base64.b64encode(dig).decode()
    return d2

def lambda_handler(event, context):
    body = json.loads(event['body'])
    for field in ["username", "email", "password","tag"]:
        if field not in body:
                return {
                    'statusCode': 400,
                    'body': json.dumps({"error": True, 
                        "message": f"{field} is not present",
                })}
    username = body['username']
    email = body["email"]
    password = body['password']
    tags = ";".join(body['tag'])
    
    if len(password)<8:
        return {
            'statusCode': 400,
            'body': json.dumps({"error": True, 
                "message": "Username not confirmed",
            })}
    
    client = boto3.client('cognito-idp')
    try:
        resp = client.sign_up(
            ClientId=COGNITO_CLIENT_ID,
            SecretHash=get_secret_hash(username),
            Username=username,
            Password=password, 
            UserAttributes=[
            {
                'Name': "email",
                'Value': email
            },
            {
                'Name': "custom:tag",
                'Value': tags
            }
            ],
            ValidationData=[
                {
                'Name': "email",
                'Value': email
            },
            {
                'Name': "custom:username",
                'Value': username
            }
])
    
    
    except client.exceptions.UsernameExistsException as e:
        return {
        'statusCode': 409,
        'body': json.dumps({"error": True, 
               "message": "Username already exists", 
                })}
    except client.exceptions.UserLambdaValidationException as e:
        return {
        'statusCode': 409,
        'body': json.dumps({"error": True, 
               "message": "Email already exists", 
                })
    }
    
    except Exception as e:
        return {
        'statusCode': 500,
        'body': json.dumps({"error": False, 
                "success": True, 
                "message": str(e), })
    }
    

    return {
        'statusCode': 201,
        'body': json.dumps({
            "success": True, 
            "message": "Sign up sucessful", 
            "data": None
        })
    }

