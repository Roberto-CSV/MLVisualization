from pydantic import BaseModel
from models.customerModel import CustomerModel


class DataResultModel(BaseModel):
  column_names: list[str]
  data: list[CustomerModel | object]



class AnalysisResultModel(BaseModel):
  original_data: list[dict] | None
  null_data: dict | None
  unique_data: dict | None
  data_types: dict | None
  cleaned_data: list[dict] | None
  transformed_data: list[dict] | None
  transformation_equivalence: dict | None
  stadistic_data: dict | None