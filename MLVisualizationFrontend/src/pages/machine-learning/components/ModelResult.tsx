import { useState, useEffect } from "react";
import {
  ConfusionMatrix,
  ConfusionMatrixInterface,
} from "../../../shared/components/ConfusionMatrix";
import { DataTable } from "../../../shared/components/DataTable";
import { MachineLearningService } from "../../../core/services/machine-learning.service";

const machineLearningService: MachineLearningService =
  new MachineLearningService();

export const ModelResult = ({ modelName }) => {
  const [model, setModel] = useState({});
  const [initialized, setInitialized] = useState(false);

  useEffect(() => {
    machineLearningService
      .getPrediction({ name: modelName, type: "Clasificación" })
      .then((response) => {
        setModel(response);
        setInitialized(true);
      });
  }, []);

  return (
    <div className="card">
      <div className="card-body">
        <h5 className="py-1">{modelName}</h5>
        {initialized ? (
          <>
            <p>
              Some quick example text to build on the card title and make up the
              bulk of the card's content.
            </p>
            <article className="table-responsive py-4">
              <h6 className="py-1">Informe de clasificación</h6>
              <table className="table">
                <thead>
                  <tr>
                    <th scope="col">#</th>
                    <th scope="col">F1 Score</th>
                    <th scope="col">Precision</th>
                    <th scope="col">Recall</th>
                    <th scope="col">Support</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <th scope="row">0</th>
                    <td>{model.classification_report["0"]["f1-score"]}</td>
                    <td>{model.classification_report["0"]["precision"]}</td>
                    <td>{model.classification_report["0"]["recall"]}</td>
                    <td>{model.classification_report["0"]["support"]}</td>
                  </tr>
                  <tr>
                    <th scope="row">1</th>
                    <td>{model.classification_report["1"]["f1-score"]}</td>
                    <td>{model.classification_report["1"]["precision"]}</td>
                    <td>{model.classification_report["1"]["recall"]}</td>
                    <td>{model.classification_report["1"]["support"]}</td>
                  </tr>
                  <tr>
                    <th scope="row">Accuracy</th>
                    <td colspan="4" className="text-center">
                      {model.classification_report["accuracy"]}
                    </td>
                  </tr>
                  <tr>
                    <th scope="row">Macro AVG</th>
                    <td>
                      {model.classification_report["macro avg"]["f1-score"]}
                    </td>
                    <td>
                      {model.classification_report["macro avg"]["precision"]}
                    </td>
                    <td>
                      {model.classification_report["macro avg"]["recall"]}
                    </td>
                    <td>
                      {model.classification_report["macro avg"]["support"]}
                    </td>
                  </tr>
                  <tr>
                    <th scope="row">Weighted AVG</th>
                    <td>
                      {model.classification_report["weighted avg"]["f1-score"]}
                    </td>
                    <td>
                      {model.classification_report["weighted avg"]["precision"]}
                    </td>
                    <td>
                      {model.classification_report["weighted avg"]["recall"]}
                    </td>
                    <td>
                      {model.classification_report["weighted avg"]["support"]}
                    </td>
                  </tr>
                </tbody>
              </table>
            </article>
            <article className="py-4">
              <h6 className="py-1">Matriz de confusión</h6>
              <ConfusionMatrix data={model.confusion_matrix}></ConfusionMatrix>
            </article>
          </>
        ) : (
          <p>No hay nada aun</p>
        )}
      </div>
    </div>
  );
};
