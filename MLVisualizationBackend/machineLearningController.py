from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from constants.machineLearningModelsConstant import AlgorithmsTypesConstant
from dto.getAnalysis import GetAnalysisDTO
from machineLearningService import MachineLearningService
from models.analysisResultModel import AnalysisResultModel
from models.machineLearningModel import MachineLearningModel
from models.predictResultModel import PredictResultModel

app = FastAPI()
# Configurar las opciones de CORS
origins = ["http://localhost", "http://localhost:5173"]  # Lista de orígenes permitidos (origins)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Lista de orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Métodos HTTP permitidos (puedes personalizarlos)
    allow_headers=["*"],  # Cabeceras permitidas (puedes personalizarlas)
)

machineLearningService: MachineLearningService = MachineLearningService('./data/EmployeeTrain.csv', 'csv', './trained_models')
get_analysis_dto = GetAnalysisDTO(
  original_data=True,
  null_data=True,
  unique_data=True,
  data_types=False,
  cleaned_data=True,
  transformed_data=True,
  transformation_equivalence=True,
  stadistic_data=True
)

@app.post("/predict")
async def predict(model: MachineLearningModel) -> PredictResultModel:
    return await machineLearningService.model_predict(model=model)

@app.post("/predictFile")
async def predict_file(file: UploadFile) -> PredictResultModel:
    model_classification = MachineLearningModel(name='Bosques aleatorios', type=AlgorithmsTypesConstant.CLASSIFICATION)
    return await machineLearningService.model_predict(model=model_classification, file=file)

@app.get("/analyse")
def analyse() -> AnalysisResultModel:
    return machineLearningService.analyse_data(get_analysis_dto)
