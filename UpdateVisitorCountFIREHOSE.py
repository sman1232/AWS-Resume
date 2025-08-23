import json
import boto3
from datetime import datetime

# Initialize the Firehose client
firehose = boto3.client('firehose')

# Firehose Delivery Stream
DELIVERY_STREAM_NAME = "PUT-S3-Pmyyb"

def lambda_handler(event, context):
    #Lambda handler that logs visitor info to Firehose.
    
    
    # Extract visitor info from event in format for API Gateway
    ip = event.get('requestContext', {}).get('identity', {}).get('sourceIp', 'Unknown')
    user_agent = event.get('headers', {}).get('User-Agent', 'Unknown')
    path = event.get('path', '/')

    # Add timestamp in UTC zone
    timestamp = datetime.utcnow().isoformat() + "Z"
    
    # Build record dictionary
    record_dict = {
        "ip": ip,
        "timestamp": timestamp,
        "user_agent": user_agent,
        "path": path
    }
    
    # Convert to JSON string
    json_string = json.dumps(record_dict)
    
    # Send record to Firehose
    response = firehose.put_record(
        DeliveryStreamName=DELIVERY_STREAM_NAME,
        Record={
            "Data": json_string
        }
    )
    
    #Return message
    return {
        'statusCode': 200,
        'body': json.dumps({
            "message": "Record sent to Firehose",
            "firehose_response": response
        })
    }
