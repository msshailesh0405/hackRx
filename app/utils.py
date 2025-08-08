from fastapi import HTTPException

def validate_token(provided_token: str, expected_token: str):
    """Check if the provided token matches the expected token."""
    if provided_token != f"Bearer {expected_token}":
        raise HTTPException(status_code=401, detail="Invalid or missing token")
