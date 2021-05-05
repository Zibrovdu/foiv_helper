from dash.dependencies import Input, Output, State
import numpy as np
from foiv_helper.load_data import load_bounds_roles
from foiv_helper.load_cfg import connection_string, table_name


def register_callbacks(app):
    @app.callback(
        Output('fio', 'options'),
        Output('role', 'options'),
        Output('zp', 'options'),
        Output('bounds', 'columns'),
        Output('bounds', 'data'),
        [Input('unit_name', 'value'),
         Input('fio', 'value'),
         Input('role', 'value'),
         Input('zp', 'value')])
    def update_all(unit_name, fio_name, role_name, zp_name):
        df = load_bounds_roles(conn_string=connection_string,
                               table=table_name)
        if unit_name == 'Все пользователи':
            fio_list = [{'label': i, 'value': i} for i in np.sort(df['ФИО сотрудника'].unique())]
            role_list = [{'label': i, 'value': i} for i in np.sort(df['Роль'].unique())]
            zp_list = [{'label': i, 'value': i} for i in np.sort(df['Подсистема'].unique())]
            if not fio_name and not role_name and not zp_name:
                data_table_df = df.drop(['Отдел'], axis=1)
                columns = [{"name": i, "id": i} for i in data_table_df.columns]
                return fio_list, role_list, zp_list, columns, data_table_df.to_dict('records')
            else:
                if not role_name and (not zp_name and fio_name):
                    filtered_df = df[df['ФИО сотрудника'].isin(fio_name)]
                elif not role_name and (not fio_name and zp_name):
                    filtered_df = df[df['Подсистема'].isin(zp_name)]
                elif not role_name and (fio_name and zp_name):
                    filtered_df = df[(df['ФИО сотрудника'].isin(fio_name)) & (df['Подсистема'].isin(zp_name))]
                elif not fio_name and (not role_name and zp_name):
                    filtered_df = df[df['Подсистема'].isin(zp_name)]
                elif not fio_name and (role_name and not zp_name):
                    filtered_df = df[df['Роль'].isin(role_name)]
                elif not fio_name and (role_name and zp_name):
                    filtered_df = df[(df['Подсистема'].isin(zp_name)) & (df['Роль'].isin(role_name))]
                elif not zp_name and (not fio_name and role_name):
                    filtered_df = df[df['Роль'].isin(fio_name)]
                elif not zp_name and (fio_name and not role_name):
                    filtered_df = df[df['ФИО сотрудника'].isin(fio_name)]
                elif not zp_name and (fio_name and role_name):
                    filtered_df = df[(df['ФИО сотрудника'].isin(fio_name)) & (df['Роль'].isin(fio_name))]
                else:
                    filtered_df = df[(df['Роль'].isin(role_name)) & (df['ФИО сотрудника'].isin(fio_name)) & (
                        df['Подсистема'].isin(zp_name))]
                data_table_df = filtered_df.drop(['Отдел'], axis=1)
                columns = [{"name": i, "id": i} for i in data_table_df.columns]
                return fio_list, role_list, zp_list, columns, data_table_df.to_dict('records')

        elif unit_name:
            filtered_df = df[df['Отдел'] == unit_name]
            fio_list = [{'label': i, 'value': i} for i in np.sort(filtered_df['ФИО сотрудника'].unique())]
            role_list = [{'label': i, 'value': i} for i in np.sort(filtered_df['Роль'].unique())]
            zp_list = [{'label': i, 'value': i} for i in np.sort(df['Подсистема'].unique())]
            if not fio_name and not role_name and not zp_name:
                data_table_df = filtered_df.drop(['Отдел'], axis=1)
                columns = [{"name": i, "id": i} for i in data_table_df.columns]
                return fio_list, role_list, zp_list, columns, data_table_df.to_dict('records')
            else:
                if not role_name:
                    filtered_df = df[(df['Отдел'] == unit_name) & (df['ФИО сотрудника'].isin(fio_name)) & (
                        df['Подсистема'].isin(zp_name))]
                    if len(filtered_df) == 0:
                        filtered_df = df[df['Отдел'] == unit_name]
                    data_table_df = filtered_df.drop(['Отдел'], axis=1)
                    columns = [{"name": i, "id": i} for i in data_table_df.columns]
                    return fio_list, role_list, zp_list, columns, data_table_df.to_dict('records')
                elif not fio_name:
                    filtered_df = df[(df['Отдел'] == unit_name) & (df['Роль'].isin(role_name))]
                    if len(filtered_df) == 0:
                        filtered_df = df[(df['Отдел'] == unit_name) & (df['Роль'].isin(role_name)) & (
                            df['Подсистема'].isin(zp_name))]
                    data_table_df = filtered_df.drop(['Отдел'], axis=1)
                    columns = [{"name": i, "id": i} for i in data_table_df.columns]
                    return fio_list, role_list, zp_list, columns, data_table_df.to_dict('records')
                elif not zp_name:
                    filtered_df = df[(df['Отдел'] == unit_name) & (df['Роль'].isin(role_name)) & (
                        df['ФИО сотрудника'].isin(fio_name))]
                    if len(filtered_df) == 0:
                        filtered_df = df[(df['Отдел'] == unit_name) & (df['Роль'].isin(role_name))]
                    data_table_df = filtered_df.drop(['Отдел'], axis=1)
                    columns = [{"name": i, "id": i} for i in data_table_df.columns]
                    return fio_list, role_list, zp_list, columns, data_table_df.to_dict('records')
                else:
                    filtered_df = df[(df['Отдел'] == unit_name) & (df['ФИО сотрудника'].isin(fio_name)) &
                                     (df['Роль'].isin(role_name)) & (df['Подсистема'].isin(zp_name))]
                    if len(filtered_df) == 0:
                        filtered_df = df[(df['Отдел'] == unit_name) & (df['ФИО сотрудника'].isin(fio_name))]
                        if len(filtered_df) == 0:
                            filtered_df = df[(df['Отдел'] == unit_name) & (df['Роль'].isin(role_name))]
                            if len(filtered_df) == 0:
                                filtered_df = df[(df['Роль'] == role_name) & (df['Подсистема'].isin(zp_name))]
                    data_table_df = filtered_df.drop(['Отдел'], axis=1)
                    columns = [{"name": i, "id": i} for i in data_table_df.columns]
                    return fio_list, role_list, zp_list, columns, data_table_df.to_dict('records')

    @app.callback(
        Output("modal-scroll", "is_open"),
        [Input("open_legend", "n_clicks"), Input("close_legend", "n_clicks")],
        [State("modal-scroll", "is_open")],
    )
    def toggle_modal(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open
