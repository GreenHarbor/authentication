rm deployment.zip
cd package
zip -r ../deployment.zip . 
cd ..
zip deployment.zip lambda_handler.py