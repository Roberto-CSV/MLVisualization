from pydantic import BaseModel
from models.customerModel import CustomerModel


class DataResultModel(BaseModel):
  column_names: list[str]
  data: list[CustomerModel | object]



class AnalysisResultModel(BaseModel):
  original_data: object | None
  null_data: object | None
  unique_data: object | None
  data_types: object | None
  cleaned_data: object | None
  transformed_data: object | None
  transformation_equivalence: object | None
  stadistic_data: object | None