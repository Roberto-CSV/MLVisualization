from machineLearningService import MachineLearningService
from dto.getAnalysis import GetAnalysisDTO

machineLearningService: MachineLearningService = MachineLearningService('./data/Train.csv', 'csv')

getAnalysisDTO = GetAnalysisDTO(
  original_data=True,
  null_data=True,
  unique_data=True,
  data_types=True,
  cleaned_data=True,
  transformed_data=True,
  transformation_equivalence=True,
  stadistic_data=True
)

machineLearningService.test(getAnalysisDTO)