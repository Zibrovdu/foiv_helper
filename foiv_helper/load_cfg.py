from sqlalchemy import create_engine
import configparser


cfg_parser = configparser.ConfigParser()
cfg_parser.read(f'settings.ini')

db_username = cfg_parser['connect']['username']
db_password = cfg_parser['connect']['password']
db_name = cfg_parser['connect']['db']
db_host = cfg_parser['connect']['host']
db_port = cfg_parser['connect']['port']
db_dialect = cfg_parser['connect']['dialect']

user_name = cfg_parser['user_1']['username']
user_pass = cfg_parser['user_1']['password']

connection_string = create_engine(f'{db_dialect}://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}',
                                  pool_pre_ping=True)

Check_username_password = {user_name: user_pass}
