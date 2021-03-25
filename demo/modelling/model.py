import datetime
import os
import typing as t
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin, RegressorMixin
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, cross_validate, TimeSeriesSplit
from sklearn.metrics import  make_scorer
from sklearn.model_selection import ShuffleSplit
import warnings
warnings.filterwarnings("ignore")

def build_estimator(hyperparams: t.Dict[str, t.Any]):
    estimator_mapping = get_estimator_mapping()
    steps = []
    for name, params in hyperparams.items():
        estimator = estimator_mapping[name](**params)
        steps.append((name, estimator))
    model = Pipeline(steps)
    return model


def get_estimator_mapping():
    return {
        "regressor": RandomForestRegressor,
        "extractor": BikeRentalFeatureExtractor,
        
    }


def rollingAv1(Data):

    Columns_to_RAverage= ['atemp','hum','windspeed']
    X=Data.copy()

    for i in Columns_to_RAverage:
      a=X[i].astype(float)
      a_shifted = a.shift(1)
      a_window = a_shifted.rolling(window=4)
      a_means = a_window.mean()
      NewName='a_'+i
      X[NewName] = a_means
    X=X.fillna(0)
    return X

class BikeRentalFeatureExtractor(BaseEstimator, TransformerMixin):
  
  def __init__(self):
    pass

  def fit(self,X, y=None):
    if y.shape[0]>0:
      self.y=y
      return self
    else:
      pass
  
  def transform(self,x):
    return rollingAv1(x)

#model = Pipeline(steps=[
#    ("extractor", BikeRentalFeatureExtractor()),
#    ("regressor", RandomForestRegressor())
#    ])

parameters = {'regressor__n_estimators':[200,300,400,500]}

time_series_splitter=TimeSeriesSplit(n_splits=6, max_train_size=7)

#clf = GridSearchCV(estimator=model, param_grid=parameters, cv=time_series_splitter, scoring=scorer)
#clf.fit(X_train,y_train)

