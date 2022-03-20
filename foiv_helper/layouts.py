# import dash_bootstrap_components as dbc
from dash import dcc, html
# import dash_table
# import numpy as np
#
# from foiv_helper.load_cfg import connection_string, table_name
# from foiv_helper.load_data import load_bounds_roles, get_upd_date


def serve_layout():
    # df = load_bounds_roles(conn_string=connection_string,
    #                        table=table_name)
    #
    # units = [{'label': i, 'value': i} for i in np.sort(df['Отдел'].unique())]
    # units.insert(0, dict(label='Все пользователи', value='Все пользователи'))

    layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')])

    return layout
