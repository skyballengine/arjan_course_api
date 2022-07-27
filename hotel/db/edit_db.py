import sqlite3

def add_column_table(table_name: str, new_column: str, column_type: str) -> str:
    #make connection to .db file
    connection = sqlite3.connect("hotel.db")
    #initiate cursor
    cur = connection.cursor()
    #define edit format
    add_column = f"ALTER TABLE {table_name} ADD COLUMN {new_column} {column_type}"
    #execute edit
    cur.execute(add_column)
    return f"You just added the {new_column} column to the {table_name} table."



