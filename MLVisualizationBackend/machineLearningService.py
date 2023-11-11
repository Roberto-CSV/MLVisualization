import pandas as pd
from models.analysisResultModel import AnalysisResultModel
from dto.getAnalysis import GetAnalysisDTO
from utils.pandasUtil import PandasUtil

class MachineLearningService:
    def __init__(
        self,
        document_data_source: str,
        document_data_type: str
    ):
        self.document_data_source: str = document_data_source
        self.document_data_type: str = document_data_type
        self.data_frame: pd.DataFrame = PandasUtil.read_file(self.document_data_type, self.document_data_source)
        self.columns_names: list[str] = self.data_frame.columns.to_list()

    def __get_columns_nulls_quantity(self, data_frame: pd.DataFrame) -> dict:
        return PandasUtil.get_columns_nulls_quantity(data_frame=data_frame)

    def __get_columns_unique_values(self, data_frame: pd.DataFrame) -> dict:
        return PandasUtil.get_columns_unique_values(data_frame=data_frame)
    
    def __get_columns_types(self, data_frame: pd.DataFrame) -> dict:
        return PandasUtil.get_columns_types(data_frame)

    def __get_clean_data(self, data_frame: pd.DataFrame) -> pd.DataFrame:
        return data_frame.copy(deep=True).dropna()

    def __get_stadistic_data(self, data_frame: pd.DataFrame):
        return data_frame.describe()

    def test(self, getAnalysisDTO: GetAnalysisDTO):
        columns_types: dict = self.__get_columns_types(self.data_frame)
        columns_nulls_quantity: dict = self.__get_columns_nulls_quantity(self.data_frame)
        cleaned_data: pd.DataFrame = self.__get_clean_data(self.data_frame)
        # After transform data
        columns_unique_values: dict = self.__get_columns_unique_values(self.data_frame)
        stadistic_data = self.__get_stadistic_data(cleaned_data)
        analysisResultModel: AnalysisResultModel = AnalysisResultModel(
            original_data=None,
            null_data=None,
            unique_data=None,
            data_types=None,
            cleaned_data=None,
            transformed_data=None,
            transformation_equivalence=None,
            stadistic_data=None
        )

        if(getAnalysisDTO.original_data):
            analysisResultModel.original_data = self.data_frame
        if(getAnalysisDTO.null_data):
            analysisResultModel.null_data = columns_nulls_quantity
        if(getAnalysisDTO.unique_data):
            analysisResultModel.unique_data = columns_unique_values
        if(getAnalysisDTO.data_types):
            analysisResultModel.data_types = columns_types
        if(getAnalysisDTO.cleaned_data):
            analysisResultModel.cleaned_data = cleaned_data
        if(getAnalysisDTO.transformed_data):
            analysisResultModel.transformed_data = None
        if(getAnalysisDTO.transformation_equivalence):
            analysisResultModel.transformation_equivalence = None
        if(getAnalysisDTO.stadistic_data):
            analysisResultModel.stadistic_data = stadistic_data
        print(analysisResultModel)
        

