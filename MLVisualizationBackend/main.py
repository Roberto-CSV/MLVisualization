from constants.machineLearningModelsConstant import AlgorithmsTypesConstant
from models.machineLearningModel import MachineLearningModel
from machineLearningService import MachineLearningService
from dto.getAnalysis import GetAnalysisDTO

machineLearningService: MachineLearningService = MachineLearningService('./data/Train.csv', 'csv', './trained_models')

get_analysis_dto = GetAnalysisDTO(
  original_data=False,
  null_data=True,
  unique_data=False,
  data_types=True,
  cleaned_data=False,
  transformed_data=False,
  transformation_equivalence=True,
  stadistic_data=True
)

model_regression = MachineLearningModel(name='Máquinas de soporte vectorial', type=AlgorithmsTypesConstant.REGRESSION)
model_classification = MachineLearningModel(name='Máquinas de soporte vectorial', type=AlgorithmsTypesConstant.CLASSIFICATION)

# print(machineLearningService.analyse_data(get_analysis_dto))

# USE MACHINE LEARNING MODELS 

machineLearningService.train_model(model_regression)
machineLearningService.train_model(model_classification)

machineLearningService.model_predict(model_regression)
machineLearningService.model_predict(model_classification)