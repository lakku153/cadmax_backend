from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.Basemodels import GIS, JDA, Architecture, AreaConversion, Attendence, EngineeringDrawing, ItemInDB, Print, SectorSuperImpose, SitePlan, SurveyForm, UrbanPlanning, customer, customer1, str_id
from app.database import form_collection,customer_collection,attendence_collection
from app.authorization import get_current_user
router = APIRouter()
def str_id(item) -> ItemInDB:
    item["id"] = str(item["_id"])  # Convert _id to string
    return ItemInDB(**item)

async def create_item(item: BaseModel,form_name: str,current_user:str):
    collection_name=current_user
    create_datetime = datetime.now()
    create_date = create_datetime.strftime('%Y-%m-%d')
    create_time = create_datetime.strftime('%H:%M:%S')
    item_dict = {key: value for key, value in item.dict().items() if value is not None}
    item_dict["create_date"] = create_date  # Store date as string in yyyy-mm-dd format
    item_dict["create_time"] = create_time
    item_dict["Department"] =form_name
    item_dict["staff"] = current_user
    result = await form_collection[collection_name].insert_one(item_dict)
    new_item = await form_collection[collection_name].find_one({"_id": result.inserted_id})
    return str_id(new_item)

# Survey Form Endpoint
@router.post("/SurveyForm/", response_model=ItemInDB)
async def create_survey_form(item: SurveyForm,current_user: str = Depends(get_current_user)):
    return await create_item(item, "SurveyForm",current_user)



# Architecture Form Endpoint
@router.post("/Architecture/", response_model=ItemInDB)
async def create_architecture(item: Architecture, current_user: str = Depends(get_current_user)):
    return await create_item(item, "Architecture",current_user)

# Urban Planning Form Endpoint
@router.post("/UrbanPlanning/", response_model=ItemInDB)
async def create_urban_planning(item: UrbanPlanning, current_user: str = Depends(get_current_user)):
    return await create_item(item, "UrbanPlanning",current_user)

# Engineering Drawing Form Endpoint
@router.post("/EngineeringDrawing/", response_model=ItemInDB)
async def create_engineering_drawing(item: EngineeringDrawing, current_user: str = Depends(get_current_user)):
    return await create_item(item, "EngineeringDrawing",current_user)

# JDA Form Endpoint
@router.post("/JDA/", response_model=ItemInDB)
async def create_jda(item: JDA, current_user: str = Depends(get_current_user)):
    return await create_item(item, "JDA",current_user)

# GIS Form Endpoint
@router.post("/GIS/", response_model=ItemInDB)
async def create_gis(item: GIS, current_user: str = Depends(get_current_user)):
    return await create_item(item, "GIS",current_user)

# Site Plan Form Endpoint
@router.post("/SitePlan/", response_model=ItemInDB)
async def create_site_plan(item: SitePlan, current_user: str = Depends(get_current_user)):
    return await create_item(item, "SitePlan",current_user)

# Area Conversion Form Endpoint
@router.post("/AreaConversion/", response_model=ItemInDB)
async def create_area_conversion(item: AreaConversion, current_user: str = Depends(get_current_user)):
    return await create_item(item, "AreaConversion",current_user)

# Sector Super Imposition Form Endpoint
@router.post("/SectorSuperImpose/", response_model=ItemInDB)
async def create_sector_super_impose(item: SectorSuperImpose, current_user: str = Depends(get_current_user)):
    return await create_item(item, "SectorSuperImpose",current_user)

# Print Form Endpoint
@router.post("/Print/", response_model=ItemInDB)
async def create_print(item: Print, current_user: str = Depends(get_current_user)):
    return await create_item(item, "Print",current_user)


@router.post("/customer_register/", response_model=customer1)
async def register(user: customer, current_user: str = Depends(get_current_user)):
    # Check if the user already exists
    collection_name=current_user
    create_datetime = datetime.now()
    create_date = create_datetime.strftime('%Y-%m-%d')
    existing_user = await customer_collection[collection_name].find_one({"name": user.name})
    if existing_user:
        raise HTTPException(status_code=400, detail="Already registered")

    user_data = user.dict()  
    user_data["create_date"] = create_date 
    user_data["staff"] = current_user
    result = await customer_collection[collection_name].insert_one(user_data)
    created_user = await customer_collection[collection_name].find_one({"_id": result.inserted_id})
    return customer1(name=created_user["name"],company=created_user["company"],contact=created_user["contact"])


@router.post("/record_attendance/",response_model=Attendence)
async def record_attendance(address: Attendence, current_user: str = Depends(get_current_user)):
    name=current_user
    attendence=address.dict()
    attendence["employee"]=name
    result = await attendence_collection.insert_one(attendence)
    address = await attendence_collection.find_one({"_id": result.inserted_id})
    return  Attendence(location=address["location"],address=address["address"],date_time=address["date_time"])
    
