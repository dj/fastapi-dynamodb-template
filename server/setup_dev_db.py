"""
setup_dev_db.py

Run with:
docker compose run server python setup_dev_db.py

Creates a table in dynamo db (stored in db/shared-local-instance.db)
"""
import boto3
from app.settings import get_settings

dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url="http://dynamodb-local:8000",
    region_name="us-west-2",
    aws_access_key_id="fakeaccesskeyid",
    aws_secret_access_key="fakesecretaccesskey",
)

table = dynamodb.create_table(
    TableName=get_settings().db_table_name,
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
