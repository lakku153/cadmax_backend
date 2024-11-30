# app/crud.py
from app.Basemodels import  UserInDB, User
from app.database import users_collection
from app.security import hash_password
from fastapi import HTTPException
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
async def create_user(user: User) -> UserInDB:
    # Check if the user already exists
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password before storing it
    hashed_password = hash_password(user.password)

    # Create the user in the database
    new_user = {**user.dict(), "hashed_password": hashed_password}
    result = await users_collection.insert_one(new_user)
    created_user = await users_collection.find_one({"_id": result.inserted_id})

    return UserInDB(username=created_user["username"], email=created_user["email"], hashed_password="")

async def get_user_by_username(username: str) -> UserInDB:
    user = await users_collection.find_one({"username": username})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserInDB(**user)





geolocator = Nominatim(user_agent="attendance_app")
def geocode_address(address: str):
    retries = 3
    for _ in range(retries):
        try:
            location = geolocator.geocode(address)
            if location:
                return (location.latitude, location.longitude)
            else:
                raise HTTPException(status_code=404, detail="Address not found")
        except GeocoderTimedOut:
            time.sleep(2)  # Wait for 2 seconds before retrying
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Geocoding error: {e}")
    raise HTTPException(status_code=500, detail="Geocoding request failed after multiple retries")

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
