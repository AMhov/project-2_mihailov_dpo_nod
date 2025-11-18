import prompt
from src.primitive_db.core import create_table, drop_table, list_tables
from src.primitive_db.utils import read_config, load_metadata

_FILEPATH = read_config().get('constants').get('FILEPATH')


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
    match command.split(" ")[0]:
        case "help":
            show_help()
        case "quit" | "exit":
            print("Выход.")
        case "create_table":
            if len(command.split(" ")) < 2:
                print(f"Некорректное значение: <{command.split(" ")[1:]}>.Попробуйте снова.")
            else:
                create_table(
                    metadata=load_metadata(_FILEPATH),
                    table_name=command.split(" ")[1],
                    columns=command.split(" ")[2:]
                    )
        case "list_tables":
            if len(command.split(" ")) > 1:
                print(f"Некорректное значение: <{command.split(" ")[1:]}>. Попробуйте снова.")
            else:
                list_tables(metadata=load_metadata(_FILEPATH))
        case "drop_table":
            if len(command.split(" ")) != 2:
                print(f"Некорректное значение: <{command.split(" ")[1:]}>. Попробуйте снова.")
            else:
                drop_table(
                    metadata=load_metadata(_FILEPATH),
                    table_name=command.split(" ")[1]
                    )
        case _:
            print(f"Функции <{command.split(" ")[0]}> нет. Попробуйте снова.")



def welcome():
    print("Первая попытка запустить проект!", "\n\n***")
    show_help()

    command = prompt.string(" Введите команду_ ")

    process_command(command)
