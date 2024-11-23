# app/main.py
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.Basemodels import ItemInDB, str_id
from app.security import get_current_user
from app.database import form_collection
router = APIRouter()

@router.get("/SurveyForm/", response_model=List[ItemInDB])
async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
    collection_name=f"{current_user}.SurveyForm"
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
    collection = form_collection[collection_name]
    # Query the MongoDB collection for tasks that match the provided date
    filtered_tasks =await collection.find({"create_date": query_date_str}).to_list(length=None)

    if not filtered_tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this date.")

    # Return the filtered tasks
    return [str_id(task) for task in filtered_tasks]

# @router.get("/Architecture/", response_model=List[ItemInDB])
# async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
#     try:
#         if date == "today":
#             query_date = datetime.now()
#         elif date == "yesterday":
#             query_date = datetime.now()+ timedelta(days=-1)
#         else:
#             query_date = datetime.strptime(date, "%Y-%m-%d")
#     except ValueError:
#         raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

#     # Convert the datetime object back to a string in the format "yyyy-mm-dd"
#     query_date_str = query_date.strftime("%Y-%m-%d")

#     # Query the MongoDB collection for tasks that match the provided date
#     filtered_tasks =await Architecture_collection.find({"create_date": query_date_str}).to_list(length=None)

#     if not filtered_tasks:
#         raise HTTPException(status_code=404, detail="No tasks found for this date.")

#     # Return the filtered tasks
#     return [str_id(task) for task in filtered_tasks]

# @router.get("/UrbanPlanning/", response_model=List[ItemInDB])
# async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
#     try:
#         if date == "today":
#             query_date = datetime.now()
#         elif date == "yesterday":
#             query_date = datetime.now()+ timedelta(days=-1)
#         else:
#             query_date = datetime.strptime(date, "%Y-%m-%d")
#     except ValueError:
#         raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

#     # Convert the datetime object back to a string in the format "yyyy-mm-dd"
#     query_date_str = query_date.strftime("%Y-%m-%d")

#     # Query the MongoDB collection for tasks that match the provided date
#     filtered_tasks =await UrbanPlanning_collection.find({"create_date": query_date_str}).to_list(length=None)

#     if not filtered_tasks:
#         raise HTTPException(status_code=404, detail="No tasks found for this date.")

#     # Return the filtered tasks
#     return [str_id(task) for task in filtered_tasks]

# @router.get("/EngineeringDrawing/", response_model=List[ItemInDB])
# async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
#     try:
#         if date == "today":
#             query_date = datetime.now()
#         elif date == "yesterday":
#             query_date = datetime.now()+ timedelta(days=-1)
#         else:
#             query_date = datetime.strptime(date, "%Y-%m-%d")
#     except ValueError:
#         raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

#     # Convert the datetime object back to a string in the format "yyyy-mm-dd"
#     query_date_str = query_date.strftime("%Y-%m-%d")

#     # Query the MongoDB collection for tasks that match the provided date
#     filtered_tasks =await EngineeringDrawing_collection.find({"create_date": query_date_str}).to_list(length=None)

#     if not filtered_tasks:
#         raise HTTPException(status_code=404, detail="No tasks found for this date.")

#     # Return the filtered tasks
#     return [str_id(task) for task in filtered_tasks]

# @router.get("/JDA/", response_model=List[ItemInDB])
# async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
#     try:
#         if date == "today":
#             query_date = datetime.now()
#         elif date == "yesterday":
#             query_date = datetime.now()+ timedelta(days=-1)
#         else:
#             query_date = datetime.strptime(date, "%Y-%m-%d")
#     except ValueError:
#         raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

#     # Convert the datetime object back to a string in the format "yyyy-mm-dd"
#     query_date_str = query_date.strftime("%Y-%m-%d")

#     # Query the MongoDB collection for tasks that match the provided date
#     filtered_tasks =await JDA_collection.find({"create_date": query_date_str}).to_list(length=None)

#     if not filtered_tasks:
#         raise HTTPException(status_code=404, detail="No tasks found for this date.")

#     # Return the filtered tasks
#     return [str_id(task) for task in filtered_tasks]

# @router.get("/GIS/", response_model=List[ItemInDB])
# async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
#     try:
#         if date == "today":
#             query_date = datetime.now()
#         elif date == "yesterday":
#             query_date = datetime.now()+ timedelta(days=-1)
#         else:
#             query_date = datetime.strptime(date, "%Y-%m-%d")
#     except ValueError:
#         raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

