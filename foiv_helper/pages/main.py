from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import numpy as np
from foiv_helper.load_cfg import connection_string, table_name
from foiv_helper.load_data import load_bounds_roles

units = [{'label': i, 'value': i} for i in np.sort(load_bounds_roles(conn_string=connection_string,
                                                                     table=table_name)['Отдел'].unique())]
units.insert(0, dict(label='Все пользователи', value='Все пользователи'))

layout = html.Div([
    html.Div([
        html.H2(
            'Полномочия и роли'
        ),
        html.Img(
            src="assets/logo.png"
        )
    ],
        className="banner"),
    html.Div([
        html.Div([
            html.Button("Легенда",
                        id="open_legend",
                        className='legend_btn'),
        ], className='div_legend_btn'),

        dbc.Modal(
            [dbc.ModalHeader("Легенда"),
             dbc.ModalBody(
                 html.Div([
                     html.Table([
                         html.Tr([
                             html.Td('Администратор',
                                     style=dict(background='rgb(247, 143, 168)')),
                         ]),
                         html.Tr([
                             html.Td('Ввод данных',
                                     style=dict(background='rgb(255, 255, 204)')),
                         ]),
                         html.Tr([
                             html.Td('Просмотр',
                                     style=dict(background='rgb(204, 255, 204)')),
                         ]),
                         html.Tr([
                             html.Td('Согласование',
                                     style=dict(background='rgb(247, 224, 244)')),
                         ]),
                         html.Tr([
                             html.Td('Утверждение',
                                     style=dict(background='rgb(252, 195, 214)')),
                         ]),
                     ]),
                 ], className='backgrd_color'),
             ),
             dbc.ModalFooter(
                 html.Button("Закрыть",
                             id="close_legend")),
             ],
            id="modal-scroll",
            backdrop='static',
            size="m",
            centered=True,
        ),
        html.Div([
            html.A("Обновление",
                   href='page_load_data',
                   className='legend_btn back_lnk')
        ],
            className='div_legend_btn'
        )
    ]),
    html.Br(),
    html.Div([
        html.H5('Название отдела: ',
                className='h5_dropdown'),
        dcc.Dropdown(id='unit_name',
                     options=units,
                     value='Все пользователи',
                     className='h5_dropdown'),
    ]),
    html.Br(),
    html.Div([
        html.H5('ФИО сотрудника: ',
                className='h5_dropdown'),
        dcc.Dropdown(id='fio',
                     multi=True,
                     placeholder='Выберите пользователей...',
                     className='h5_dropdown')
    ]),
    html.Br(),
    html.Div([
        html.H5('Роли пользователя:',
                className='h5_dropdown'),
        dcc.Dropdown(id='role',
                     multi=True,
                     placeholder='Выберите роль...',
                     className='h5_dropdown')
    ]),
    html.Br(),
    html.Div([
        html.H5('Подсистема:',
                className='h5_dropdown'),
        dcc.Dropdown(id='zp',
                     multi=True,
                     placeholder='Выберите...',
                     className='h5_dropdown')
    ]),
    html.Br(),
    html.Div([
        html.H5(f'Актуально на {"get_upd_date(conn_string=connection_string, table=table_name)"}')
    ], className='h5_update_data_label'),
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
    ], className='h5_dropdown')
], className='backgrd_color')
