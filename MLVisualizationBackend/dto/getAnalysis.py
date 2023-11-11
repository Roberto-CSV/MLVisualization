from pydantic import BaseModel

class GetAnalysisDTO(BaseModel):
  original_data: bool
  null_data: bool
  unique_data: bool
  data_types: bool
  cleaned_data: bool
  transformed_data: bool
  transformation_equivalence: bool
  stadistic_data: bool