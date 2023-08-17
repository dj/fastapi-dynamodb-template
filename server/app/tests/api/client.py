import os
from fastapi.testclient import TestClient

os.environ["DB_TABLE_NAME"] = "lists-app-test"

from ...main import app

test_client = TestClient(app)
