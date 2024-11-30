
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from app.Basemodels import User, Token, User1, customer, customer1, profile
from app.functions import get_user_by_username
from app.security import create_access_token, verify_password,hash_password
from app.database import MONGO_URI, users_collection,customer_collection
from app.get import router
from app.post import router as post_router
from motor.motor_asyncio import AsyncIOMotorClient
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow only your frontend
    # allow_origins=["http://192.168.1.81:3000"],  # Allow only your frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI app!"}

@app.post("/register/", response_model=User)
async def register(user: User):
    # Check if the user already exists
    existing_user = await users_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password before storing it
    hashed_password = hash_password(user.password)


    # Create the user in the database
    new_user = {**user.dict(), "hashed_password": hashed_password}
    result = await users_collection.insert_one(new_user)
    created_user = await users_collection.find_one({"_id": result.inserted_id})
    return User(username=created_user["username"], password=created_user["password"],Jobrole=created_user["Jobrole"])

@app.post("/login/", response_model=Token)
async def login(user: User1):
    db_user = await get_user_by_username(user.username)
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}
   
app.include_router(router)
app.include_router(post_router)



@app.post("/customer_register/", response_model=customer1)
async def register(user: customer):
    # Check if the user already exists
    existing_user = await customer_collection.find_one({"ClientName": user.ClientName})
    if existing_user:
        raise HTTPException(status_code=400, detail="Already registered")

    result = await customer_collection.insert_one(user.dict())
    created_user = await customer_collection.find_one({"_id": result.inserted_id})

    return customer1(ClientName=created_user["ClientName"],Company=created_user["Company"],Contect=created_user["Contact"])
































# async def get_user_me(current_user: str = Depends(get_current_user)):
#     user = await users_collection.find_one({"username": current_user})
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return User(username=user["username"])



# @app.post("/logout/")
# async def logout(response: Response, token: str = Depends(get_token_from_header)):
#     # Decode the token
#     payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

#     # Modify the expiration time to a past date (immediately invalidate the token)
#     payload["exp"] = datetime.now() - timedelta(seconds=1)  # Set expiration to the past (1 second ago)

#     # Re-encode the token with the new expiration time
#     invalidated_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

#     # Optionally, delete the access token cookie (if you're using cookies)
#     response.delete_cookie("access_token")
    
#     # Return a response confirming the logout
#     return JSONResponse(content={"message": "Successfully logged out"})

# @app.post("/changepassword/")

# async def change_password(request: ChangePasswordRequest, current_user: str = Depends(get_current_user)):
#     # Fetch the user from the database
#     user = await users_collection.find_one({"email": current_user})
    
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     # Verify the current password
#     if not verify_password(request.current_password, user["hashed_password"]):
#         raise HTTPException(status_code=400, detail="Current password is incorrect")

#     # Validate the new password
#     if len(request.new_password) < 6:
#         raise HTTPException(status_code=400, detail="New password must be at least 6 characters long")
#     if not is_password_strong(request.new_password):
#         raise HTTPException(status_code=400, detail="New password must contain an uppercase letter, a number, and a special character")

#     # Hash the new password
#     new_hashed_password = hash_password(request.new_password)

#     # Update the password in the database
#     await users_collection.update_one({"email": current_user}, {"$set": {"hashed_password": new_hashed_password, "password": request.new_password}})
#     return JSONResponse(content={"message": "Password successfully changed"})

# @app.delete("/users/me/")
# async def delete_account(current_user: str = Depends(get_current_user)):
#     # Fetch the current user from the database
#     user = await users_collection.find_one({"email": current_user})
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")

#     # Delete the user from the database
#     await users_collection.delete_one({"email": current_user})

#     return {"message": "User account deleted successfully"}


# @app.get("/users/me/", response_model=User)
# async def get_user_me(current_user: str = Depends(get_current_user)):
#     user = await users_collection.find_one({"username": current_user})
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return User(username=user["username"], password=user["username"])


# @app.get("/users/{user_id}", response_model=User)
# async def get_user_by_id(user_id: str):
#     # Convert the user_id to an ObjectId
#     try:
#         object_id = ObjectId(user_id)
#     except Exception:
#         raise HTTPException(status_code=400, detail="Invalid user ID format")

#     user = await users_collection.find_one({"_id": object_id})
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     return User(username=user["username"], email=user["email"], password="")

# @app.get("/users/", response_model=List[User])
# async def list_all_users(current_user: str = Depends(get_current_user)):
#     # Fetch the current user's details
#     user = await users_collection.find_one({"email": current_user})
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     # Check if the user is an admin (you could add a role field in your DB)
#     if user.get("role") != "admin":
#         raise HTTPException(status_code=403, detail="Access denied")

#     # Fetch all users from the database
#     users_cursor = users_collection.find()
#     users_list = await users_cursor.to_list(length=100)  # Adjust length as needed
#     return [User(username=user["username"], email=user["email"]) for user in users_list]

# @app.delete("/admin/users/{user_id}/delete/")
# async def delete_user_by_admin(user_id: str, current_user: str = Depends(get_current_user)):
#     # Fetch the current user from the database
#     admin_user = await users_collection.find_one({"email": current_user})
#     if admin_user is None:
#         raise HTTPException(status_code=404, detail="User not found")

#     # Check if the user is an admin
#     if admin_user.get("role") != "admin":
#         raise HTTPException(status_code=403, detail="Admin privileges required")

#     # Convert the user_id to ObjectId
#     try:
#         object_id = ObjectId(user_id)
#     except Exception:
#         raise HTTPException(status_code=400, detail="Invalid user ID format")

#     # Fetch the user to be deleted
#     user_to_delete = await users_collection.find_one({"_id": object_id})
#     if user_to_delete is None:
#         raise HTTPException(status_code=404, detail="User not found")

#     # Delete the user
#     await users_collection.delete_one({"_id": object_id})

#     return {"message": f"User {user_to_delete['username']} deleted successfully"}