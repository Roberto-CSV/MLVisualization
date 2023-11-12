from sklearn.linear_model import Lasso, LogisticRegression, Ridge, RidgeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVR, SVC
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

class AlgorithmsTypesConstant:
  REGRESSION = 'Regresión'
  CLASSIFICATION = 'Clasificación'

class MachineLearningModelsName:
  # Regression
  LINEAR_LASSO = 'LINEAR_LASSO'
  GRADIENT_BOOSTING = 'GRADIENT_BOOSTING'
  # Classification
  LINEAR_MULTINOMIAL_LOGISTIC_REGRESSION = 'LINEAR_MULTINOMIAL_LOGISTIC_REGRESSION'
  GUSSIAN_NAIVE_BAYES = 'GUSSIAN_NAIVE_BAYES'
  # Shared
  LINEAR_RIDGE = 'LINEAR_RIDGE'
  SUPPORT_VECTOR_MACHINES = 'SUPPORT_VECTOR_MACHINES'
  DECISION_TREES = 'DECISION_TREES'
  RANDOM_FOREST = 'RANDOM_FOREST'
  K_NEAREST_NEIGHBORRS = 'K_NEAREST_NEIGHBORRS'

class MachineLearningModelsConstant:
  REGRESSION = {
    MachineLearningModelsName.LINEAR_LASSO: {
      'name': 'Lasso',
      'type': AlgorithmsTypesConstant.REGRESSION,
      'algorithm': Lasso(alpha=0.1)
    },
    MachineLearningModelsName.GRADIENT_BOOSTING: {
      'name': 'Gradient boosting',
      'type': AlgorithmsTypesConstant.REGRESSION,
      'algorithm': GradientBoostingRegressor(random_state=0)
    },
    MachineLearningModelsName.LINEAR_RIDGE: {
      'name': 'Ridge',
      'type': AlgorithmsTypesConstant.REGRESSION,
      'algorithm': Ridge(),
    },
    MachineLearningModelsName.SUPPORT_VECTOR_MACHINES: {
      'name': 'Máquinas de soporte vectorial',
      'type': AlgorithmsTypesConstant.REGRESSION,
      'algorithm': make_pipeline(StandardScaler(), SVR(C=1.0, epsilon=0.2))
    },
    MachineLearningModelsName.DECISION_TREES: {
      'name': 'Árboles de decisión',
      'type': AlgorithmsTypesConstant.REGRESSION,
      'algorithm': DecisionTreeRegressor(random_state=0)
    },
    MachineLearningModelsName.RANDOM_FOREST: {
      'name': 'Bosques aleatorios',
      'type': AlgorithmsTypesConstant.REGRESSION,
      'algorithm': RandomForestRegressor(n_estimators=10)
    },
    MachineLearningModelsName.K_NEAREST_NEIGHBORRS: {
      'name': 'Vecinos más cercanos (KNN)',
      'type': AlgorithmsTypesConstant.REGRESSION,
      'algorithm': KNeighborsRegressor(n_neighbors=3)
    }
  }
  CLASSIFICATION = {
    MachineLearningModelsName.LINEAR_MULTINOMIAL_LOGISTIC_REGRESSION: {
      'name': 'Regresión logística multinomial',
      'type': AlgorithmsTypesConstant.CLASSIFICATION,
      'algorithm': LogisticRegression(random_state=0, multi_class='multinomial')
    },
    MachineLearningModelsName.GUSSIAN_NAIVE_BAYES: {
      'name': 'Naive bayes gussiano',
      'type': AlgorithmsTypesConstant.CLASSIFICATION,
      'algorithm': GaussianNB()
    },
    MachineLearningModelsName.LINEAR_RIDGE: {
      'name': 'Ridge',
      'type': AlgorithmsTypesConstant.CLASSIFICATION,
      'algorithm': RidgeClassifier(),
    },
    MachineLearningModelsName.SUPPORT_VECTOR_MACHINES: {
      'name': 'Máquinas de soporte vectorial',
      'type': AlgorithmsTypesConstant.CLASSIFICATION,
      'algorithm': make_pipeline(StandardScaler(), SVC(kernel='rbf', C=1.0, gamma=0.1))
    },
    MachineLearningModelsName.DECISION_TREES: {
      'name': 'Árboles de decisión',
      'type': AlgorithmsTypesConstant.CLASSIFICATION,
      'algorithm': DecisionTreeClassifier(random_state=0)
    },
    MachineLearningModelsName.RANDOM_FOREST: {
      'name': 'Bosques aleatorios',
      'type': AlgorithmsTypesConstant.CLASSIFICATION,
      'algorithm': RandomForestClassifier(n_estimators=10)
    },
    MachineLearningModelsName.K_NEAREST_NEIGHBORRS: {
      'name': 'Vecinos más cercanos (KNN)',
      'type': AlgorithmsTypesConstant.CLASSIFICATION,
      'algorithm': KNeighborsClassifier(n_neighbors=3)
    }
  }

