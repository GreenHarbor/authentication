import boto3
import botocore.exceptions
import json

USER_POOL_ID = ""

def lambda_handler(event, context):
    # It sets the user pool autoConfirmUser flag after validating the email domain
    client = boto3.client('cognito-idp')
    try:
        response = client.list_users(
            UserPoolId=USER_POOL_ID,
            AttributesToGet=[
                "email",
                'custom:tag',
            ],
            
        )
    except Exception as e:
            return {
                    'statusCode': 500,
                    'body': json.dumps({"error": True, 
                        "message": str(e),
                })}

    if response["ResponseMetadata"]["HTTPStatusCode"] != 200:
            return {
                    'statusCode': 500,
                    'body': json.dumps({"error": True, 
                        "message": "Unable to retrieve users",
                })}
    res=[]
    for user in response["Users"]:
        attributes = user["Attributes"]
        email=None
        tags=[]
        
        for attribute in attributes: 
             if attribute["Name"] == "email":
                  email = attribute["Value"]
             elif attribute["Name"] == "custom:tag":
                  tags.extend(attribute["Value"].split(";"))

        res.append({"username":user["Username"],"email":email,"tag":tags})
    # Return to Amazon Cognito
    return {
        'statusCode': 200,
        'body': json.dumps({
            "success": True, 
            "data": res
        })
    }

if __name__=="__main__":
    print(lambda_handler({},None))