#     # Convert the datetime object back to a string in the format "yyyy-mm-dd"
#     query_date_str = query_date.strftime("%Y-%m-%d")

#     # Query the MongoDB collection for tasks that match the provided date
#     filtered_tasks =await GIS_collection.find({"create_date": query_date_str}).to_list(length=None)

#     if not filtered_tasks:
#         raise HTTPException(status_code=404, detail="No tasks found for this date.")

#     # Return the filtered tasks
#     return [str_id(task) for task in filtered_tasks]

# @router.get("/SitePlan/", response_model=List[ItemInDB])
# async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
#     try:
#         if date == "today":
#             query_date = datetime.now()
#         elif date == "yesterday":
#             query_date = datetime.now()+ timedelta(days=-1)
#         else:
#             query_date = datetime.strptime(date, "%Y-%m-%d")
#     except ValueError:
#         raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

#     # Convert the datetime object back to a string in the format "yyyy-mm-dd"
#     query_date_str = query_date.strftime("%Y-%m-%d")

#     # Query the MongoDB collection for tasks that match the provided date
#     filtered_tasks =await SitePlan_collection.find({"create_date": query_date_str}).to_list(length=None)

#     if not filtered_tasks:
#         raise HTTPException(status_code=404, detail="No tasks found for this date.")

#     # Return the filtered tasks
#     return [str_id(task) for task in filtered_tasks]

# @router.get("/AreaConversion/", response_model=List[ItemInDB])
# async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
#     try:
#         if date == "today":
#             query_date = datetime.now()
#         elif date == "yesterday":
#             query_date = datetime.now()+ timedelta(days=-1)
#         else:
#             query_date = datetime.strptime(date, "%Y-%m-%d")
#     except ValueError:
#         raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

#     # Convert the datetime object back to a string in the format "yyyy-mm-dd"
#     query_date_str = query_date.strftime("%Y-%m-%d")

#     # Query the MongoDB collection for tasks that match the provided date
#     filtered_tasks =await AreaConversion_collection.find({"create_date": query_date_str}).to_list(length=None)

#     if not filtered_tasks:
#         raise HTTPException(status_code=404, detail="No tasks found for this date.")

#     # Return the filtered tasks
#     return [str_id(task) for task in filtered_tasks]

# @router.get("/SectorSuperImpose/", response_model=List[ItemInDB])
# async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
#     try:
#         if date == "today":
#             query_date = datetime.now()
#         elif date == "yesterday":
#             query_date = datetime.now()+ timedelta(days=-1)
#         else:
#             query_date = datetime.strptime(date, "%Y-%m-%d")
#     except ValueError:
#         raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

#     # Convert the datetime object back to a string in the format "yyyy-mm-dd"
#     query_date_str = query_date.strftime("%Y-%m-%d")

#     # Query the MongoDB collection for tasks that match the provided date
#     filtered_tasks =await SectorSuperImpose_collection.find({"create_date": query_date_str}).to_list(length=None)

#     if not filtered_tasks:
#         raise HTTPException(status_code=404, detail="No tasks found for this date.")

#     # Return the filtered tasks
#     return [str_id(task) for task in filtered_tasks]


# @router.get("/Print/", response_model=List[ItemInDB])
# async def get_survey_form(date: str,current_user: str = Depends(get_current_user)):
#     try:
#         if date == "today":
#             query_date = datetime.now()
#         elif date == "yesterday":
#             query_date = datetime.now()+ timedelta(days=-1)
#         else:
#             query_date = datetime.strptime(date, "%Y-%m-%d")
#     except ValueError:
#         raise HTTPException(status_code=400, detail="Invalid date format. Use 'YYYY-MM-DD'.")

#     # Convert the datetime object back to a string in the format "yyyy-mm-dd"
#     query_date_str = query_date.strftime("%Y-%m-%d")

#     # Query the MongoDB collection for tasks that match the provided date
#     filtered_tasks =await Print_collection.find({"create_date": query_date_str}).to_list(length=None)

#     if not filtered_tasks:
#         raise HTTPException(status_code=404, detail="No tasks found for this date.")

#     # Return the filtered tasks
#     return [str_id(task) for task in filtered_tasks]





