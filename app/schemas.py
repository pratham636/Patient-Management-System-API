from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
class Patient(BaseModel):
    id:Annotated[str,Field(...,descprition='Id of the patient',examples=['P001'])]
    name:Annotated[str,Field(...,description='Name of the patient')]
    city:Annotated[str,Field(...,description='City where the patient is living')]
    age:Annotated[int,Field(...,gt=0,lt=120,description='Age of the patient')]
    gender:Annotated[Literal['male','female','others'],Field(...,description='Gender of the patient')]
    height:Annotated[float,Field(...,gt=0,description='Height of the patient in meters')]
    weight:Annotated[float,Field(...,gt=0,description='Weight of the patient in kg')]

    @computed_field
    @property
    def bmi(self)->float:
        if not self.weight or not self.height:
            return 0
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18.5:
            return 'Underweig'
        # elif self.bmi<25:
        #     return 'Normal'
        elif self.bmi<30:
            return 'Normal'
        else:
            return 'Obese'

class PatientUpdate(BaseModel):
    name:Annotated[str,Field(default=None)]
    city:Annotated[str,Field(default=None)]
    age:Annotated[int,Field(default=None)]
    gender:Annotated[Literal['male','female','others'],Field(default=None)]
    height:Annotated[float,Field(default=None)]
    weight:Annotated[float,Field(default=None)]
