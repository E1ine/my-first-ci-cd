import sys
import os
import pytest
from app import app

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  

def test_hello_world():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Hello' in response.data
