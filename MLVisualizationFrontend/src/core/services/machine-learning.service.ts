import {
  AnalysisResultModel,
  MachineLearningModel,
  PredictionResultModel,
} from "./models/machine-learning.model";
export class MachineLearningService {
  // Define la URL de la API a la que deseas hacer la solicitud
  API_URL: string = "http://127.0.0.1:8000";

  async getDataAnalysis(): Promise<AnalysisResultModel | undefined> {
    let dataAnalysis: AnalysisResultModel | undefined;
    // Realiza una solicitud GET utilizando fetch
    await fetch(this.API_URL)
      .then((response) => {
        // Verifica si la respuesta es exitosa (código de estado 200)
        if (response.ok) {
          // Parsea la respuesta como JSON
          return response.json();
        } else {
          // Si la respuesta no es exitosa, lanza un error
          throw new Error("Error en la solicitud");
        }
      })
      .then((data) => {
        // Procesa los datos de respuesta
        dataAnalysis = data;
      })
      .catch((error) => {
        // Maneja los errores de la solicitud
        console.error("Error:", error);
      });
    return dataAnalysis;
  }

  async getPrediction(
    model?: MachineLearningModel,
    file?
  ): Promise<PredictionResultModel | undefined> {
    let predictionResult: PredictionResultModel | undefined;
    let urlPredict: string = model ? "/predict" : "/predictFile";
    let formData = new FormData();
    if(file) formData.append("file", file)
    console.log(formData.get("file"))
    // Realiza una solicitud GET utilizando fetch
    await fetch(this.API_URL + urlPredict, {
      method: "POST",
      headers: model ? {
        "Content-Type": "application/json",
      } : undefined,
      body: model ? JSON.stringify(model) : formData,
    })
      .then((response) => {
        // Verifica si la respuesta es exitosa (código de estado 200)
        if (response.ok) {
          // Parsea la respuesta como JSON
          return response.json();
        } else {
          // Si la respuesta no es exitosa, lanza un error
          throw new Error("Error en la solicitud");
        }
      })
      .then((data) => {
        // Procesa los datos de respuesta
        predictionResult = data;
      })
      .catch((error) => {
        // Maneja los errores de la solicitud
        console.error("Error:", error);
      });
    return predictionResult;
  }
}
