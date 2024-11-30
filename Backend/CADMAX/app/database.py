# app/database.py
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://punit:Punit3357@database.8lofl.mongodb.net/?retryWrites=true&w=majority&appName=users"
client = AsyncIOMotorClient(MONGO_URI)
db = client["Users"]
form=client["Forms"]
customer=client["Customer"]
attendence=client["Users"]

attendence_collection=db["attendence"]
users_collection = db["users"]
customer_collection=customer["customer"]
form_collection=form["forms"]



