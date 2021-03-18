import pandas as pd
from foiv_helper.load_cfg import connection_string


def load_bounds_roles():
    """
    Синтаксис:
    ----------

    load_bounds_roles()

    Описание:
    ----------
    Функция загружает в Датафрейм из базы данных данные по полномочиям и ролям пользователей.

    Returns:
    ----------
        **pandas.DataFrame**
    """
    df = pd.read_sql('bounds_roles', con=connection_string)
    df.columns = ['ФИО сотрудника', 'Организация (ФОИВ)', 'Отдел', 'Полномочие', 'Роль', 'Код роли доступа в ПОИБ',
                  'Подсистема']
    df = df[['ФИО сотрудника', 'Организация (ФОИВ)', 'Отдел', 'Подсистема', 'Роль', 'Полномочие',
             'Код роли доступа в ПОИБ']]
    df['Организация (ФОИВ)'] = df['Организация (ФОИВ)'].apply(lambda x: x.capitalize())
    df['ФИО сотрудника'] = df['ФИО сотрудника'].apply(lambda x: x.title())

    return df
