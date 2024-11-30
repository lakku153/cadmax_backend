from typing import Optional
from bson import ObjectId
from pydantic import BaseModel

# Pydantic Models for user registration and login
class User(BaseModel):
    username: str
    password: str
    Jobrole:str

class UserInDB(User):
    hashed_password: str
class profile(BaseModel):
    username:str
    Jobrole:str

class User1(BaseModel):
    username: str
    password: str
class CustomerName(BaseModel):
    name: str
    class Config:
        orm_mode = True
class customer(BaseModel):
    name:str
    company:str
    contact:str
    address:str

class customer1(BaseModel):
    name:str
    company:str
    contact:str

class Token(BaseModel):
    access_token: str
    token_type: str



class ItemInDB(BaseModel):
    id: str
    Department:str
    TotalArea: str
    TotalCost: str
    Remarks:str
    ClientName:str

    
    class Config:
        # Convert Mongo ObjectId to string
        json_encoders = {
            ObjectId: str
        }  # Allows Pydantic to work with ORM models, e.g., MongoDB, SQLAlchemy


class SurveyForm(BaseModel):
    ClientName: str
    TypeOfSurvey: str
    KhasraNo: str
    TotalArea: str
    Demarcation: str
    DayInSurvey: str
    TotalCost: str
    Remarks: str

class SurveyFormInDB(ItemInDB, SurveyForm):
    pass

# Architecture Model
class Architecture(BaseModel):
    ClientName: str
    BuildingType: str
    Location: str
    TotalArea: str
    TotalCost: str
    DesignStyle: str
    Remarks: str

class ArchitectureInDB(ItemInDB, Architecture):
    pass

# Urban Planning Model
class UrbanPlanning(BaseModel):
    ClientName: str
    KhasraNo: str
    TotalArea: str
    Demarcation: str
    TotalCost: str
    Remarks: str

class UrbanPlanningInDB(ItemInDB, UrbanPlanning):
    pass

# Engineering Drawing Model
class EngineeringDrawing(BaseModel):
    ClientName: str
    KhasraNo: str
    TotalArea: str
    TotalCost: str
    Remarks: str

class EngineeringDrawingInDB(ItemInDB, EngineeringDrawing):
    pass

# JDA Model
class JDA(BaseModel):
    ClientName: str
    KhasraNo: str
    TotalArea: str
    TotalCost: str
    Remarks: str

class JDAInDB(ItemInDB, JDA):
    pass

# GIS Model
class GIS(BaseModel):
    ClientName: str
    NameOfScheme: str
    KhasraNo: str
    TotalArea: str
    TotalCost: str
    Remarks: str

class GISInDB(ItemInDB, GIS):
    pass

# Site Plan Model
class SitePlan(BaseModel):
    ClientName: str
    NumberOfPlots: int
    KhasraNo: str
    TotalArea: str
    NumberOfShops: int
    TotalCost: str
    Remarks: str

class SitePlanInDB(ItemInDB, SitePlan):
    pass

# Area Conversion Model
class AreaConversion(BaseModel):
    ClientName: str
    KhasraNo: str
    TotalArea: str
    TotalCost: str
    Remarks: str

class AreaConversionInDB(ItemInDB, AreaConversion):
    pass

# Sector Super Imposition Model
class SectorSuperImpose(BaseModel):
    ClientName: str
    KhasraNo: str
    TotalArea: str
    TotalCost: str
    Remarks: str

class SectorSuperImposeInDB(ItemInDB, SectorSuperImpose):
    pass

# Print Model
class Print(BaseModel):
    ClientName: str
    TypeOfprint: str
    KhasraNo: str
    Papersize: str
    TotalArea: str
    TotalCost:str
    Remarks: str


# Helper function to convert MongoDB's _id to string for ItemInDB
def str_id(item) -> ItemInDB:
    item["id"] = str(item["_id"])  
    return ItemInDB(**item)


class work(BaseModel):
    
    Department:str
    TotalArea: str
    TotalCost: str
    ClientName:str

class customerworking(BaseModel):
    Department: str
    TotalCost:str
    Working:str
    Staff:str
    TotalArea: str

# Define a Pydantic model for the attendance data
class Attendence(BaseModel):
    location: str
    address:str
    date_time: str
   
