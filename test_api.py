import pytest
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_summurizing_api():
    response_1 = client.post("/sumurrize_the_text/", json = {"text":"please summurize it!"} )
    assert response_1.status_code == 200