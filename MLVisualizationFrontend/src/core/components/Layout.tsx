import { Sidebar } from './Sidebar'

export const Layout = ({children}) => {
  return (
    <>
      <div className='row vh-100 g-0 overflow-hidden'>
        <section className='col-md-2 h-100 d-none d-md-block'>
          <Sidebar></Sidebar>
        </section>
        <main className='col-12 col-md-10 overflow-auto px-4 h-100'>
          {children}
        </main>
      </div>
    </>
  )
}
