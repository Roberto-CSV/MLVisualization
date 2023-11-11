from pydantic import BaseModel

class CustomerModel(BaseModel):
    ID: float | None
    Gender: str | None
    Ever_Married: str | None
    Age: float | None
    Graduated: str | None
    Profession: str | None
    Work_Experience: float | None
    Spending_Score: str | None
    Family_Size: float | None
    Var_1: str | None
    Segmentation: str | None