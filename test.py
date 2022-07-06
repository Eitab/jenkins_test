import requests
import pytest

def test_base_route_hello_world():
    response = requests.get("http://localhost:5000/")
    assert response.status_code == 200

def test_text():
    response = requests.get("http://localhost:5000/")
    assert "Welcome to the Application with updated code!" == response.text


def test_base_route_stub():
    response = requests.get("http://localhost:5000/stub")
    assert response.status_code == 200

def test_text_stub():
    response = requests.get("http://localhost:5000/stub")
    assert "Value of Stub: 200" == response.text
