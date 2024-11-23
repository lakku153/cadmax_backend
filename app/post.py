from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
import app
from app.Basemodels import GIS, JDA, Architecture, AreaConversion, EngineeringDrawing, ItemInDB, Print, SectorSuperImpose, SitePlan, SurveyForm, UrbanPlanning, str_id
from app.database import users_collection,form_collection
from app.authorization import get_current_user

router = APIRouter()
def str_id(item) -> ItemInDB:
    item["id"] = str(item["_id"])  # Convert _id to string
    return ItemInDB(**item)

async def create_item(item: BaseModel,form_name: str,current_user:str):
    collection_name=f"{current_user}.{form_name}"
    create_datetime = datetime.now()
    create_date = create_datetime.strftime('%Y-%m-%d')
    create_time = create_datetime.strftime('%H:%M:%S')
    item_dict = {key: value for key, value in item.dict().items() if value is not None}
    item_dict["create_date"] = create_date  # Store date as string in yyyy-mm-dd format
    item_dict["create_time"] = create_time
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
    return await create_item(item, "Architecture")

# Urban Planning Form Endpoint
@router.post("/UrbanPlanning/", response_model=ItemInDB)
async def create_urban_planning(item: UrbanPlanning, current_user: str = Depends(get_current_user)):
    return await create_item(item, "UrbanPlanning")

# Engineering Drawing Form Endpoint
@router.post("/EngineeringDrawing/", response_model=ItemInDB)
async def create_engineering_drawing(item: EngineeringDrawing, current_user: str = Depends(get_current_user)):
    return await create_item(item, "EngineeringDrawing")

# JDA Form Endpoint
@router.post("/JDA/", response_model=ItemInDB)
async def create_jda(item: JDA, current_user: str = Depends(get_current_user)):
    return await create_item(item, "JDA")

# GIS Form Endpoint
@router.post("/GIS/", response_model=ItemInDB)
async def create_gis(item: GIS, current_user: str = Depends(get_current_user)):
    return await create_item(item, "GIS")

# Site Plan Form Endpoint
@router.post("/SitePlan/", response_model=ItemInDB)
async def create_site_plan(item: SitePlan, current_user: str = Depends(get_current_user)):
    return await create_item(item, "SitePlan")

# Area Conversion Form Endpoint
@router.post("/AreaConversion/", response_model=ItemInDB)
async def create_area_conversion(item: AreaConversion, current_user: str = Depends(get_current_user)):
    return await create_item(item, "AreaConversion")

# Sector Super Imposition Form Endpoint
@router.post("/SectorSuperImpose/", response_model=ItemInDB)
async def create_sector_super_impose(item: SectorSuperImpose, current_user: str = Depends(get_current_user)):
    return await create_item(item, "SectorSuperImpose")

# Print Form Endpoint
@router.post("/Print/", response_model=ItemInDB)
async def create_print(item: Print, current_user: str = Depends(get_current_user)):
    return await create_item(item, "Print")