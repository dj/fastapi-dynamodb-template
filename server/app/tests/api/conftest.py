import pytest
import os
import boto3

test_table_name = "test-table"


@pytest.fixture(scope="session", autouse=True)
def setup_db(request):
    dynamodb = boto3.resource(
        "dynamodb",
        endpoint_url="http://dynamodb-local:8000",
        region_name="us-west-2",
        aws_access_key_id="fakeaccesskeyid",
        aws_secret_access_key="fakesecretaccesskey",
    )

    table = dynamodb.create_table(
        TableName=test_table_name,
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

    print(f"\n\nTest table created: {test_table_name}\n\n")

    def teardown():
        dynamodb.meta.client.delete_table(TableName=test_table_name)
        print(f"\n\nTest table deleted: {test_table_name}\n\n")

    request.addfinalizer(teardown)
