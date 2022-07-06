import requests
import pytest

def test_base_route_hello_world():
    response = requests.get("http://localhost:5000/")
    assert response.status_code == 200

def test_text():
    response = requests.get("http://localhost:5000/")
    assert "Welcome to the Application with updated code!" == response.text
