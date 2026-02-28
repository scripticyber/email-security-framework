import pytest
from app.utils.email_parser import parse_email

SAMPLE_EMAIL = """From: test@example.com
Subject: Test Email

Hello world!
"""

def test_parse_simple_email():
    result = parse_email(SAMPLE_EMAIL)
    assert "headers" in result
    assert result["headers"]["Subject"] == "Test Email"
    assert "body" in result
    assert "Hello world!" in result["body"]