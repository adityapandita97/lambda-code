-----
CODE:
-----

import json

host = ".org" #the origin you wish to allow. In your case this would be: host = ".zuluapp.io "
allowed_methods = ["GET","OPTIONS"] #the methods that are allowed

def lambda_handler(event, context):
    host_name = event['headers']['origin']
    requested_method = event['headers']['access-control-request-method']

#if condition to check if the host name is present in the origin.
#Ensure to NOT include "*" in the host and just include the remaining part

    if host in host_name and requested_method in allowed_methods:
        return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': str(host_name),
            'Access-Control-Allow-Methods': str(requested_method)
        },
        'body': json.dumps('Hello from Lambda!')
        }

    else:
        return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': host,
            'Access-Control-Allow-Methods': str(allowed_methods),
        },
        'body': json.dumps('Hello from Lambda!')
        }


------------
EXPLAINATION:
------------

This code is a simple AWS Lambda function that creates an API gateway that sets CORS headers in the HTTP response. It uses the Python programming language to handle requests.

The purpose of this script is to allow cross-origin resource sharing (CORS) across different origins. CORS is a security feature implemented in web browsers that restricts websites from making requests to other domains due to security reasons; it prevents attackers from using a user's browser to launch attacks on other sites. However, some web apps require permission to call resources from other domains, which can be granted through the use of CORS.

Let’s get into the code itself -

Importing necessary libraries

import json
This line imports the json library to manipulate data structures in JSON format.

Setting some configurations

host = ".org"
allowed_methods = ["GET","OPTIONS"]
These two lines define the allowed origins and methods for CORS control.

Defining the lambda_handler() function

def lambda_handler(event, context):
The lambda_handler() function is the main entry point for the lambda function. It takes two parameters, "event" and "context." The "event" parameter contains data about an incoming request, while the "context” parameter provides information about the Lambda function's environment.

Reading request headers

host_name = event['headers']['origin']
requested_method = event['headers']['access-control-request-method']
These lines read the origin and method types from incoming request headers.

Checking if the host and method are allowed

if host in host_name and requested_method in allowed_methods:
        return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': str(host_name),
            'Access-Control-Allow-Methods': str(requested_method)
        },
        'body': json.dumps('Hello from Lambda!')
        }
Here, we check whether the incoming origin and method match our allowed configuration, and if found, sets the Access-Control-Allow-* headers on the response. This allows the origin site to access resources on our site under controlled circumstances. A 200 status code is returned with the required headers added, allowing calling the specified API over CORS.

If the provided host or method has not been allowed

else:
        return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': host,
            'Access-Control-Allow-Methods': str(allowed_methods),
        },
        'body': json.dumps('Hello from Lambda!')
        }
Here, we can see that when the allowed_hostnames and method don't match what is allowed, we simply return the standard header in the response to disallow invocation over CORS.

In summary, this code receives HTTP requests and checks the incoming headers against an allowed list defined, which then appends or rejects the calls altogether while setting the desired header attributes.
