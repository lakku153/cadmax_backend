# app/schemas.py
from datetime import datetime, timedelta
import logging
import bcrypt
import jwt
from bson import ObjectId
from .database import users_collection
from fastapi import Header, HTTPException, Depends
SECRET_KEY = "hvjgfvbcjhg"  # Use a stronger secret key in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Helper function to verify passwords
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

# Helper function to create JWT token
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.now() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_token_from_header(authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(status_code=403, detail="Authorization header missing")
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Invalid token format")
    
    return authorization.split(" ")[1]

async def get_current_user(token: str = Depends(get_token_from_header)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        logging.debug(f"Extracted username from JWT: {username}")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        user = await users_collection.find_one({"username": username})
        if not isinstance(username, str):
            logging.debug(f"Error: Username is not a string, it is a {type(username)}")
            raise HTTPException(status_code=401, detail="Invalid credentials: username is not a string")
        
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        return username
    except jwt.PyJWTError as e:
        logging.debug(f"JWT Error: {str(e)}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

# Middleware to verify token (protected route example)
# Middleware to verify token (protected route example)
# def verify_token(authorization: str = Header(None)):
#     if authorization is None or not authorization.startswith("Bearer "):
#         raise HTTPException(status_code=403, detail="Authorization header missing or malformed")
    
#     token = authorization.split(" ")[1]
    
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload  # Return the payload (e.g., user info)
#     except jwt.PyJWTError:
#         raise HTTPException(status_code=403, detail="Could not validate credentials")


