import prompt


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
    match command:
        case "help":
            show_help()
        case "quit" | "exit":
            print("Выход.")


def welcome():
    print("Первая попытка запустить проект!", "\n\n***")
    show_help()

    command = prompt.string(" Введите команду_ ")

    process_command(command)
