import { ALGORITHMS_TYPES, MACHINE_LEARNING_MODELS } from "../../core/const/MachineLearningModels"
import { MachineLearningResult } from "./components/MachineLearningResult";

export const MachineLearning = () => {
  const machineLearningModelsEntries = Object.entries(MACHINE_LEARNING_MODELS);
  console.log(machineLearningModelsEntries)
  const onSubmit = (e: any) => {

  }

  return (
    <div className='container-fluid h-100'>
      <main className='d-flex flex-wrap align-items-center h-100'>
        <section className="row h-100">
          <div className="row align-self-end">
            <h2 className='py-1'>Modelos de aprendizaje automático</h2>
            <p className='py-4'>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea provident vitae voluptatum optio, libero cum expedita, non mollitia animi a quas doloremque eos dicta nisi amet nam odio deleniti facilis.
              Quisquam, eos expedita dicta incidunt nobis fugiat dolorem. In cumque, quos quo officia, eum beatae repellendus alias fugiat laborum iste possimus fuga, voluptas delectus quidem dolor quam assumenda nulla corrupti.
              Provident ad reiciendis, culpa, dolor nam impedit quisquam fugit ab possimus nesciunt velit quidem laboriosam. Maxime voluptate, earum illum id ut tempore repellendus provident, accusantium distinctio illo doloremque excepturi nam.
            </p>
          </div>
          <form className="row align-self-start">
            <p className="fw-bold">Prueba los modelos:</p>
            <div className="col-lg-7 col-sm-12 py-2">
              <input
                type="file"
                className="form-control"
                id="inputGroupFile02"
              />
            </div>
            <div className="col-lg-3 col-sm-12 py-2">
              <select
                className="form-select"
                aria-label="Default select example"
              >
                <option hidden defaultValue={'nonSelectedModel'}>Selecciona el modelo</option>
                {
                  machineLearningModelsEntries.map((algorithmType, algorithmsTypesIndex) => {
                    return (
                      <>
                        <option
                          disabled
                          key={algorithmType[0].concat(algorithmsTypesIndex.toString())}
                        >
                          {
                            algorithmsTypesIndex == 0
                              ? ALGORITHMS_TYPES.REGRESSION
                              : ALGORITHMS_TYPES.CLASSIFICATION
                          }
                        </option>
                        {
                          Object.entries(algorithmType[1]).map((machineLearningModel) => {
                            return (
                              <>
                                <option
                                  value={[machineLearningModel[1].name, machineLearningModel[1].type]}
                                  key={machineLearningModel[0].concat(machineLearningModel[1].type)}
                                >
                                  {machineLearningModel[1].name}
                                </option>
                              </>
                            )
                          })
                        }
                      </>
                    )
                  })
                }
              </select>
            </div>
            <div className="col-lg-2 col-sm-12 py-2">
              <button type="submit" className="btn btn-dark w-100">Clasificar</button>
            </div>
          </form>
        </section>
        <section className="row h-100">
          <MachineLearningResult></MachineLearningResult>
        </section>
      </main>
    </div>
  )
}
