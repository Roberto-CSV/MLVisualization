import { ClipboardDataIcon, DiagramIcon, HouseIcon } from "../../shared/components/Icon"


const SidebarNavItem = ({ name, icon, active = false }) => {
  return (
    <li className="list-group-item border-0 p-0 my-1 d-grid">
      <button type="button" className="btn text-start border-0">
        <div className={"row g-0" + (active ? " fw-bold" : "")}>
          <div className="col-4 text-center">{icon}</div>
          <div className="col-8">{name}</div>
        </div>
      </button>
    </li>
  )
}

export const Sidebar = () => {
  return (
    <aside className="container-fluid h-100 border-end">
      <div className="row row-cols-1 h-100 align-items-center justify-content-center text-center">
        <div id="sidebar-top-items" className="col text-center">
          <img className="w-50" src="https://img.freepik.com/free-vector/electric-bulb-filled-with-water-energy-concept-vector-concept-ecology_460848-14739.jpg?w=740&t=st=1698970592~exp=1698971192~hmac=6e245c954ec2d6c5604619c484282db75a6066c66e8d00eb51623c20be021537" />
        </div>
        <div id="sidebar-middle-items" className="col border-0 align-self-start">
          <ul className="list-group list-group-flush  border-0">
            <SidebarNavItem name={'Inicio'} icon={<HouseIcon></HouseIcon>} active></SidebarNavItem>
            <SidebarNavItem name={'Análisis'} icon={<ClipboardDataIcon></ClipboardDataIcon>}></SidebarNavItem>
            <SidebarNavItem name={'Modelos'} icon={<DiagramIcon></DiagramIcon>}></SidebarNavItem>
          </ul>
        </div>
        <div id="sidebar-bottom-items" className="col">
          {/* Bottom content */}
        </div>
      </div>
    </aside>
  )
}
