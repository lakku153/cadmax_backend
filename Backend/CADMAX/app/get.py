# app/main.py
from datetime import datetime, timedelta
from pydoc import doc
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.Basemodels import CustomerName, ItemInDB, customer1, customerworking, profile, str_id, work
from app.security import get_current_user
from app.database import form_collection,customer_collection,users_collection
router = APIRouter()

@router.get("/SurveyForm/", response_model=List[ItemInDB])
async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
    collection_name=f"{current_user}"
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
    collection_name=f"{current_user}"
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
    collection_name=f"{current_user}"
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
    collection_name=f"{current_user}"
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
    collection_name=f"{current_user}"
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
    collection_name=f"{current_user}"
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
    collection_name=f"{current_user}"
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
    collection_name=f"{current_user}"
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
    collection_name=f"{current_user}"
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
    collection_name=f"{current_user}"
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
async def get_customer_detail(name: str,current_user: str = Depends(get_current_user)):
    # Query the database to find the user by ClientName
    collection_name=current_user

    existing_user = await customer_collection[collection_name].find_one({"name": name})

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
async def get_customer_detail(current_user: str = Depends(get_current_user)):
    # Query the database to find the user by ClientName
    username=current_user
    existing_user = await users_collection.find_one({"username": username})
    # Return the customer details
    return profile(
        username=existing_user["username"],
        Jobrole=existing_user["Jobrole"]
    )

@router.get("/customers/", response_model=List[CustomerName])
async def get_customers(current_user: str = Depends(get_current_user)):
    try:
        # Fetch only the names from the database
        collection_name=f"{current_user}"
        customers = await customer_collection[collection_name].find({}, {"name": 1}).to_list(length=None)
        if not customers:
            return []
        # Convert the MongoDB data into the Pydantic CustomerName model
        return [CustomerName(name=customer["name"]) for customer in customers]
    
    except Exception as e:
        return {"error": f"Failed to fetch customers: {str(e)}"}
    
    
@router.get("/employee_working/", response_model=List[work])
async def get_customer_detail(date:str,current_user: str = Depends(get_current_user)):
    # if date=="Today":
    #     date = datetime.now().strftime("%Y-%m-%d")
    # elif date=="Yesterday":
    #     date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    
    # collection_name=f"{current_user
    # Query the database to find the user by ClientName
    collection_name=current_user
    existing = form_collection[collection_name].find({"create_date": date})
    existing = await existing.to_list(length=100)
    if not existing:
        # If user not found, raise an exception
        raise HTTPException(status_code=404, detail="No working for this date")

    return [work(
        Department=doc["Department"],
        TotalArea=doc["TotalArea"],    
        TotalCost=doc["TotalCost"],     
        ClientName=doc["ClientName"],    
    ) for doc in existing]

@router.get("/customer_working/", response_model=customerworking)
async def get_customer_detail(date: str, name:str,current_user: str = Depends(get_current_user)):

    collection_name=current_user
      
    if date=="Today":
        date = datetime.now().strftime("%Y-%m-%d")
    elif date=="Yesterday":
        date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    cursor = await form_collection[collection_name].find_one({ "ClientName": name,"create_date": date})
    # existing_user = await cursor.to_list(length=100)
    
    if not cursor:
       raise HTTPException(status_code=404, detail="No working for this date")
    
    
    return customerworking(
            Department=cursor["Department"],  # Default to "unknown" if Department is missing
            TotalCost=cursor["TotalCost"],  # Default to 0 if TotalCost is missing
            TotalArea=cursor["TotalArea"],  # Default to 0 if TotalArea is missing
            Staff=cursor["staff"],# Default if Remarks are missing
            Working=cursor["Remarks"] 
        )
