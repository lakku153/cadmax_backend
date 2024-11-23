from bson import ObjectId
from pydantic import BaseModel

# Pydantic Models for user registration and login
class User(BaseModel):
    username: str
    password: str
    Jobrole:str

class UserInDB(User):
    hashed_password: str


class User1(BaseModel):
    username: str
    password: str

class customer(BaseModel):
    ClientName:str
    Company:str
    Contect:int
    Address:str
class customer1(BaseModel):
    ClientName:str
    Company:str
    Contect:int

class Token(BaseModel):
    access_token: str
    token_type: str



class ItemInDB(BaseModel):
    id: str
    # department:str
    ClientName:str
    TotalArea: float
    TotalCost: float
    Remarks:str

    
    class Config:
        # Convert Mongo ObjectId to string
        json_encoders = {
            ObjectId: str
        }  # Allows Pydantic to work with ORM models, e.g., MongoDB, SQLAlchemy


# Survey Form Model
class SurveyForm(BaseModel):
    ClientName: str
    TypeOfSurvey: str
    KhasraNo: str
    TotalArea: float
    Demarcation: str
    DayInSurvey: str
    TotalCost: float
    Remarks: str

class SurveyFormInDB(ItemInDB, SurveyForm):
    pass

# Architecture Model
class Architecture(BaseModel):
    ClientName: str
    BuildingType: str
    Location: str
    TotalArea: float
    TotalCost: float
    DesignStyle: str
    Remarks: str

class ArchitectureInDB(ItemInDB, Architecture):
    pass

# Urban Planning Model
class UrbanPlanning(BaseModel):
    ClientName: str
    KhasraNo: str
    TotalArea: float
    Demarcation: str
    TotalCost: float
    Remarks: str

class UrbanPlanningInDB(ItemInDB, UrbanPlanning):
    pass

# Engineering Drawing Model
class EngineeringDrawing(BaseModel):
    ClientName: str
    KhasraNo: str
    TotalArea: float
    TotalCost: float
    Remarks: str

class EngineeringDrawingInDB(ItemInDB, EngineeringDrawing):
    pass

# JDA Model
class JDA(BaseModel):
    ClientName: str
    KhasraNo: str
    TotalArea: float
    TotalCost: float
    Remarks: str

class JDAInDB(ItemInDB, JDA):
    pass

# GIS Model
class GIS(BaseModel):
    ClientName: str
    NameOfScheme: str
    KhasraNo: str
    TotalArea: float
    TotalCost: float
    Remarks: str

class GISInDB(ItemInDB, GIS):
    pass

# Site Plan Model
class SitePlan(BaseModel):
    ClientName: str
    NumberOfPlots: int
    KhasraNo: str
    TotalArea: float
    NumberOfShops: int
    TotalCost: float
    Remarks: str

class SitePlanInDB(ItemInDB, SitePlan):
    pass

# Area Conversion Model
class AreaConversion(BaseModel):
    ClientName: str
    KhasraNo: str
    TotalArea: float
    TotalCost: float
    Remarks: str

class AreaConversionInDB(ItemInDB, AreaConversion):
    pass

# Sector Super Imposition Model
class SectorSuperImpose(BaseModel):
    ClientName: str
    KhasraNo: str
    TotalArea: float
    TotalCost: float
    Remarks: str

class SectorSuperImposeInDB(ItemInDB, SectorSuperImpose):
    pass

# Print Model
class Print(BaseModel):
    ClientName: str
    TypeOfprint: str
    KhasraNo: str
    Papersize: str
    TotalArea: float
    TotalCost:float
    Remarks: str

class PrintInDB(ItemInDB, Print):
    pass


# Helper function to convert MongoDB's _id to string for ItemInDB
def str_id(item) -> ItemInDB:
    item["id"] = str(item["_id"])  
    return ItemInDB(**item)


# class forgot(BaseModel):
#     username: str
#     password: str