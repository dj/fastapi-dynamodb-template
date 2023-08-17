import boto3

dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url="http://localhost:8000",
    region_name="us-west-2",
    aws_access_key_id="fakeaccesskeyid",
    aws_secret_access_key="fakesecretaccesskey",
)

table = dynamodb.create_table(
    TableName="lists-app",
    KeySchema=[
        {"AttributeName": "PK", "KeyType": "HASH"},
        {"AttributeName": "SK", "KeyType": "RANGE"},
    ],
    AttributeDefinitions=[
        {"AttributeName": "PK", "AttributeType": "S"},
        {"AttributeName": "SK", "AttributeType": "S"},
    ],
    ProvisionedThroughput={
        "ReadCapacityUnits": 1,
        "WriteCapacityUnits": 1,
    },
)

table.wait_until_exists()

print("table created", table)
