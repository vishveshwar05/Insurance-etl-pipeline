import boto3, csv, json

s3 = boto3.client('s3')
sqs = boto3.client('sqs')

QUEUE_URL = "your-rejected-queue-url"

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    response = s3.get_object(Bucket=bucket, Key=key)
    lines = response['Body'].read().decode('utf-8').splitlines()
    
    reader = csv.DictReader(lines)
    
    accepted = []
    rejected = []
    
    for row in reader:
        if row['ClaimID'] and float(row['ClaimAmount']) > 0:
            accepted.append(row)
        else:
            rejected.append(row)
    
    for r in rejected:
        sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(r)
        )
    
    return {"statusCode": 200}
