import sqlite3

def get_db():
    #make connection to .db file
    connection = sqlite3.connect("hotel.db")
    #initiate cursor
    cur = connection.cursor()

    return cur

def add_column_table(table_name: str, new_column: str, column_type: str) -> str:
    #get db connection
    cur = get_db()
    #define edit format
    add_column = f"ALTER TABLE {table_name} ADD COLUMN {new_column} {column_type}"
    #execute edit
    cur.execute(add_column)
    return f"You just added the {new_column} column to the {table_name} table."

# constraint_name would be "email" or "last_name" to refer to the column it is making unique
def add_constraint(table_name: str, table_column: str) -> str:
    #get db connection
    cur = get_db()
    #define edit format
    add_unique_constraint = f"CREATE UNIQUE INDEX {table_column}_unique ON {table_name}({table_column})"
    # execute edit
    cur.execute(add_unique_constraint)
    return f"You just added the UNIQUE constraint to the {table_column} column of the {table_name} table"

def display_tables():
    TABLES = ["customer", "room", "booking"]
    #get db connection
    cur = get_db()
    #display tables one by one
    for table in TABLES:
        for row in cur.execute(f"SELECT * FROM {table}"):
            print(row)



if __name__ == "__main__":
    # add command below to execute update


    # display tables after each update
    display_tables()

