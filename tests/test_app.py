import sys
import os
from app import app

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # если реально нужен


def test_hello_world():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Hello' in response.data
