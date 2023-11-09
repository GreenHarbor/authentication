# Authentication Service

## Introduction

This repository contains the authentication service application written in Python, designed to be deployed on AWS Lambda. It facilitates user signup and signin by interfacing with Amazon Cognito User Pool.

Repository: [authentication](https://github.com/GreenHarbor/authentication.git)

## Features

- **User Signup**: Allows new users to create an account.
- **User Signin**: Enables existing users to sign in to their account.
- **AWS Lambda Deployment**: Designed for serverless deployment on AWS Lambda for scalability and efficiency.
- **Amazon Cognito Integration**: Utilizes Amazon Cognito User Pool for managing user authentication.

## Getting Started

These instructions will guide you through the setup and deployment of the authentication service.

### Prerequisites

- AWS Account
- AWS CLI configured with appropriate permissions
- Python 3.8+
- Serverless Framework (optional for deployment)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/GreenHarbor/authentication.git
   ```
2. Navigate to the project directory:
   ```
   cd authentication
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Configuration

- Configure your AWS credentials to enable deployment to AWS Lambda.
- Set up an Amazon Cognito User Pool and note down the necessary identifiers required for the application.

### Deployment

Deploy the application to AWS Lambda using the AWS CLI or Serverless Framework:

Using AWS CLI:
```
aws lambda create-function --function-name authentication-service \
--zip-file fileb://function.zip --handler lambda_function.lambda_handler \
--runtime python3.8 --role arn:aws:iam::account-id:role/lambda-role
```

Using Serverless Framework:
```
serverless deploy
```

## Usage

After deployment, the service will expose two main endpoints:

- `/signup`: Endpoint for user registration.
- `/signin`: Endpoint for user login.
