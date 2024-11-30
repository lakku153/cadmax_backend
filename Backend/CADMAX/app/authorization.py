# app/auth.py
from fastapi import HTTPException, Header, Depends
import jwt
from app.security import SECRET_KEY, ALGORITHM
from fastapi import HTTPException
import re
def get_token_from_header(authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(status_code=403, detail="Authorization header missing")
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Invalid token format")
    
    return authorization.split(" ")[1]

def get_current_user(token: str = Depends(get_token_from_header)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return email
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials")

def is_password_strong(password: str) -> bool:
    # Require at least one uppercase letter, one digit, and one special character
    return bool(re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password))

