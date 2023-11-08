from pydantic import BaseModel


class FillTechniqueModel(BaseModel):
    text: str
    value: str
