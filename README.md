# Dynamodb and FastAPI template
Sample project for experimenting with DynamoDB and FastAPI. I created this to learn about DynamoDB, OAuth2 and JSON Web Tokens.

Running the project with docker compose starts up the API and a  [DynamoDB local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) instance.

## Run the project
```
docker compose up --build
```

## Create DynamoDB Table
This needs to be run the first time you start the project. If you delete the file in the db directory you will need to run it again.

```
docker compose run server python setup_dev_db.py
```

DynamoDB databases are often designed around a [single table](https://www.alexdebrie.com/posts/dynamodb-single-table/). This project uses a single table, the name of this table is configured in `server/.env`. Single table design was something I was curious about understanding when creating this project.

## Run the tests
```
docker compose run server pytest
```

Running the tests will create a new table called `test-table` to use for API tests, and then delete it when the tests complete, so as not to conflict with any data in the table that is used when you run the project with `docker compose up --build`. See `conftest.py`.
