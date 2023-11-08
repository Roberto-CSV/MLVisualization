from pydantic import BaseModel
from models.customerModel import CustomerModel, ConvertedCustomerModel
from typing import Any


class AnalysisResultCustomerModel(BaseModel):
    ID: Any
    Gender: Any
    Ever_Married: Any
    Age: Any
    Graduated: Any
    Profession: Any
    Work_Experience: Any
    Spending_Score: Any
    Family_Size: Any
    Var_1: Any
    Segmentation: Any


class DataAnalysisResultModel(BaseModel):
    steps: AnalysisResultCustomerModel | None
    data: list[CustomerModel | ConvertedCustomerModel]


class AnalysisResultModel(BaseModel):
    original_data: Any
    columns_names: list[str]
    columns_types: AnalysisResultCustomerModel | None
    columns_nulls: AnalysisResultCustomerModel | None
    columns_uniques: AnalysisResultCustomerModel | None
    cleaned_data: DataAnalysisResultModel | None
    converted_data: DataAnalysisResultModel | None
