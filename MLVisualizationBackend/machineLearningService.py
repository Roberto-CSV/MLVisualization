import numpy
import pandas as pd
from constants.machineLearningModelsConstant import AlgorithmsTypesConstant, MachineLearningModelsName, MachineLearningModelsConstant
from models.machineLearningModel import MachineLearningModel
from models.analysisResultModel import AnalysisResultModel
from dto.getAnalysis import GetAnalysisDTO
from models.predictResultModel import PredictResultModel
from utils.pandasUtil import PandasUtil
import joblib
from sklearn.metrics import classification_report, confusion_matrix, mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from fastapi import FastAPI, File, HTTPException, UploadFile


class ResultTypes:
    TRAIN = 'train'
    PREDICT = 'predict'

class MachineLearningService:
    def __init__(
        self,
        document_data_source: str,
        document_data_type: str,
        trained_models_source: str
    ):
        self.document_data_source: str = document_data_source
        self.document_data_type: str = document_data_type
        self.trained_models_source: str = trained_models_source
        self.trained_models_file_extension: str = 'joblib'
        self.data_frame: pd.DataFrame = PandasUtil.read_file(self.document_data_type, self.document_data_source)
        self.columns_names: list[str] = self.data_frame.columns.to_list()

    def __get_columns_nulls_quantity__(self, data_frame: pd.DataFrame) -> dict:
        return PandasUtil.get_columns_nulls_quantity(data_frame=data_frame)

    def __get_columns_unique_values__(self, data_frame: pd.DataFrame) -> dict:
        return PandasUtil.get_columns_unique_values(data_frame=data_frame)
    
    def __get_columns_types__(self, data_frame: pd.DataFrame) -> dict:
        return PandasUtil.get_columns_types(data_frame)

    def __clean_data__(self, data_frame: pd.DataFrame) -> pd.DataFrame:
        return data_frame.copy(deep=True).dropna()

    def __get_transformation_equivalence__(self, data_frame: pd.DataFrame) -> dict:
        cleaned_data: pd.DataFrame = self.__clean_data__(data_frame)
        columns_types: dict = self.__get_columns_types__(cleaned_data)
        columns_unique_values: dict = self.__get_columns_unique_values__(cleaned_data)
        transformation_equivalence: dict = {}
        for key in columns_types.keys():
            dtype: str = columns_types.get(key)
            if(dtype.__eq__('object')):
                unique_values: list[str] = columns_unique_values.get(key)
                transformed_values: dict = {}
                for index in range(len(unique_values)):
                    unique_value: str = unique_values[index]
                    transformed_values[unique_value] = index
                transformation_equivalence[key] = transformed_values
        return transformation_equivalence
    
    def __transform_data__(self, data_frame: pd.DataFrame):
        transformed_data: pd.DataFrame = self.__clean_data__(data_frame)
        transformation_equivalence = self.__get_transformation_equivalence__(transformed_data)
        for column_key in transformation_equivalence.keys():
            column_transformation_equivalence: dict = transformation_equivalence.get(column_key)
            transformed_data[column_key] = transformed_data[column_key].replace(column_transformation_equivalence)
        return transformed_data

    def __get_stadistic_data__(self, data_frame: pd.DataFrame):
        return data_frame.describe()

    def analyse_data(self, get_analysis_dto: GetAnalysisDTO) -> AnalysisResultModel:
        columns_types: dict = self.__get_columns_types__(self.data_frame)
        columns_nulls_quantity: dict = self.__get_columns_nulls_quantity__(self.data_frame)
        cleaned_data: pd.DataFrame = self.__clean_data__(self.data_frame)
        transformation_equivalence: dict = self.__get_transformation_equivalence__(self.data_frame)
        transformed_data: pd.DataFrame = self.__transform_data__(self.data_frame)
        # After transform data
        columns_unique_values: dict = self.__get_columns_unique_values__(self.data_frame)
        stadistic_data = self.__get_stadistic_data__(cleaned_data)
        analysis_result_model: AnalysisResultModel = AnalysisResultModel(
            original_data=None,
            null_data=None,
            unique_data=None,
            data_types=None,
            cleaned_data=None,
            transformed_data=None,
            transformation_equivalence=None,
            stadistic_data=None
        )

        if(get_analysis_dto.original_data):
            analysis_result_model.original_data = self.data_frame.to_dict(orient='records')
        if(get_analysis_dto.null_data):
            analysis_result_model.null_data = columns_nulls_quantity
        if(get_analysis_dto.unique_data):
            analysis_result_model.unique_data = columns_unique_values
        if(get_analysis_dto.data_types):
            analysis_result_model.data_types = columns_types
        if(get_analysis_dto.cleaned_data):
            analysis_result_model.cleaned_data = cleaned_data.to_dict(orient='records')
        if(get_analysis_dto.transformed_data):
            analysis_result_model.transformed_data = transformed_data.to_dict(orient='records')
        if(get_analysis_dto.transformation_equivalence):
            analysis_result_model.transformation_equivalence = transformation_equivalence
        if(get_analysis_dto.stadistic_data):
            analysis_result_model.stadistic_data = stadistic_data.to_dict()
        return analysis_result_model

    def __train_predict_model__(
            self, 
            model: dict, 
            result_type: str,
            x_train: pd.DataFrame = None,
            y_train: pd.Series = None,
            model_name: str = None,
            data_to_predict: pd.DataFrame = None
        ):
        result = None
        model_type: str = model.get('type')
        trained_model_source: str = f"{self.trained_models_source}/{model_type}/{model_name}_{model_type}.{self.trained_models_file_extension}"
        if(result_type.__eq__(ResultTypes.TRAIN)):
            machineLearningModel = model.get('algorithm')
            machineLearningModel.fit(x_train, y_train)
            joblib.dump(machineLearningModel, trained_model_source)
        elif(result_type.__eq__(ResultTypes.PREDICT)):
            machineLearningModel = joblib.load(trained_model_source)
            result = machineLearningModel.predict(data_to_predict)
            # print(data_to_predict)
        return result

    def __get_regression_model__(
            self, 
            model: MachineLearningModel, 
            result_type: str,
            x_train: pd.DataFrame = None,
            y_train: pd.Series = None,
            data_to_predict: pd.DataFrame = None
        ):
        result = None
        if(self.__is_model_equal__(MachineLearningModelsConstant.REGRESSION.get(MachineLearningModelsName.LINEAR_LASSO), model)):
            model_name = MachineLearningModelsName.LINEAR_LASSO
            machineLearningModel = MachineLearningModelsConstant.REGRESSION.get(model_name)
            result = self.__train_predict_model__(machineLearningModel, result_type, x_train, y_train, model_name, data_to_predict)
        elif(self.__is_model_equal__(MachineLearningModelsConstant.REGRESSION.get(MachineLearningModelsName.GRADIENT_BOOSTING), model)):
            model_name = MachineLearningModelsName.GRADIENT_BOOSTING
            machineLearningModel = MachineLearningModelsConstant.REGRESSION.get(model_name)
            result = self.__train_predict_model__(machineLearningModel, result_type, x_train, y_train, model_name, data_to_predict)
        elif(self.__is_model_equal__(MachineLearningModelsConstant.REGRESSION.get(MachineLearningModelsName.LINEAR_RIDGE), model)):
            model_name = MachineLearningModelsName.LINEAR_RIDGE
            machineLearningModel = MachineLearningModelsConstant.REGRESSION.get(model_name)
            result = self.__train_predict_model__(machineLearningModel, result_type, x_train, y_train, model_name, data_to_predict)
        elif(self.__is_model_equal__(MachineLearningModelsConstant.REGRESSION.get(MachineLearningModelsName.SUPPORT_VECTOR_MACHINES), model)):
            model_name = MachineLearningModelsName.SUPPORT_VECTOR_MACHINES
            machineLearningModel = MachineLearningModelsConstant.REGRESSION.get(model_name)
            result = self.__train_predict_model__(machineLearningModel, result_type, x_train, y_train, model_name, data_to_predict)
        elif(self.__is_model_equal__(MachineLearningModelsConstant.REGRESSION.get(MachineLearningModelsName.DECISION_TREES), model)):
            model_name = MachineLearningModelsName.DECISION_TREES
            machineLearningModel = MachineLearningModelsConstant.REGRESSION.get(model_name)
            result = self.__train_predict_model__(machineLearningModel, result_type, x_train, y_train, model_name, data_to_predict)
        elif(self.__is_model_equal__(MachineLearningModelsConstant.REGRESSION.get(MachineLearningModelsName.RANDOM_FOREST), model)):
            model_name = MachineLearningModelsName.RANDOM_FOREST
            machineLearningModel = MachineLearningModelsConstant.REGRESSION.get(model_name)
            result = self.__train_predict_model__(machineLearningModel, result_type, x_train, y_train, model_name, data_to_predict)
        elif(self.__is_model_equal__(MachineLearningModelsConstant.REGRESSION.get(MachineLearningModelsName.K_NEAREST_NEIGHBORRS), model)):
            model_name = MachineLearningModelsName.K_NEAREST_NEIGHBORRS
            machineLearningModel = MachineLearningModelsConstant.REGRESSION.get(model_name)
            result = self.__train_predict_model__(machineLearningModel, result_type, x_train, y_train, model_name, data_to_predict)
        return result
    
    def __get_classification_model__(
            self, 
            model: MachineLearningModel, 
            result_type: str,
            x_train: pd.DataFrame = None,
            y_train: pd.Series = None,
            data_to_predict: pd.DataFrame = None
        ):
        result = None
        if(self.__is_model_equal__(MachineLearningModelsConstant.CLASSIFICATION.get(MachineLearningModelsName.LINEAR_MULTINOMIAL_LOGISTIC_REGRESSION), model)):
            model_name = MachineLearningModelsName.LINEAR_MULTINOMIAL_LOGISTIC_REGRESSION
            machineLearningModel = MachineLearningModelsConstant.CLASSIFICATION.get(MachineLearningModelsName.LINEAR_MULTINOMIAL_LOGISTIC_REGRESSION)
            result = self.__train_predict_model__(machineLearningModel, result_type, x_train, y_train, model_name, data_to_predict)
        elif(self.__is_model_equal__(MachineLearningModelsConstant.CLASSIFICATION.get(MachineLearningModelsName.GUSSIAN_NAIVE_BAYES), model)):
            model_name = MachineLearningModelsName.GUSSIAN_NAIVE_BAYES
            machineLearningModel = MachineLearningModelsConstant.CLASSIFICATION.get(model_name)
            result = self.__train_predict_model__(machineLearningModel, result_type, x_train, y_train, model_name, data_to_predict)
        elif(self.__is_model_equal__(MachineLearningModelsConstant.CLASSIFICATION.get(MachineLearningModelsName.LINEAR_RIDGE), model)):
            model_name = MachineLearningModelsName.LINEAR_RIDGE
            machineLearningModel = MachineLearningModelsConstant.CLASSIFICATION.get(model_name)
            result = self.__train_predict_model__(machineLearningModel, result_type, x_train, y_train, model_name, data_to_predict)
        elif(self.__is_model_equal__(MachineLearningModelsConstant.CLASSIFICATION.get(MachineLearningModelsName.SUPPORT_VECTOR_MACHINES), model)):
            model_name = MachineLearningModelsName.SUPPORT_VECTOR_MACHINES
            machineLearningModel = MachineLearningModelsConstant.CLASSIFICATION.get(model_name)
            result = self.__train_predict_model__(machineLearningModel, result_type, x_train, y_train, model_name, data_to_predict)
        elif(self.__is_model_equal__(MachineLearningModelsConstant.CLASSIFICATION.get(MachineLearningModelsName.DECISION_TREES), model)):
            model_name = MachineLearningModelsName.DECISION_TREES
            machineLearningModel = MachineLearningModelsConstant.CLASSIFICATION.get(model_name)
            result = self.__train_predict_model__(machineLearningModel, result_type, x_train, y_train, model_name, data_to_predict)
        elif(self.__is_model_equal__(MachineLearningModelsConstant.CLASSIFICATION.get(MachineLearningModelsName.RANDOM_FOREST), model)):
            model_name = MachineLearningModelsName.RANDOM_FOREST
            machineLearningModel = MachineLearningModelsConstant.CLASSIFICATION.get(model_name)
            result = self.__train_predict_model__(machineLearningModel, result_type, x_train, y_train, model_name, data_to_predict)
        elif(self.__is_model_equal__(MachineLearningModelsConstant.CLASSIFICATION.get(MachineLearningModelsName.K_NEAREST_NEIGHBORRS), model)):
            model_name = MachineLearningModelsName.K_NEAREST_NEIGHBORRS
            machineLearningModel = MachineLearningModelsConstant.CLASSIFICATION.get(model_name)
            result = self.__train_predict_model__(machineLearningModel, result_type, x_train, y_train, model_name, data_to_predict)
        return result

    def train_model(self, model: MachineLearningModel) -> None:
        transformed_data: pd.DataFrame = self.__transform_data__(self.data_frame)
        x_train: pd.DataFrame = transformed_data.drop(['LeaveOrNot'], axis=1)
        y_train: pd.Series = transformed_data['LeaveOrNot']
        if(model.type.__eq__(AlgorithmsTypesConstant.REGRESSION)):
            self.__get_regression_model__(model=model, result_type=ResultTypes.TRAIN, x_train=x_train, y_train=y_train)
        elif(model.type.__eq__(AlgorithmsTypesConstant.CLASSIFICATION)):
            self.__get_classification_model__(model=model, result_type=ResultTypes.TRAIN, x_train=x_train, y_train=y_train)
        
    async def model_predict(self, model: MachineLearningModel, file: UploadFile = None) -> PredictResultModel:
        classification_report_var = None
        confusion_matrix_var = None
        prediction_data: numpy.ndarray = None
        if(file == None):
            data: pd.DataFrame = PandasUtil.read_file(self.document_data_type, './data/EmployeeTest.csv')
            data: pd.DataFrame = self.__transform_data__(data)
            X = data.drop(['LeaveOrNot'], axis=1)
            y = data['LeaveOrNot']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        else:
            try:
                # Guardar el archivo en el servidor (opcional)
                with open(file.filename, "wb") as file_object:
                    file_object.write(file.file.read())

                # Leer el archivo con Pandas
                df = pd.read_csv(file.filename)  # Cambia el método según el tipo de archivo que estás subiendo

                # Puedes realizar operaciones con el DataFrame df según tus necesidades

                # Devolver algunos datos procesados (esto es solo un ejemplo)
                X_test = self.__transform_data__(df)

            except Exception as e:
                # Manejar errores si ocurren durante la lectura del archivo
                raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {str(e)}")
            
        if(model.type.__eq__(AlgorithmsTypesConstant.CLASSIFICATION)):
            prediction_data = self.__get_classification_model__(model=model, result_type=ResultTypes.PREDICT, data_to_predict=X_test)
            X_test["LeaveOrNot"] = prediction_data.tolist()
            X_test = X_test.to_dict(orient="records")
            if(file == None):
                true_prediction: list = y_test.values
                classification_report_var = classification_report(true_prediction, prediction_data, zero_division=1, output_dict=True)
                confusion_matrix_var = confusion_matrix(true_prediction, prediction_data).tolist()
                X_test = None
        predictionResult: PredictResultModel = PredictResultModel(
            classification_report=classification_report_var,
            confusion_matrix=confusion_matrix_var,
            prediction_data=X_test
        )
        return predictionResult

    def __is_model_equal__(self, model: dict, model_to_compare: MachineLearningModel) -> bool:
        if(model.get('name').__eq__(model_to_compare.name) and model.get('type').__eq__(model_to_compare.type)):
            return True
        return False


    def unionFiles(self):
        data: pd.DataFrame = PandasUtil.read_file(self.document_data_type, './data/Employee.csv')
        X = data.drop(['LeaveOrNot'], axis=1)
        y = data['LeaveOrNot']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        train_concat: pd.DataFrame = pd.concat([X_train, y_train], axis=1)
        test_concat: pd.DataFrame = pd.concat([X_test, y_test], axis=1)
        train_concat.to_csv('./data/EmployeeTrain.csv', index=False)
        test_concat.to_csv('./data/EmployeeTest.csv', index=False)
        print(test_concat)
        return
    