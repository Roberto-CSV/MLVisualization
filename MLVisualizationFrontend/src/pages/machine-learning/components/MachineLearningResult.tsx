import { ModelResult } from './ModelResult';

export const MachineLearningResult = () => {
  return (
    <div className="row">
      <section className="col-lg-12 col-sm-12 mb-5">
        <article className="my-5" id="machine-learning-results">
          <h3 className="py-1">
            Modelos
          </h3>
          <p className="py-2">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum adipisci recusandae asperiores, architecto explicabo vitae, pariatur ex inventore earum mollitia error suscipit totam vero porro voluptate eos. Eveniet, dolorum quaerat?
            Veritatis debitis laudantium optio velit id ipsum harum. Nostrum ratione dolorum vero fuga, veniam saepe fugit ipsum, aut laborum officiis tenetur quas esse recusandae minima ullam ipsa laboriosam earum aperiam.
          </p>
        </article>
        <article className="row my-5" id='machine-learning-models'>
          <h4 className='py-1'>Modelos</h4>
          <div className="col-sm-12 col-xl-3 mt-2 mb-3">
            <ModelResult modelName={"Máquinas de soporte vectorial"}></ModelResult>
          </div>
          <div className="col-sm-12 col-xl-3 mt-2 mb-3">
            <ModelResult modelName={"Árboles de decisión"}></ModelResult>
          </div>
          <div className="col-sm-12 col-xl-3 mt-2 mb-3">
            <ModelResult modelName={"Bosques aleatorios"}></ModelResult>
          </div>
          <div className="col-sm-12 col-xl-3 mt-2 mb-3">
            <ModelResult modelName={"Vecinos más cercanos (KNN)"}></ModelResult>
          </div>
        </article>
      </section>
    </div>
  )
}
