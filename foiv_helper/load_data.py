import pandas as pd

from foiv_helper.load_cfg import table_name


def load_bounds_roles(conn_string, table):
    """
    Синтаксис:
    ----------
    **load_bounds_roles** ()

    Описание:
    ----------
    Функция загружает в Датафрейм из базы данных данные по полномочиям и ролям пользователей.

    Returns:
    ----------
        **DataFrame**
    """
    df = pd.read_sql(f"""
        SELECT fio, org, unit, subs, role, bound, role_code
        FROM  {table}
        """, con=conn_string)
    df.columns = ['ФИО сотрудника', 'Организация (ФОИВ)', 'Отдел', 'Подсистема', 'Роль', 'Полномочие',
                  'Код роли доступа в ПОИБ']
    df = df[['ФИО сотрудника', 'Организация (ФОИВ)', 'Отдел', 'Подсистема', 'Роль', 'Полномочие',
             'Код роли доступа в ПОИБ']]
    df['Организация (ФОИВ)'] = df['Организация (ФОИВ)'].apply(lambda x: x.capitalize())
    df['ФИО сотрудника'] = df['ФИО сотрудника'].apply(lambda x: x.title())

    return df


def get_upd_date(conn_string, table):
    months = ['', 'Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября',
              'Ноября', 'Декабря']
    df = pd.read_sql(f"""
        SELECT pg_xact_commit_timestamp(xmin) 
        FROM {table}
        """, con=conn_string)
    upd_db_date = df.pg_xact_commit_timestamp.mean().strftime('%d %m %Y')

    return ' '.join([upd_db_date[:2], months[int(upd_db_date[3:5])], upd_db_date[6:], 'года'])
