

def create_table(metadata, table_name, columns):
    columns = ['id'] + columns['columns']
    try:
        if not metadata.tables.get(table_name):
            for col_name in columns:
                if isinstance(col_name, (str, int, bool)):
                    table = Table(table_name, metadata, *columns)


            return table
    except Exception as e:
        print(e)
        return None
