import { ModelResult } from './ModelResult';

export const MachineLearningResult = () => {
  return (
    <div className="row">
      <section className="col-lg-8 col-sm-12 mb-5">
        <article className="my-5" id="machine-learning-results">
          <h3 className="py-1">
            Resultados
          </h3>
          <p className="py-2">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum adipisci recusandae asperiores, architecto explicabo vitae, pariatur ex inventore earum mollitia error suscipit totam vero porro voluptate eos. Eveniet, dolorum quaerat?
            Veritatis debitis laudantium optio velit id ipsum harum. Nostrum ratione dolorum vero fuga, veniam saepe fugit ipsum, aut laborum officiis tenetur quas esse recusandae minima ullam ipsa laboriosam earum aperiam.
          </p>
        </article>
        <article className="row my-5" id='machine-learning-models'>
          <h4 className='py-1'>Modelos</h4>
          <div className="col-sm-12 col-xl-6 mt-2 mb-3">
            <ModelResult></ModelResult>
          </div>
          <div className="col-sm-12 col-xl-6 mt-2 mb-3">
            <ModelResult></ModelResult>
          </div>
        </article>
        <div className="row my-5" id='machine-learning-comparison'>
          <h4 className='py-1'>Comparación</h4>
          <p className='py-2'>
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Voluptatibus quod tenetur delectus. Quaerat ipsam corrupti dolorum temporibus. Officia dolorum consequatur laboriosam impedit ad, vero iure velit molestiae eius sed neque?
          </p>
          <div className="col my-2">
            <div className='card'>
              <div className="card-body">
                Nada
              </div>
            </div>
          </div>
        </div>
      </section>
      <section className="col-4 d-none d-lg-block">
        <div className="list-group sticky-top p-5">
          <h5 className="p-3 border-bottom">En esta página</h5>
          <a
            href="#machine-learning-results"
            className="list-group-item list-group-item-action border-0"
          >
            Resultados
          </a>
          <a
            href="#machine-learning-models"
            className="list-group-item list-group-item-action border-0"
          >
            Modelos
          </a>
          <a
            href="#machine-learning-comparison"
            className="list-group-item list-group-item-action border-0"
          >
            Comparación
          </a>
          {/* {
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
          } */}
        </div>
      </section>
    </div>
  )
}
