export enum ALGORITHMS_TYPES {
  REGRESSION = 'Regresión',
  CLASSIFICATION = 'Clasificación'
}

export const MACHINE_LEARNING_MODELS = {
  REGRESSION: {
    LINEAR_LASSO: {
      name: 'Lasso',
      type: ALGORITHMS_TYPES.REGRESSION
    },
    GRADIENT_BOOSTING: {
      name: 'Gradient boosting',
      type: ALGORITHMS_TYPES.REGRESSION
    },
    LINEAR_RIDGE: {
      name: 'Ridge',
      type: ALGORITHMS_TYPES.REGRESSION
    },
    SUPPORT_VECTOR_MACHINES: {
      name: 'Máquinas de soporte vectorial (SVR)',
      type: ALGORITHMS_TYPES.REGRESSION
    },
    DECISION_TREES: {
      name: 'Árboles de decisión',
      type: ALGORITHMS_TYPES.REGRESSION
    },
    RANDOM_FOREST: {
      name: 'Bosques aleatorios',
      type: ALGORITHMS_TYPES.REGRESSION
    },
    K_NEAREST_NEIGHBORRS: {
      name: 'Vecinos más cercanos (KNN)',
      type: ALGORITHMS_TYPES.REGRESSION
    }
  },
  CLASSIFICATION: {
    LINEAR_MULTINOMIAL_LOGISTIC_REGRESSION: {
      name: 'Regresión logística multinomial',
      type: ALGORITHMS_TYPES.CLASSIFICATION
    },
    GUSSIAN_NAIVE_BAYES: {
      name: 'Naive bayes gussiano',
      type: ALGORITHMS_TYPES.CLASSIFICATION
    },
    LINEAR_RIDGE: {
      name: 'Ridge',
      type: ALGORITHMS_TYPES.CLASSIFICATION
    },
    SUPPORT_VECTOR_MACHINES: {
      name: 'Máquinas de soporte vectorial (SVC)',
      type: ALGORITHMS_TYPES.CLASSIFICATION
    },
    DECISION_TREES: {
      name: 'Árboles de decisión',
      type: ALGORITHMS_TYPES.CLASSIFICATION
    },
    RANDOM_FOREST: {
      name: 'Bosques aleatorios',
      type: ALGORITHMS_TYPES.CLASSIFICATION
    },
    K_NEAREST_NEIGHBORRS: {
      name: 'Vecinos más cercanos (KNN)',
      type: ALGORITHMS_TYPES.CLASSIFICATION
    }
  },
}