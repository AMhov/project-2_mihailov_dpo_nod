from src.primitive_db.utils import save_metadata
from src.primitive_db.utils import read_config, load_metadata

_FILEPATH = read_config().get('constants').get('FILEPATH')


def create_table(metadata: dict, table_name: str, columns: list):
    """Создание таблицы
    Output: dict - вернет метаданные в случае успеха
    """
    if not metadata.get(table_name):
        columns = ['ID:int'] + columns
        data_type = [col_name.split(':')[1] for col_name in columns]
        if set(data_type).issubset(set(['bool', 'int', 'str'])):
            metadata[table_name] = dict(i.split(':') for i in columns)
            save_metadata(_FILEPATH, metadata)
            print(f"Таблица {table_name} успешно создана со столбцами: {', '.join(columns)}")
            return metadata
        else:
            print("Ошибка: Неверный тип данных в столбцах.")
    else:
        print(f"Ошибка: Таблица {table_name} уже существует.")


def drop_table(metadata: dict, table_name: str) -> None:
    """Удаление таблицы"""
    if metadata.get(table_name):
        del metadata[table_name]
        save_metadata(_FILEPATH, metadata)
        print(f"Таблица {table_name} успешно удалена.")
        return metadata
    else:
        print(f"Ошибка: Таблица {table_name} не существует.")


def list_tables(metadata: dict) -> list:
    """Вывод списка таблиц"""
    try:
        tables = list(metadata.keys())
        if tables:
            for table in tables:
                print(f"- {table}")
        else:
            print("Ошибка: Нет таблиц в базе данных.")
    except:
        print("Метаданные получены неверно.")


def insert(metadata, table_name, values):
    """Добавление данных в таблицу"""
    if metadata.get(table_name):
        if len(values) == len(metadata[table_name]) - 1:
            if all(isinstance(value, str) for value in values):        # ???? need check
                values = [None] + values
                metadata[table_name]['data'].append(values)
                save_metadata(_FILEPATH, metadata)
                print(f"Запись {values} успешно добавлена в таблицу {table_name}.")
                return metadata # ???????????
            

def select(table_data, where_clause:dict=None):
    """Отбор и фильтрация данных при наличии фильтров"""
    if where_clause:
        for key, value in where_clause.items():
            if key in table_data[0]:
                table_data = [row for row in table_data if row[table_data[0].index(key)] == value]
        return table_data
    else:
        return table_data
    

def update(table_data, set_clause, where_clause:dict):
    """Обновление данных в таблице"""
    if where_clause:
        for key, value in where_clause.items():
        #     if key in table_data[0]:
        #         table_data = [row for row in table_data if row[table_data[0].index(key)] == value]
        # for key, value in set_clause.items():
        #     if key in table_data[0]:
