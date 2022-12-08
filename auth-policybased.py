def lambda_handler(event, context):
    
    #1 - Log the event
    print('*********** The event is: ***************')
    print(event)
    
    #2 - See if the header value is valid
    if event['headers']['authorizationtoken'] == 'secretcode':
        auth = 'Allow'
    else:
        auth = 'Deny'
    authResponse = { "principalId": "abc123", "policyDocument": { "Version": "2012-10-17", "Statement": [{"Action": "execute-api:Invoke", "Resource": ["arn:aws:execute-api:us-east-1:185036908705:ji09sb7bz6/*/*"], "Effect": auth}] }}
    authResponse['context'] = {
        "userheadervalue" : event['headers']['authorizationtoken'] == 'secretcode',
        "respondedas" : auth
    }
    return authResponse
    
