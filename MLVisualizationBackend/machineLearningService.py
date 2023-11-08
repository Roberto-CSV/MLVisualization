import pandas as pd
import json
from constants.machineLearningConstant import DocumentTypesConstant
from mappers.JSONMapper import JSONMapper
from models.analysisResultModel import AnalysisResultModel, DataAnalysisResultModel, AnalysisResultCustomerModel
from utils.pandasUtil import PandasUtil
from constants.machineLearningConstant import FillTechniquesConstant


class MachineLearningService:
    def __init__(
        self,
        document_source: str,
        document_type: str
    ):
        self.document_source: str = document_source
        self.document_type: str = document_type
        self.data_frame: pd.DataFrame = PandasUtil.read_file(
            self.document_type, self.document_source)
        self.columns_names: list[str] = self.data_frame.columns.to_list()

    def __can_apply_cleaning_method(self, cleaning_method: str, column_type: str) -> bool:
        can_apply: bool = False
        if column_type == "object":
            if cleaning_method in [FillTechniquesConstant.NEXT.value, FillTechniquesConstant.PREVIOUS.value, FillTechniquesConstant.DROP.value]:
                can_apply = True
            else:
                can_apply = False
        else:
            can_apply = True
        return can_apply

    def __apply_cleaning_method(self, column_name: str, cleaning_method: str, data_frame: pd.DataFrame) -> pd.DataFrame:
        clean_data_frame: pd.DataFrame = data_frame.copy(deep=True)
        if cleaning_method == FillTechniquesConstant.MEAN.value:
            clean_data_frame[column_name].fillna(
                clean_data_frame[column_name].mean(), inplace=True)
        elif cleaning_method == FillTechniquesConstant.STD.value:
            clean_data_frame[column_name].fillna(
                clean_data_frame[column_name].std(), inplace=True)
        elif cleaning_method == FillTechniquesConstant.MIN.value:
            clean_data_frame[column_name].fillna(
                clean_data_frame[column_name].min(), inplace=True)
        elif cleaning_method == FillTechniquesConstant.PERCENTILE_25.value:
            clean_data_frame[column_name].fillna(
                clean_data_frame[column_name].quantile(0.25), inplace=True)
        elif cleaning_method == FillTechniquesConstant.PERCENTILE_50.value:
            clean_data_frame[column_name].fillna(
                clean_data_frame[column_name].median(), inplace=True)
        elif cleaning_method == FillTechniquesConstant.PERCENTILE_75.value:
            clean_data_frame[column_name].fillna(
                clean_data_frame[column_name].quantile(0.75), inplace=True)
        elif cleaning_method == FillTechniquesConstant.MAX.value:
            clean_data_frame[column_name].fillna(
                clean_data_frame[column_name].max(), inplace=True)
        elif cleaning_method == FillTechniquesConstant.PREVIOUS.value:
            clean_data_frame[column_name].fillna(
                clean_data_frame[column_name].bfill(), inplace=True)
        elif cleaning_method == FillTechniquesConstant.NEXT.value:
            clean_data_frame[column_name].fillna(
                clean_data_frame[column_name].ffill(), inplace=True)
        elif cleaning_method == FillTechniquesConstant.DROP.value:
            clean_data_frame[column_name].dropna(inplace=True)
        return clean_data_frame

    def __get_cleaning_method(self, column_name: str, techniques: AnalysisResultCustomerModel) -> str:
        cleaning_method: str = ""
        if column_name == "ID":
            cleaning_method = techniques.ID
        elif column_name == "Gender":
            cleaning_method = techniques.Gender
        elif column_name == "Ever_Married":
            cleaning_method = techniques.Ever_Married
        elif column_name == "Age":
            cleaning_method = techniques.Age
        elif column_name == "Graduated":
            cleaning_method = techniques.Graduated
        elif column_name == "Profession":
            cleaning_method = techniques.Profession
        elif column_name == "Work_Experience":
            cleaning_method = techniques.Work_Experience
        elif column_name == "Spending_Score":
            cleaning_method = techniques.Spending_Score
        elif column_name == "Family_Size":
            cleaning_method = techniques.Family_Size
        elif column_name == "Var_1":
            cleaning_method = techniques.Var_1
        elif column_name == "Segmentation":
            cleaning_method = techniques.Segmentation
        return cleaning_method

    def __clear_data(self, data_frame: pd.DataFrame, techniques: AnalysisResultCustomerModel) -> pd.DataFrame:
        clean_data_frame: pd.DataFrame = data_frame.copy(deep=True)
        for column_name in self.columns_names:
            cleaning_method: str = self.__get_cleaning_method(
                column_name, techniques)
            column_type: str = data_frame[column_name].dtype
            can_apply_cleaning_method: bool = self.__can_apply_cleaning_method(
                cleaning_method, column_type)
            if (can_apply_cleaning_method):
                clean_data_frame = self.__apply_cleaning_method(
                    column_name, cleaning_method, clean_data_frame)
        return clean_data_frame

    def __convert_uniques(self, columns_uniques: dict) -> dict:
        converted_columns_uniques: dict = {}
        for column_name in columns_uniques.keys():
            if type(columns_uniques.get(column_name)[0]) == type(""):
                iterator: int = 0
                converted_columns_uniques[column_name] = []
                for column_unique in columns_uniques.get(column_name):
                    converted_columns_uniques.get(column_name).append(iterator)
                    iterator += 1
            else:
                converted_columns_uniques[column_name] = columns_uniques.get(
                    column_name)
        return converted_columns_uniques

    def __convert_column(self, value: object, column_name: str, columns_uniques: dict, converted_columns_uniques: dict) -> object:
        converted_value: object = value
        iterator: int = 0
        for column_unique in columns_uniques.get(column_name):
            if column_unique == value:
                converted_value = converted_columns_uniques.get(column_name)[
                    iterator]
                break
            iterator += 1
        return converted_value

    def __convert_data(self, data_frame: pd.DataFrame) -> pd.DataFrame:
        converted_data_frame: pd.DataFrame = data_frame.copy(deep=True)
        columns_uniques: dict = PandasUtil.get_unique_values(
            data_frame.dropna())
        converted_columns_uniques: dict = self.__convert_uniques(data_frame)
        for column_name in converted_data_frame.columns:
            if (column_name != "ID"):
                converted_data_frame[column_name] = converted_data_frame[column_name].apply(
                    self.__convert_column, args=(column_name, columns_uniques, converted_columns_uniques))
        return converted_data_frame

    def __get_cleaning_method_text(self, cleaning_method: str):
        cleaning_method_text: str = ""
        if cleaning_method == FillTechniquesConstant.MEAN.value:
            cleaning_method_text = FillTechniquesConstant.MEAN.text
        elif cleaning_method == FillTechniquesConstant.STD.value:
            cleaning_method_text = FillTechniquesConstant.STD.text
        elif cleaning_method == FillTechniquesConstant.MIN.value:
            cleaning_method_text = FillTechniquesConstant.MIN.text
        elif cleaning_method == FillTechniquesConstant.PERCENTILE_25.value:
            cleaning_method_text = FillTechniquesConstant.PERCENTILE_25.text
        elif cleaning_method == FillTechniquesConstant.PERCENTILE_50.value:
            cleaning_method_text = FillTechniquesConstant.PERCENTILE_50.text
        elif cleaning_method == FillTechniquesConstant.PERCENTILE_75.value:
            cleaning_method_text = FillTechniquesConstant.PERCENTILE_75.text
        elif cleaning_method == FillTechniquesConstant.MAX.value:
            cleaning_method_text = FillTechniquesConstant.MAX.text
        elif cleaning_method == FillTechniquesConstant.PREVIOUS.value:
            cleaning_method_text = FillTechniquesConstant.PREVIOUS.text
        elif cleaning_method == FillTechniquesConstant.NEXT.value:
            cleaning_method_text = FillTechniquesConstant.NEXT.text
        elif cleaning_method == FillTechniquesConstant.DROP.value:
            cleaning_method_text = FillTechniquesConstant.DROP.text
        return cleaning_method_text

    def run(self) -> AnalysisResultModel:
        column_types: pd.DataFrame = self.data_frame.dtypes
        columns_nulls: pd.DataFrame = self.data_frame.isnull().sum()
        columns_uniques: dict = PandasUtil.get_unique_values(
            self.data_frame.dropna())
        columns_converted_uniques: dict = self.__convert_uniques(
            columns_uniques)

        # Request
        request: AnalysisResultCustomerModel = AnalysisResultCustomerModel(
            ID="mean",
            Gender="previous",
            Ever_Married="previous",
            Age="mean",
            Graduated="previous",
            Profession="previous",
            Work_Experience="mean",
            Spending_Score="previous",
            Family_Size="mean",
            Var_1="previous",
            Segmentation="previous"
        )

        # Mapper
        types: AnalysisResultCustomerModel = JSONMapper.to_analysis_result_customer(
            column_types.to_dict())
        nulls: AnalysisResultCustomerModel = JSONMapper.to_analysis_result_customer(
            columns_nulls.to_dict())
        uniques: AnalysisResultCustomerModel = JSONMapper.to_analysis_result_customer(
            columns_uniques)
        converted_uniques: AnalysisResultCustomerModel = JSONMapper.to_analysis_result_customer(
            columns_converted_uniques)
        # Others
        cleaned_data_steps: AnalysisResultCustomerModel = AnalysisResultCustomerModel(
            ID=self.__get_cleaning_method_text(request.ID),
            Gender=self.__get_cleaning_method_text(request.Gender),
            Ever_Married=self.__get_cleaning_method_text(request.Ever_Married),
            Age=self.__get_cleaning_method_text(request.Age),
            Graduated=self.__get_cleaning_method_text(request.Graduated),
            Profession=self.__get_cleaning_method_text(request.Profession),
            Work_Experience=self.__get_cleaning_method_text(request.Work_Experience),
            Spending_Score=self.__get_cleaning_method_text(request.Spending_Score),
            Family_Size=self.__get_cleaning_method_text(request.Family_Size),
            Var_1=self.__get_cleaning_method_text(request.Var_1),
            Segmentation=self.__get_cleaning_method_text(request.Segmentation)
        )
        cleaned_data: pd.DataFrame = self.__clear_data(
            self.data_frame, request)
        converted_data: pd.DataFrame = self.__convert_data(cleaned_data)
        print(types)
        return AnalysisResultModel(
            original_data=PandasUtil.get_json(self.data_frame),
            columns_names=self.data_frame.columns.to_list(),
            columns_types=None,
            columns_nulls=nulls,
            columns_uniques=uniques,
            # cleaned_data=None,
            cleaned_data=DataAnalysisResultModel(
                steps=cleaned_data_steps, data=cleaned_data.to_dict(orient="records")),
            # converted_data=None
            converted_data=DataAnalysisResultModel(
                steps=converted_uniques, data=converted_data.to_dict(orient="records")),
        )
