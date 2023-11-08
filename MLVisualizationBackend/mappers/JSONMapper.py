import json
from models.analysisResultModel import AnalysisResultCustomerModel


class JSONMapper:

    def to_analysis_result_customer(json_data: dict) -> AnalysisResultCustomerModel | None:
        analysis_result_types: AnalysisResultCustomerModel = None
        try:
            analysis_result_types = AnalysisResultCustomerModel(
                ID=json_data.get("ID"),
                Gender=json_data.get("Gender"),
                Ever_Married=json_data.get("Ever_Married"),
                Age=json_data.get("Age"),
                Graduated=json_data.get("Graduated"),
                Profession=json_data.get("Profession"),
                Work_Experience=json_data.get("Work_Experience"),
                Spending_Score=json_data.get("Spending_Score"),
                Family_Size=json_data.get("Family_Size"),
                Var_1=json_data.get("Var_1"),
                Segmentation=json_data.get("Segmentation"),
            )
        except Exception:
            print("to_analysis_result_customer exception")
        return analysis_result_types
