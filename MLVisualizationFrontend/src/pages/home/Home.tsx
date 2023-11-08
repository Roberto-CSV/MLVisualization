
export const Home = () => {
  return (
    <div className='container-fluid h-100'>
      <main className='d-flex h-100 align-items-center'>
        <div className="row align-items-center">
          <section className="col-6">
            <h1 className='py-1'>Gestión y análisis de datos</h1>
            <p className='py-4'>Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque enim, doloribus
              odio provident eligendi tenetur repellat saepe quaerat quae! Dolor, itaque molestiae
              labore ea commodi quas nisi voluptate dignissimos? Rem!</p>
            <div className='hstack gap-2'>
              <button type='button' className='btn btn-dark'>Comenzar</button>
              <a className='btn' target="blank" href="https://www.google.com/search?q=Gesti%C3%B3n+y+an%C3%A1lisis+de+datos&rlz=1C1UEAD_esCO1070CO1070&sourceid=chrome&ie=UTF-8">Más información</a>
            </div>
          </section>
          <section className="col-6">
            <img alt="Dibujo de un arbol de dinero" className='w-100' src="https://img.freepik.com/free-vector/business-tree-knowledge-tree-hand-drawn-sketch-vector-illustration_460848-14196.jpg?w=740&t=st=1698967050~exp=1698967650~hmac=73e8f9d3fe8d5cbc1e66342bb8c02f86da3ca299740b8710ef25f537a8aabce0" />
          </section>
        </div>
      </main>
    </div>
  )
}
