import json
import boto3

# Initialize the DynamoDB resource (AWS Documentation)
dynamodb = boto3.resource('dynamodb')

# replace table name with mine (AWS Documentation)
table = dynamodb.Table('tableForCloudResumeChallenge')

def lambda_handler(event, context):
    # key used in DynamoDB table
    key = {
        'pk': 'visitorCount'  # or whatever your primary key is
    }

    #get item with the primary key
    response = table.get_item(Key=key)
    print("DynamoDB resonse:", response)

    
    #if item exists, then pull the value out of it, but if not, return 0
    if 'Item' in response:
        current_count = int(response['Item'].get('count', 0))
    else:
        current_count = 0
        print("Item not found in DynamoDB table.")

    #increment the count
    new_count = current_count + 1
    print("New count:", new_count)


    #update the item count in DynamoDB
    table.update_item(
    Key=key,
    UpdateExpression='SET #placeholderForCount = :val',
    ExpressionAttributeNames={'#placeholderForCount': 'count'},
    ExpressionAttributeValues={':val': new_count}
    )



    #print("DynamoDB response:", response)

    #Return the updated count
    return {
        'statusCode': 200,
       'body': json.dumps({'count': new_count})
   }
