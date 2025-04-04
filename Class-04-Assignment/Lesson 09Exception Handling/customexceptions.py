class InvalidEmailError(Exception):
    """Raised when an email doesn't contain @ symbol"""
    pass

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError("Email must contain @ symbol")

try:
    validate_email("user.example.com")
except InvalidEmailError as e:
    print(f"Email validation failed: {e}")