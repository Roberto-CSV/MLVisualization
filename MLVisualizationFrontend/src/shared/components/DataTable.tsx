import { useState } from "react";

export const DataTable = (props) => {
  const rowsQuantity: number = 10;
  const minPage: number = props?.data?.length ? 1 : 0;
  const maxPage: number = Math.ceil((props?.data?.length ?? 0) / rowsQuantity);
  const [partialData, setPartialData] = useState(props?.data?.slice(0, rowsQuantity));
  const [actualPage, setActualPage] = useState(minPage ?? 0);
  const [columnsToShow, setColumnsToShow] = useState(props?.columns);

  const handlePreviousPage = () => {
    if (actualPage > minPage) {
      const previousPage: number = actualPage - 1;
      const firstItemPosition: number = (previousPage * rowsQuantity) - rowsQuantity >= 0
        ? (previousPage * rowsQuantity) - rowsQuantity
        : 0;
      const lastItemPosition: number = firstItemPosition + rowsQuantity;
      setPartialData(props.data.slice(firstItemPosition, lastItemPosition));
      setActualPage(previousPage);
    }
  }
  const handleNextPage = () => {
    if (actualPage < maxPage) {
      const nextPage: number = actualPage + 1;
      const firstItemPosition: number = (actualPage * rowsQuantity);
      const lastItemPosition: number = (firstItemPosition + rowsQuantity) < props?.data?.length
        ? (firstItemPosition + rowsQuantity)
        : props?.data?.length;
      setPartialData(props?.data?.slice(firstItemPosition, lastItemPosition));
      setActualPage(nextPage);
    }
  }
  const reloadPartialData = () => {
    const firstItemPosition: number = actualPage == 1
      ? 0
      : actualPage * rowsQuantity;
    setPartialData(props.data.slice(firstItemPosition, firstItemPosition + partialData.length));
  }
  const handleSelectColumnsChange = (event: any) => {
    const target: any = event.target;
    const value: any = target.type === 'checkbox' ? target.checked : target.value;
    const name: string = target.name;
    let partialColumnsToShow: string[] = columnsToShow;
    if (value) {
      partialColumnsToShow.unshift(name);
    } else {
      partialColumnsToShow = partialColumnsToShow.filter((column: string) => column != name);
    }
    setColumnsToShow(partialColumnsToShow);
    reloadPartialData()
  };

  return (
    <div className="container g-0">
      <div className="row">
        <div className="col table-responsive">
          <table className="table table-hover border">
            <thead className="table-light">
              <tr>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="p-3 text-center" colSpan={3}>No hay datos a mostrar en la tabla.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div className="row">
        <div className="col">
          <p className="text-body-secondary">Página {actualPage} de {maxPage}</p>
        </div>
        <div className="col text-end">
          <button
            className="btn btn-outline-secondary btn-sm"
            disabled={actualPage == minPage}
            onClick={handlePreviousPage}
          >
            Anterior
          </button>
          <button
            className="btn btn-outline-secondary ms-2 btn-sm"
            disabled={actualPage == maxPage}
            onClick={handleNextPage}
          >
            Siguiente
          </button>
        </div>
      </div>
    </div>
  )
}