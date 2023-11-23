import { useState } from "react";
import {
  ALGORITHMS_TYPES,
  MACHINE_LEARNING_MODELS,
} from "../../core/const/MachineLearningModels";
import { MachineLearningResult } from "./components/MachineLearningResult";
import { MachineLearningService } from "../../core/services/machine-learning.service";

const machineLearningService: MachineLearningService =
  new MachineLearningService();

export const MachineLearning = () => {
  const machineLearningModelsEntries = Object.entries(MACHINE_LEARNING_MODELS);
  const [file, setFile] = useState(null);
  const [submitError, setSubmitError] = useState("");
  const [modelResult, setModelResult] = useState({});

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile);
  };
  const onSubmit = (e: any) => {
    e.preventDefault();
    if (file?.name.split(".")[1].toLowerCase() !== "csv") {
      setSubmitError("Archivo no válido, debe ser un csv.");
    } else {
      setSubmitError("");
    }
    machineLearningService.getPrediction(null, file).then((response) => {
      setModelResult(response);
      console.log(response);
    });
  };

  return (
    <div className="container-fluid h-100">
      <main className="d-flex flex-wrap align-items-center h-100">
        <section className="row h-100">
          <div className="row align-self-end">
            <h2 className="py-1">Modelos de aprendizaje automático</h2>
            <p className="py-4">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea
              provident vitae voluptatum optio, libero cum expedita, non
              mollitia animi a quas doloremque eos dicta nisi amet nam odio
              deleniti facilis. Quisquam, eos expedita dicta incidunt nobis
              fugiat dolorem. In cumque, quos quo officia, eum beatae
              repellendus alias fugiat laborum iste possimus fuga, voluptas
              delectus quidem dolor quam assumenda nulla corrupti. Provident ad
              reiciendis, culpa, dolor nam impedit quisquam fugit ab possimus
              nesciunt velit quidem laboriosam. Maxime voluptate, earum illum id
              ut tempore repellendus provident, accusantium distinctio illo
              doloremque excepturi nam.
            </p>
          </div>
          <form className="row align-self-start" onSubmit={onSubmit}>
            <p className="fw-bold">Prueba el modelo de Bosques Aleatorios:</p>
            <div className="col-lg-10 col-sm-12 py-2">
              <input
                onChange={handleFileChange}
                type="file"
                className="form-control"
                id="inputGroupFile02"
              />
            </div>
            <div className="col-lg-2 col-sm-12 py-2">
              <button
                type="submit"
                disabled={!file}
                className="btn btn-dark w-100"
              >
                Clasificar
              </button>
            </div>
            {submitError ? (
              <p className="text-center py-2 text-danger">
                <small>{submitError}</small>
              </p>
            ) : (
              <span></span>
            )}
          </form>
          {modelResult.prediction_data ? (
            <div className="table-responsive py-5">
              <table className="table">
                <thead>
                  <tr className="p-2">
                    <th className="p-2">Age</th>
                    <th className="p-2">City</th>
                    <th className="p-2">Education</th>
                    <th className="p-2">EverBenched</th>
                    <th className="p-2">ExperienceInCurrentDomain</th>
                    <th className="p-2">Gender</th>
                    <th className="p-2">JoiningYear</th>
                    <th className="p-2">PaymentTier</th>
                    <th className="p-2">LeaveOrNot</th>
                  </tr>
                </thead>
                <tbody>
                  {
                    modelResult.prediction_data.map((row, index) => {
                      return (
                        <tr key={index}>
                          <td className="p-3">{row.Age}</td>
                          <td className="p-3">{row.City}</td>
                          <td className="p-3">{row.Education}</td>
                          <td className="p-3">{row.EverBenched}</td>
                          <td className="p-3">{row.ExperienceInCurrentDomain}</td>
                          <td className="p-3">{row.Gender}</td>
                          <td className="p-3">{row.JoiningYear}</td>
                          <td className="p-3">{row.PaymentTier}</td>
                          <td className="p-3">{row.LeaveOrNot}</td>
                        </tr>
                      );
                    })
                  }
                </tbody>
              </table>
            </div>
          ) : (
            <span></span>
          )}
        </section>
        <section className="row h-100 py-5">
          <MachineLearningResult></MachineLearningResult>
        </section>
      </main>
    </div>
  );
};
