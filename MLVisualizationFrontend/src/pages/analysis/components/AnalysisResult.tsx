import { AnalysisOptions } from "../../../core/const/AnalysisOption"
import { DataTable } from '../../../shared/components/DataTable';

export const AnalysisResult = () => {
  const analysisOptionsEntries = Object.entries(AnalysisOptions);

  return (
    <div className="row">
      <section className="col-lg-8 col-sm-12">
        <article id="data-analysis-results" className="mb-5">
          <h3 className="py-1">Resultados del análisis</h3>
          <p className="py-2">
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quidem cupiditate voluptatem veritatis
            praesentium numquam. Obcaecati aperiam vero maiores sapiente eos eveniet beatae voluptates soluta
            laudantium, assumenda facilis debitis sit minus.
          </p>
        </article>
        {
          analysisOptionsEntries.map((analysisOptionEntry, index) => {
            return (
              <article
                key={analysisOptionEntry[0]}
                id={analysisOptionEntry[0]}
                className="mb-5"
              >
                <h4 className="py-1">{(index + 1) + '. ' + analysisOptionEntry[1]?.name}</h4>
                <p className="py-2">{analysisOptionEntry[1]?.description}</p>
                <div>
                  <DataTable></DataTable>
                </div>
              </article>
            )
          })
        }
      </section>
      <section className="col-4 d-none d-lg-block">
        <div className="list-group sticky-top p-5">
          <h5 className="p-3 border-bottom">En esta página</h5>
          <a
            href="#data-analysis-results"
            className="list-group-item list-group-item-action border-0"
          >
            Resultados del análisis
          </a>
          {
            analysisOptionsEntries.map((analysisOptionEntry, index) => {
              return (
                <a
                  key={'reference-' + analysisOptionEntry[0]}
                  href={'#' + analysisOptionEntry[0]}
                  className="list-group-item list-group-item-action border-0"
                >
                  {(index + 1) + '. ' + analysisOptionEntry[1]?.name}
                </a>
              )
            })
          }
        </div>
      </section>
    </div>
  )
}
