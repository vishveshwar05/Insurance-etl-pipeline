import json
import random

def lambda_handler(event, context):
    for record in event['Records']:
        claim = json.loads(record['body'])
        status = random.choice(["PAID", "PENDING", "FAILED"])
        print(claim.get("ClaimID"), status)

    return {"statusCode": 200}
