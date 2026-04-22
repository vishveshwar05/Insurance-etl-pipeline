import boto3, json, uuid

s3 = boto3.client('s3')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    
    file_name = f"claims/{uuid.uuid4()}.json"
    
    s3.put_object(
        Bucket="claims-raw-data",
        Key=file_name,
        Body=json.dumps(body)
    )
    
    return {
        "statusCode": 200,
        "body": "Claim uploaded successfully"
    }
