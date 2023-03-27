import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


class SteelStrengthLoader:
    def __init__(self):
        self._csv_dataframe = None
        self.formula: pd.Series
        self.c: pd.Series
        self.mn: pd.Series
        self.si: pd.Series
        self.cr: pd.Series
        self.ni: pd.Series
        self.mo: pd.Series
        self.v: pd.Series
        self.n: pd.Series
        self.nb: pd.Series
        self.co: pd.Series
        self.w: pd.Series
        self.al: pd.Series
        self.ti: pd.Series
        self.yield_strength: pd.Series
        self.tensile_strength: pd.Series
        self.elongation: pd.Series
        self.feature_names = ['c', 'mn', 'si', 'cr', 'ni', 'mo', 'v', 'n', 'nb', 'co', 'w', 'al', 'ti']

    def get_target(self):
        return self.yield_strength

    def get_features(self):
        return self._csv_dataframe[self.feature_names]

    def load(self, csv_filename=''):
        self._csv_dataframe = pd.read_csv(csv_filename, sep=',', header=0)
        self._csv_dataframe.rename({'yield strength': 'yield_strength',
                                    'tensile strength': 'tensile_strength'}, axis='columns', inplace=True)
        self.formula = self._csv_dataframe['formula']
        self.c = self._csv_dataframe['c']
        self.mn = self._csv_dataframe['mn']
        self.si = self._csv_dataframe['si']
        self.cr = self._csv_dataframe['cr']
        self.ni = self._csv_dataframe['ni']
        self.mo = self._csv_dataframe['mo']
        self.v = self._csv_dataframe['v']
        self.n = self._csv_dataframe['n']
        self.nb = self._csv_dataframe['nb']
        self.co = self._csv_dataframe['co']
        self.w = self._csv_dataframe['w']
        self.al = self._csv_dataframe['al']
        self.ti = self._csv_dataframe['ti']
        self.yield_strenth = self._csv_dataframe['yield_strength']
        self.tensile_strength = self._csv_dataframe['tensile_strength']
        self.elongation = self._csv_dataframe['elongation']

    def _update_dataframe(self):
        self._csv_dataframe['formula'] = self.formula
        self._csv_dataframe['c'] = self.c
        self._csv_dataframe['mn'] = self.mn
        self._csv_dataframe['si'] = self.si
        self._csv_dataframe['cr'] = self.cr
        self._csv_dataframe['ni'] = self.ni
        self._csv_dataframe['mo'] = self.mo
        self._csv_dataframe['v'] = self.v
        self._csv_dataframe['n'] = self.n
        self._csv_dataframe['nb'] = self.nb
        self._csv_dataframe['co'] = self.co
        self._csv_dataframe['w'] = self.w
        self._csv_dataframe['al'] = self.al
        self._csv_dataframe['ti'] = self.ti
        self._csv_dataframe['yield strength'] = self.yield_strenth
        self._csv_dataframe['tensile strength'] = self.tensile_strength
        self._csv_dataframe['elongation'] = self.elongation

    def describe(self):
        print(self._csv_dataframe.describe())

    def get_column_names(self):
        return self._csv_dataframe.columns

    def scatter(self, x='yield_strength', y=''):
        fig = px.scatter(self._csv_dataframe, x=x, y=y)
        fig.show()

    def scatter_matrix(self, variable_space: list):
        fig = px.scatter_matrix(self._csv_dataframe, dimensions=variable_space)
        fig.show()

    def distplot(self, variable_space: list):
        pass

    def parallel_coords(self, variable_space: list):
        if len(variable_space) < 1:
            plotvars = self.feature_names.copy()

        else:
            plotvars = variable_space

        plotvars.append('yield_strength')
        print(plotvars)
        fig = px.parallel_categories(self._csv_dataframe[plotvars], color='yield_strength',
                                     color_continuous_scale=px.colors.sequential.Inferno)
        fig.show()
