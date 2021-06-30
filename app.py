import dash
import dash_auth
import dash_bootstrap_components as dbc

from foiv_helper.callbacks import register_callbacks
from foiv_helper.layouts import serve_layout
from foiv_helper.load_cfg import Check_username_password

app = dash.Dash(__name__,
                title='Полномочия и роли пользователей',
                external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
auth = dash_auth.BasicAuth(app, Check_username_password)

app.layout = serve_layout
register_callbacks(app)

if __name__ == '__main__':
    app.run_server()
