import shlex
import prompt
from src.primitive_db.core import create_table, drop_table, list_tables
from src.primitive_db.utils import read_config, load_metadata

_FILEPATH = read_config().get('constants').get('FILEPATH')
_CONDITION = True
metadata = load_metadata(_FILEPATH)

def show_help():
    """Показать справку"""
    print("\n***Процесс работы с таблицей***")
    print("Функции:")
    print("<command> create_table <имя_таблицы> <столбец1:тип> .. - создать таблицу")
    print("<command> list_tables - показать список всех таблиц")
    print("<command> drop_table <имя_таблицы> - удалить таблицу")
    print("\nОбщие команды:")
    print("<command> exit - выход из программы")
    print("<command> help - справочная информация\n") 

def process_command(command):
    """Обработка команд пользователя"""
    match command[0]:
        case "help":
            show_help()
        case "quit" | "exit":
            global _CONDITION
            _CONDITION = False
            print("Выход.")
        case "create_table":
            if len(command) < 2:
                print(f"Некорректное значение: <{command[1:]}>.Попробуйте снова.")
            else:
                create_table(
                    metadata=metadata,
                    table_name=command[1],
                    columns=command[2:]
                    )
        case "list_tables":
            if len(command) > 1:
                print(f"Некорректное значение: <{command[1:]}>. Попробуйте снова.")
            else:
                list_tables(metadata=metadata)
        case "drop_table":
            if len(command) != 2:
                print(f"Некорректное значение: <{command[1:]}>. Попробуйте снова.")
            else:
                drop_table(
                    metadata=metadata,
                    table_name=command[1]
                    )
        case _:
            print(f"Функции <{command[0]}> нет. Попробуйте снова.")



def welcome():
    print("Первая попытка запустить проект!", "\n\n***")
    show_help()

    while _CONDITION:
        user_input = prompt.string(" Введите команду_ ")
        args = shlex.split(user_input)
        process_command(args)
