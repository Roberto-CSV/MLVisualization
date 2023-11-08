import pandas as pd
import json
from constants.machineLearningConstant import DocumentTypesConstant


class PandasUtil:

    @staticmethod
    def get_unique_values(data_frame: pd.DataFrame) -> dict:
        columns_names: list[str] = data_frame.columns.to_list()
        columns_uniques: dict = {}
        for column_name in columns_names:
            columns_uniques[column_name] = data_frame[column_name].unique(
            ).tolist()
        return columns_uniques

    @staticmethod
    def get_json(data_frame: pd.DataFrame) -> dict:
        json_string: str = data_frame.to_json(orient="records")
        data_frame_json: dict = json.loads(json_string)
        return data_frame_json

    @staticmethod
    def read_file(
        document_type: str,
        document_source: str
    ) -> pd.DataFrame | None:
        try:
            data_frame: pd.DataFrame = pd.DataFrame()
            if (document_type == DocumentTypesConstant.CSV):
                data_frame = pd.read_csv(document_source)
            elif (document_type == DocumentTypesConstant.EXCEL):
                data_frame = pd.read_excel(document_source)
            return data_frame
        except exception:
            print(exception)
