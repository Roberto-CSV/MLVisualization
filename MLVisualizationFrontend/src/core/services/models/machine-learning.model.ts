export interface AnalysisResultCustomerModel {
  ID: any;
  Gender: any;
  Ever_Married: any;
  Age: any;
  Graduated: any;
  Profession: any;
  Work_Experience: any;
  Spending_Score: any;
  Family_Size: any;
  Var_1: any;
  Segmentation: any;
}

export interface DataAnalysisResultModel {
  steps: AnalysisResultCustomerModel | undefined | null;
  data: CustomerModel[] | ConvertedCustomerModel[];
}

export interface AnalysisResultModel {
  original_data: any;
  columns_names: string[];
  columns_types: AnalysisResultCustomerModel | undefined | null;
  columns_nulls: AnalysisResultCustomerModel | undefined | null;
  columns_uniques: AnalysisResultCustomerModel | undefined | null;
  cleaned_data: DataAnalysisResultModel | undefined | null;
  converted_data: DataAnalysisResultModel | undefined | null;
}

// CUSTOMER
export interface CustomerModel {
  ID: number | undefined | null;
  Gender: string | undefined | null;
  Ever_Married: string | undefined | null;
  Age: number | undefined | null;
  Graduated: string | undefined | null;
  Profession: string | undefined | null;
  Work_Experience: number | undefined | null;
  Spending_Score: string | undefined | null;
  Family_Size: number | undefined | null;
  Var_1: string | undefined | null;
  Segmentation: string | undefined | null;
}

export interface ConvertedCustomerModel {
  ID: number | undefined | null;
  Gender: number | undefined | null;
  Ever_Married: number | undefined | null;
  Age: number | undefined | null;
  Graduated: number | undefined | null;
  Profession: number | undefined | null;
  Work_Experience: number | undefined | null;
  Spending_Score: number | undefined | null;
  Family_Size: number | undefined | null;
  Var_1: number | undefined | null;
  Segmentation: number | undefined | null;
}

export interface AnalysisResultModel {
  original_data: any;
  columns_names: string[];
  columns_types: AnalysisResultCustomerModel | undefined | null;
  columns_nulls: AnalysisResultCustomerModel | undefined | null;
  columns_uniques: AnalysisResultCustomerModel | undefined | null;
  cleaned_data: DataAnalysisResultModel | undefined | null;
  converted_data: DataAnalysisResultModel | undefined | null;
}

export interface PredictionResultModel {
  classification_report: object | null;
  confusion_matrix: object | null;
  prediction_data: [object] | null;
}

export interface MachineLearningModel {
  name: string;
  type: string;
}
