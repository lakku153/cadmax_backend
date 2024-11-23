# app/main.py
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.Basemodels import CustomerName, ItemInDB, customer1, profile, str_id
from app.security import get_current_user
from app.database import form_collection,customer_collection,users_collection
router = APIRouter()

@router.get("/SurveyForm/", response_model=List[ItemInDB])
async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
    collection_name=f"{current_user}.SurveyForm"
    collection = form_collection[collection_name]
    try:
        if date == "today":
            query_date = datetime.now()
        elif date == "yesterday":
            query_date = datetime.now()+ timedelta(days=-1)
        else:
            query_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

    # Convert the datetime object back to a string in the format "yyyy-mm-dd"
    query_date_str = query_date.strftime("%Y-%m-%d")
    
    # Query the MongoDB collection for tasks that match the provided date
    filtered_tasks =await collection.find({"create_date": query_date_str}).to_list(length=None)

    if not filtered_tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this date.")

    # Return the filtered tasks
    return [str_id(task) for task in filtered_tasks]

@router.get("/Architecture/", response_model=List[ItemInDB])
async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
    collection_name=f"{current_user}.Architecture"
    collection = form_collection[collection_name]
    try:
        if date == "today":
            query_date = datetime.now()
        elif date == "yesterday":
            query_date = datetime.now()+ timedelta(days=-1)
        else:
            query_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

    # Convert the datetime object back to a string in the format "yyyy-mm-dd"
    query_date_str = query_date.strftime("%Y-%m-%d")

    # Query the MongoDB collection for tasks that match the provided date
    filtered_tasks =await collection.find({"create_date": query_date_str}).to_list(length=None)

    if not filtered_tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this date.")

    # Return the filtered tasks
    return [str_id(task) for task in filtered_tasks]

@router.get("/UrbanPlanning/", response_model=List[ItemInDB])
async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
    collection_name=f"{current_user}.UrbanPlanning"
    collection = form_collection[collection_name]
    try:
        if date == "today":
            query_date = datetime.now()
        elif date == "yesterday":
            query_date = datetime.now()+ timedelta(days=-1)
        else:
            query_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

    # Convert the datetime object back to a string in the format "yyyy-mm-dd"
    query_date_str = query_date.strftime("%Y-%m-%d")

    # Query the MongoDB collection for tasks that match the provided date
    filtered_tasks =await collection.find({"create_date": query_date_str}).to_list(length=None)

    if not filtered_tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this date.")

    # Return the filtered tasks
    return [str_id(task) for task in filtered_tasks]

@router.get("/EngineeringDrawing/", response_model=List[ItemInDB])
async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
    collection_name=f"{current_user}.EngineeringDrawing"
    collection = form_collection[collection_name]
    try:
        if date == "today":
            query_date = datetime.now()
        elif date == "yesterday":
            query_date = datetime.now()+ timedelta(days=-1)
        else:
            query_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

    # Convert the datetime object back to a string in the format "yyyy-mm-dd"
    query_date_str = query_date.strftime("%Y-%m-%d")

    # Query the MongoDB collection for tasks that match the provided date
    filtered_tasks =await collection.find({"create_date": query_date_str}).to_list(length=None)

    if not filtered_tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this date.")

    # Return the filtered tasks
    return [str_id(task) for task in filtered_tasks]

@router.get("/JDA/", response_model=List[ItemInDB])
async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
    collection_name=f"{current_user}.JDA"
    collection = form_collection[collection_name]
    try:
        if date == "today":
            query_date = datetime.now()
        elif date == "yesterday":
            query_date = datetime.now()+ timedelta(days=-1)
        else:
            query_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

    # Convert the datetime object back to a string in the format "yyyy-mm-dd"
    query_date_str = query_date.strftime("%Y-%m-%d")

    # Query the MongoDB collection for tasks that match the provided date
    filtered_tasks =await collection.find({"create_date": query_date_str}).to_list(length=None)

    if not filtered_tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this date.")

    # Return the filtered tasks
    return [str_id(task) for task in filtered_tasks]

@router.get("/GIS/", response_model=List[ItemInDB])
async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
    collection_name=f"{current_user}.GIS"
    collection = form_collection[collection_name]
    try:
        if date == "today":
            query_date = datetime.now()
        elif date == "yesterday":
            query_date = datetime.now()+ timedelta(days=-1)
        else:
            query_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

    # Convert the datetime object back to a string in the format "yyyy-mm-dd"
    query_date_str = query_date.strftime("%Y-%m-%d")

    # Query the MongoDB collection for tasks that match the provided date
    filtered_tasks =await collection.find({"create_date": query_date_str}).to_list(length=None)

    if not filtered_tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this date.")

    # Return the filtered tasks
    return [str_id(task) for task in filtered_tasks]

