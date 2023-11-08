import { ConfusionMatrix, ConfusionMatrixInterface } from '../../../shared/components/ConfusionMatrix';
import { DataTable } from "../../../shared/components/DataTable"

export const ModelResult = () => {
  const confusionMatrixData: ConfusionMatrixInterface = {
    truePositive: 10,
    falseNegative: 10,
    falsePositive: 10,
    trueNegative: 10,
  };

  return (
    <div className="card">
      <div className="card-body">
        <h5 className="py-1">Support Vector Machine</h5>
        {/* <h6 className="card-subtitle mb-2 text-body-secondary">Card subtitle</h6> */}
        <p>
          Some quick example text to build on the card title and make up the bulk of the card's content.
        </p>
        <article className="py-4">
          <h6 className="py-1">Informe de clasificación</h6>
          <DataTable></DataTable>
        </article>
        <article className="py-4">
          <h6 className="py-1">Matriz de confusión</h6>
          <ConfusionMatrix data={confusionMatrixData}></ConfusionMatrix>
        </article>
      </div>
    </div>
  )
}
