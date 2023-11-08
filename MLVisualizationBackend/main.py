from machineLearningService import MachineLearningService

machineLearningService: MachineLearningService = MachineLearningService(
    './data/Train.csv', 'csv')

machineLearningService.run()