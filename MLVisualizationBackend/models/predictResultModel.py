from pydantic import BaseModel


class PredictResultModel(BaseModel):
  classification_report: object | None
  confusion_matrix: object | None
  prediction_data: object | None

