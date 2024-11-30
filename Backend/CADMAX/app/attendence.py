# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import Optional
# from geopy.geocoders import Nominatim

# app = FastAPI()

# # Define a Pydantic model for the attendance data
# class Attendance(BaseModel):
#     employee_id: str
#     address: str
#     location: Optional[str] = None  # latitude, longitude or address can be optional
#     date_time: str  # The datetime when attendance is recorded

# # Initialize geocoder (Nominatim is a free geocoder provided by OpenStreetMap)
# geolocator = Nominatim(user_agent="attendance_app")

# # Function to geocode an address
# def geocode_address(address: str):
#     try:
#         location = geolocator.geocode(address)
#         if location:
#             return (location.latitude, location.longitude)
#         else:
#             raise HTTPException(status_code=404, detail="Address not found")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Geocoding error: {e}")

# # Endpoint to record attendance
# @app.post("/record_attendance/")
# async def record_attendance(attendance: Attendance):
#     try:
#         # Geocode the address to get latitude and longitude
#         if attendance.address:
#             latitude, longitude = geocode_address(attendance.address)
#             attendance.location = f"Lat: {latitude}, Lon: {longitude}"
        
#         # In a real application, save this data to a database
#         print(f"Attendance Recorded: {attendance}")

#         # For now, return the received data as a response
#         return {
#             "message": "Attendance successfully recorded",
#             "data": attendance
#         }
#     except HTTPException as e:
#         raise e
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

# # To run the FastAPI app, use the following command:
# # uvicorn app_name:app --reload
