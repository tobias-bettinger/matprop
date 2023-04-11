import os.path

import numpy as np
import pandas as pd
import xgboost as xgb


class XGBModel:
    def __init__(self, model_path: str = ''):
        self.model = None
        self._model_path = model_path
        self._load()

    def _load(self):
        if os.path.exists(self._model_path):
            self.model = xgb.Booster()
            self.model.load_model(self._model_path)

        else:
            raise FileExistsError

    def predict(self, features):
        if any((isinstance(features, np.ndarray), isinstance(features, pd.DataFrame))):
            return self.model.predict(xgb.DMatrix(features))

        elif isinstance(features, xgb.DMatrix):
            return self.model.predict(features)

        else:
            raise TypeError(f'Your feature input is of type {type(features)} which is not a valid type!')
