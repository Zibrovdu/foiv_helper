from dash import dcc, html

layout = html.Div([
    html.Div([
        html.H2(
            'Полномочия и роли'
        ),
        html.Img(
            src="assets/logo.png"
        )
    ],
        className="banner"
    ),
    html.Div([
        html.A('Главная страница',
               href='/',
               className='legend_btn back_lnk')
    ],
        className='div_legend_btn'
    ),
    html.Br(),
    html.Br(),
    html.Div([
        html.Div([
            html.H3('Загрузка данных из ПОИБ')
        ],
            className='div_load'
        ),
        html.Div([
            html.H3('Загрузка данных по сотрудникам')
        ])
    ])
],
    className='backgrd_color'
)
