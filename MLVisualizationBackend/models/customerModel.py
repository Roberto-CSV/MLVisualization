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

class ConvertedCustomerModel(BaseModel):
    ID: float | None
    Gender: float | None
    Ever_Married: float | None
    Age: float | None
    Graduated: float | None
    Profession: float | None
    Work_Experience: float | None
    Spending_Score: float | None
    Family_Size: float | None
    Var_1: float | None
    Segmentation: float | None