@router.get("/SitePlan/", response_model=List[ItemInDB])
async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
    collection_name=f"{current_user}.SitePlan"
    collection = form_collection[collection_name]
    try:
        if date == "today":
            query_date = datetime.now()
        elif date == "yesterday":
            query_date = datetime.now()+ timedelta(days=-1)
        else:
            query_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

    # Convert the datetime object back to a string in the format "yyyy-mm-dd"
    query_date_str = query_date.strftime("%Y-%m-%d")

    # Query the MongoDB collection for tasks that match the provided date
    filtered_tasks =await collection.find({"create_date": query_date_str}).to_list(length=None)

    if not filtered_tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this date.")

    # Return the filtered tasks
    return [str_id(task) for task in filtered_tasks]

@router.get("/AreaConversion/", response_model=List[ItemInDB])
async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
    collection_name=f"{current_user}.AreaConversion"
    collection = form_collection[collection_name]
    try:
        if date == "today":
            query_date = datetime.now()
        elif date == "yesterday":
            query_date = datetime.now()+ timedelta(days=-1)
        else:
            query_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

    # Convert the datetime object back to a string in the format "yyyy-mm-dd"
    query_date_str = query_date.strftime("%Y-%m-%d")

    # Query the MongoDB collection for tasks that match the provided date
    filtered_tasks =await collection.find({"create_date": query_date_str}).to_list(length=None)

    if not filtered_tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this date.")

    # Return the filtered tasks
    return [str_id(task) for task in filtered_tasks]

@router.get("/SectorSuperImpose/", response_model=List[ItemInDB])
async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
    collection_name=f"{current_user}.SectorSuperImpose"
    collection = form_collection[collection_name]
    try:
        if date == "today":
            query_date = datetime.now()
        elif date == "yesterday":
            query_date = datetime.now()+ timedelta(days=-1)
        else:
            query_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

    # Convert the datetime object back to a string in the format "yyyy-mm-dd"
    query_date_str = query_date.strftime("%Y-%m-%d")

    # Query the MongoDB collection for tasks that match the provided date
    filtered_tasks =await collection.find({"create_date": query_date_str}).to_list(length=None)

    if not filtered_tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this date.")

    # Return the filtered tasks
    return [str_id(task) for task in filtered_tasks]


@router.get("/Print/", response_model=List[ItemInDB])
async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
    collection_name=f"{current_user}.Print"
    collection = form_collection[collection_name]
    try:
        if date == "today":
            query_date = datetime.now()
        elif date == "yesterday":
            query_date = datetime.now()+ timedelta(days=-1)
        else:
            query_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

    # Convert the datetime object back to a string in the format "yyyy-mm-dd"
    query_date_str = query_date.strftime("%Y-%m-%d")

    # Query the MongoDB collection for tasks that match the provided date
    filtered_tasks =await collection.find({"create_date": query_date_str}).to_list(length=None)

    if not filtered_tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this date.")

    # Return the filtered tasks
    return [str_id(task) for task in filtered_tasks]

from fastapi import HTTPException

@router.get("/customer_detail/", response_model=customer1)
async def get_customer_detail(name: str):
    # Query the database to find the user by ClientName
    existing_user = await customer_collection.find_one({"name": name})

    if not existing_user:
        # If user not found, raise an exception
        raise HTTPException(status_code=404, detail="Customer not found")

    # Return the customer details
    return customer1(
        name=existing_user["name"],
        company=existing_user["company"],
        contact=existing_user["contact"]
    )



@router.get("/profile/", response_model=profile)
async def get_customer_detail(username: str):
    # Query the database to find the user by ClientName
    existing_user = await users_collection.find_one({"username": username})
    # Return the customer details
    return profile(
        username=existing_user["username"],
        Jobrole=existing_user["Jobrole"]
    )

@router.get("/customers/", response_model=List[CustomerName])
async def get_customers():
    try:
        # Fetch only the names from the database
        customers = await customer_collection.find({}, {"name": 1}).to_list(length=None)
        if not customers:
            return []
        # Convert the MongoDB data into the Pydantic CustomerName model
        return [CustomerName(name=customer["name"]) for customer in customers]
    
    except Exception as e:
        return {"error": f"Failed to fetch customers: {str(e)}"}