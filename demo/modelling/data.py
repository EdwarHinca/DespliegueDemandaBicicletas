import datetime
import os

import typing as t
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import typing_extensions as te
from sklearn.base import BaseEstimator, TransformerMixin, RegressorMixin
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, cross_validate, TimeSeriesSplit
from sklearn.metrics import  make_scorer
from sklearn.model_selection import ShuffleSplit
import warnings
warnings.filterwarnings("ignore")

#df = pd.read_csv("local/data/timeseries.csv")

class DatasetReader(te.Protocol):
    def __call__(self) -> pd.DataFrame:
        ...


SplitName = te.Literal["train", "test"]


def get_dataset(reader: DatasetReader, splits: t.Iterable[SplitName]):
    df = reader()
    #df = clean_dataset(df)
    target_column = "cnt"
    y = df[target_column]
    feature_columns = ['yr', 'mnth', 'hr','season', 'holiday', 'weekday','workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed']
    X = df[feature_columns]
    indices_train=X['yr']==0
    X_train, y_train = X[indices_train], y[indices_train]
    X_test, y_test = X[~indices_train], y[~indices_train]


    split_mapping = {"train": (X_train, y_train), "test": (X_test, y_test)}
    return {k: split_mapping[k] for k in splits}



