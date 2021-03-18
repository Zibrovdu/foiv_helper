import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import numpy as np
import dash_table
from foiv_helper.load_data import load_bounds_roles



def serve_layout():
    df = load_bounds_roles()

    units = [{'label': i, 'value': i} for i in np.sort(df['Отдел'].unique())]
    units.insert(0, dict(label='Все пользователи', value='Все пользователи'))

    layout = html.Div([
        html.Div([
            html.Div([
                html.Button("Легенда", id="open_legend",
                            style=dict(float='right', position='relative', margin='0 auto')),
            ], style=dict(padding='20px')),

            dbc.Modal(
                [dbc.ModalHeader("Легенда", style=dict(textAlign='center')),
                 dbc.ModalBody(
                     html.Div([
                         html.Table([
                             html.Tr([
                                 html.Td('-', style=dict(background='rgb(204, 236, 255)')),
                             ]),
                             html.Tr([
                                 html.Td('Администратор', style=dict(background='rgb(247, 143, 168)')),
                             ]),
                             html.Tr([
                                 html.Td('Ввод данных', style=dict(background='rgb(255, 255, 204)')),
                             ]),
                             html.Tr([
                                 html.Td('Просмотр', style=dict(background='rgb(204, 255, 204)')),
                             ]),
                             html.Tr([
                                 html.Td('Согласование', style=dict(background='rgb(247, 224, 244)')),
                             ]),
                             html.Tr([
                                 html.Td('Утверждение', style=dict(background='rgb(252, 195, 214)')),
                             ]),
                         ]),
                     ], style=dict(background='#ebecf1')),
                 ),
                 dbc.ModalFooter(
                     html.Button("Закрыть", id="close_legend")
                 ),
                 ],
                id="modal-scroll",
                backdrop='static',
                size="m",
                centered=True,
            ),
        ]),
        html.Br(),
        html.Div([
            html.H5('Название отдела: ', style=dict(width='98%', margin='0 auto')),
            dcc.Dropdown(id='unit_name', options=units, value='Все пользователи',
                         style=dict(width='99%', margin='0 auto')),
        ]),
        html.Br(),
        html.Div([
            html.H5('ФИО сотрудника: ', style=dict(width='98%', margin='0 auto')),
            dcc.Dropdown(id='fio', multi=True, placeholder='Выберите пользователей...',
                         style=dict(width='99%', margin='0 auto'))
        ]),
        html.Br(),
        html.Div([
            html.H5('Роли пользователя', style=dict(width='98%', margin='0 auto')),
            dcc.Dropdown(id='role', multi=True, placeholder='Выберите роль...',
                         style=dict(width='99%', margin='0 auto'))
        ]),
        html.Br(),
        html.Div([
            html.H5(id='subs')
        ]),
        html.Div([
            html.H5('Актуально на 05 марта 2021 года')
        ], style=dict(textAlign='right', padding='0 20px')),
        html.Div([
            dash_table.DataTable(id='bounds',
                                 style_as_list_view=False,
                                 sort_action="native",
                                 style_table={'overflowX': 'auto'},
                                 style_data=dict(whiteSpace='normal',
                                                 height='auto',
                                                 backgroundColor='rgb(204, 236, 255)'),
                                 style_cell={'textAlign': 'left'},
                                 style_data_conditional=[{'if': {'filter_query': '{Роль} = "Просмотр"'},
                                                          'backgroundColor': 'rgb(204, 255, 204)'},
                                                         {'if': {'filter_query': '{Роль} = "Ввод данных"'},
                                                          'backgroundColor': 'rgb(255, 255, 204)'},
                                                         {'if': {'filter_query': '{Роль} = "Согласование"'},
                                                          'backgroundColor': 'rgb(254, 210, 210)'},
                                                         {'if': {'filter_query': '{Роль} = "Утверждение"'},
                                                          'backgroundColor': 'rgb(253, 230, 254)'},
                                                         {'if': {'filter_query': '{Роль} = "Администратор"'},
                                                          'backgroundColor': 'rgb(247, 143, 168)'},
                                                         {'if': {'column_id': 'Подсистема'}, 'width': '4.5%'},
                                                         ],
                                 style_header={'backgroundColor': 'rgb(230, 230, 230)',
                                               'fontWeight': 'bold'},
                                 export_format='xlsx',
                                 export_headers='display',
                                 )
        ])
    ], style=dict(background='#ebecf1'))
    return layout
