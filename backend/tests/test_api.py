import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  

from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_submit_success():
    payload = {"aadhaar": "123412341234", "pan": "ABCDE1234F", "name": "Test", "email": "me@ex.com", "otp": "123456"}
    r = client.post("/submit", json=payload)
    assert r.status_code == 200
    js = r.json()
    assert "id" in js and js["message"] == "saved"

def test_submit_bad_pan():
    payload = {"aadhaar": "123412341234", "pan": "bad", "name": "Test"}
    r = client.post("/submit", json=payload)
    assert r.status_code == 400

def test_schema_endpoint():
    r = client.get("/schema")
    assert r.status_code in (200, 404)
