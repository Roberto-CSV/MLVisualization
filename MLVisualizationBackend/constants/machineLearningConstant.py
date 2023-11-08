from models.fillTechniqueModel import FillTechniqueModel


class DocumentTypesConstant:
    CSV: str = "csv"
    EXCEL: str = "excel"


class FillTechniquesConstant:
    MEAN: FillTechniqueModel = FillTechniqueModel(
        text="Valor medio de los datos", value="mean")
    STD: FillTechniqueModel = FillTechniqueModel(
        text="Valor promedio de los datos", value="std")
    MIN: FillTechniqueModel = FillTechniqueModel(
        text="Valor minimo de los datos", value="min")
    PERCENTILE_25: FillTechniqueModel = FillTechniqueModel(
        text="Valor del percentil 25 de los datos", value="25%")
    PERCENTILE_50: FillTechniqueModel = FillTechniqueModel(
        text="Valor del percentil 50 o mediana de los datos", value="50%")
    PERCENTILE_75: FillTechniqueModel = FillTechniqueModel(
        text="Valor del percentil 75 de los datos", value="75%")
    MAX: FillTechniqueModel = FillTechniqueModel(
        text="Valor maximo de los datos", value="max")
    PREVIOUS: FillTechniqueModel = FillTechniqueModel(
        text="Valor anterior no nulo", value="previous")
    NEXT: FillTechniqueModel = FillTechniqueModel(
        text="Valor siguiente no nulo", value="next")
    DROP: FillTechniqueModel = FillTechniqueModel(
        text="Eliminar filas con datos nulos en esta columna", value="drop")
