import { AnalysisOptions } from "../../core/const/AnalysisOption";
import { AnalysisResult } from "./components/AnalysisResult";

export const Analysis = () => {
  const analysisOptionsEntries = Object.entries(AnalysisOptions);

  const analyseData = (e: any) => {
    console.log(e);
  };
  const handleSelectClicked = (e: any) => {
    console.log(e);
    console.log(e.target_valueTracker.getValue())
  };

  return (
    <div className='container-fluid h-100'>
      <main className='d-flex flex-wrap align-items-center h-100'>
        <section className="row align-items-center h-100">
          <article className="col-lg-6 col-sm-12">
            <h2 className='py-1'>Segmentación de clientes</h2>
            <div className='py-4'>
              <p>
                <span className="fw-bold">Contexto: </span>Una empresa de automóviles tiene planes de ingresar
                a nuevos mercados con sus productos existentes (P1, P2, P3, P4 y P5). Después de una intensa
                investigación de mercado, dedujeron que el comportamiento del nuevo mercado es similar al del
                mercado existente.
              </p>
              <p>
                <span className="fw-bold">Contenido: </span>En su mercado actual, el equipo de ventas ha
                clasificado todos los clientes en 4 segmentos (A, B, C, D). Luego, realizaron un alcance
                segmentado y comunicación para diferentes segmentos de clientes. Esta estrategia ha funcionado
                excepcionalmente bien para a ellos. Planean utilizar la misma estrategia en nuevos mercados y
                han identificado 2627 nuevos potenciales clientes. Debe ayudar al gerente a predecir el grupo
                correcto de nuevos clientes.
              </p>
            </div>
            <div className='hstack gap-2'>
              <button
                type='button'
                className='btn btn-dark'
                data-bs-toggle="modal"
                data-bs-target="#exampleModal"
              >
                Analizar
              </button>
              <a
                className='btn'
                target="blank"
                href="https://www.kaggle.com/datasets/vetrirah/customer"
              >
                Más información
              </a>
            </div>
          </article>
          <div className="col-lg-6 d-none d-lg-block">
            <img
              alt="dibujo de un arbol de dinero"
              className='w-100'
              src="https://img.freepik.com/free-vector/business-planning-sketch-concept_1284-37242.jpg?w=740&t=st=1699025057~exp=1699025657~hmac=ad6c539f59c49e0ce3624586997a5806a8cb7711b6168d4be408d5e1321bce4b"
            />
          </div>
        </section>
        <section className="row my-5">
          <AnalysisResult></AnalysisResult>
        </section>
      </main>
      {/* Modal */}
      <div
        className="modal modal-md fade"
        id="exampleModal"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div className="modal-dialog modal-dialog-centered">
          <div className="modal-content">
            <div className="modal-header">
              <h2
                className="modal-title fs-5"
                id="exampleModalLabel">
                Opciones de análisis
              </h2>
              <button
                type="button"
                className="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              >
              </button>
            </div>
            <div className="modal-body">
              <form onSubmit={analyseData}>
                {
                  analysisOptionsEntries.map((analysisOptionEntry) => {
                    return (
                      <div
                        className="d-flex justify-content-between align-items-center py-1"
                        key={'form-option-' + analysisOptionEntry[0]}
                      >
                        {analysisOptionEntry[1]?.name}
                        <div>
                          <input
                            type="checkbox"
                            className="btn-check"
                            name={'btn-rado-' + analysisOptionEntry[0]}
                            id={'btn-rado-' + analysisOptionEntry[0]}
                            autoComplete="off"
                            onClick={handleSelectClicked}
                          />
                          <label
                            className="btn btn-outline-dark"
                            htmlFor={'btn-rado-' + analysisOptionEntry[0]}
                          >
                            Activar
                          </label>
                        </div>
                      </div>
                    )
                  })
                }
              </form>
            </div>
            <div className="modal-footer">
              <button
                type="button"
                className="btn"
                data-bs-dismiss="modal"
              >
                Cancelar</button>
              <button
                type="button"
                className="btn btn-dark"
              >
                Confirmar</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
