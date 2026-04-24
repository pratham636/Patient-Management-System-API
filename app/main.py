from fastapi import FastAPI,Path ,HTTPException,Query
from fastapi.responses import JSONResponse  
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
from .schemas import Patient, PatientUpdate
from .database import load_data, save_data

app=FastAPI()



@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get("/about")
def about():
    return {"message":"A fully functional API to manage your patient records"}

@app.get('/view') 
def view():
    data=load_data() 
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description='ID of the patient in the DB',example=['P001'])):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException (status_code=404,detail='Patient not found')

@app.get('/sort')
def sort_patients(sort_by:str= Query(...,description='Sort on the basis of hieght,weight or bmi'),order:str=Query('asc',description='sort in asc or desc order')):
    valid_fields=['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail='Invalid field select from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order select between asc and desc')
    data=load_data()
    sort_order=True if order=='desc' else False
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorted_data


@app.post("/create")
def create_patient(patient:Patient):

    data=load_data()


    if patient.id in data:
        raise HTTPException(status_code=400,detail='Patient already exists')
    
    data[patient.id]=patient.model_dump(exclude=['id'])
    save_data(data)
    return JSONResponse(status_code=201,content={'message':'patient created successfully'})

@app.put('/edit/{patient_id}')
def update_patient(patient_id:str,patient_update:PatientUpdate):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail='Patient not found')
    existing_patient_info = data[patient_id]
    updated_patient_info=patient_update.model_dump(exclude_unset=True)
    for key , value in updated_patient_info.items():
        existing_patient_info[key]=value
    existing_patient_info['id']=patient_id
    patient_pydandic_obj=Patient(**existing_patient_info)
    existing_patient_info=patient_pydandic_obj.model_dump(exclude='id',context={'computed':True})
    data[patient_id]=existing_patient_info
    save_data(data)
    return JSONResponse(status_code=200,content={'message':'patient updated'})
@app.delete('/delete/{patient_id}')
def delete_patient(patient_id:str):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail='Patient not found')
    del data[patient_id]
    save_data(data)
    return JSONResponse(status_code=200,content={'message':'Patient deleted'})