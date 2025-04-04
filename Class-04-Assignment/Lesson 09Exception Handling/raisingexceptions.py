def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age < 18:
        raise ValueError("Must be at least 18 years old")
    else:
        print("Age is valid")

try:
    validate_age(-5)
except ValueError as e:
    print(f"Invalid age: {e}")