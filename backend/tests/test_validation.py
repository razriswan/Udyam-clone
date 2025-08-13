import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.validation import validate_aadhaar, validate_pan, validate_email, validate_otp

def test_aadhaar_valid():
    assert validate_aadhaar("123412341234")

def test_aadhaar_invalid():
    assert not validate_aadhaar("1234")

def test_pan_valid():
    assert validate_pan("ABCDE1234F")

def test_pan_invalid():
    assert not validate_pan("abc")

def test_email_valid():
    assert validate_email("a@b.com")

def test_email_invalid():
    assert not validate_email("bad@")

def test_otp_optional_and_valid():
    assert validate_otp(None)
    assert validate_otp("1234")
    assert validate_otp("123456")

def test_otp_invalid():
    assert not validate_otp("12")
