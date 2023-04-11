import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd


def _get_nrows(ncols: int, nfeatures: int):
    _nrows = round(nfeatures / ncols)
    if nfeatures % ncols > 0:
        _nrows += 1
    return _nrows


def plot_gridded(df: pd.DataFrame,
                 feature_names: list,
                 plotly_method,
                 subplots_kwargs: dict,
                 plotting_func_kwargs: dict,
                 target_name: str = '',
                 ncols: int = 3,
                 figure_height: int = 1400):
    nrows = _get_nrows(ncols, len(feature_names))
    fig = make_subplots(rows=nrows, cols=ncols, shared_xaxes=True, shared_yaxes=True, subplot_titles=feature_names)
    fig.update_layout(autosize=False, width=800, height=figure_height)

    column_i = 1
    row_j = 1
    for feature in feature_names:
        if any((target_name == '', target_name is None)):
            fig.add_trace(plotly_method(x=df[feature], name=feature, **plotting_func_kwargs), row=row_j, col=column_i)

        else:
            fig.add_trace(plotly_method(x=df[feature], y=df[target_name], name=feature, **plotting_func_kwargs),
                          row=row_j, col=column_i)

        if column_i % ncols == 0:
            row_j += 1
            column_i = 0
        column_i += 1
    fig.show()
