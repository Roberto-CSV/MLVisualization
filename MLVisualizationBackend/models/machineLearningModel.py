from pydantic import BaseModel

class MachineLearningModel(BaseModel):
    name: str
    type: str