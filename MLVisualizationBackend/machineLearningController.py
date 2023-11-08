from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from machineLearningService import MachineLearningService
from models.customerModel import CustomerModel
from models.analysisResultModel import AnalysisResultModel

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

machineLearningService: MachineLearningService = MachineLearningService(
    './data/Train.csv', 'csv')


@app.get("/")
def test() -> AnalysisResultModel:
    return machineLearningService.run()
