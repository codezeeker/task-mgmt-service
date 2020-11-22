import sqlite3
from sqlite3 import Error

def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        # conn = sqlite3.connect(':memory:')
        conn = sqlite3.connect('mydatabase.db')
        curs = conn.cursor()
        curs.execute("CREATE TABLE IF NOT EXISTS todo (item TEXT)")
        list_item = input("add the task: ")
        curs.execute("INSERT INTO todo(item) VALUES(?)", [list_item])
        curs.execute("COMMIT")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def retrieve_rows():
    conn = None
    try:
        conn = sqlite3.connect('mydatabase.db')
        # conn = sqlite3.connect(':memory:')
        curs = conn.cursor()
        curs.execute("SELECT * from todo")
        rows = curs.fetchall()
        print(rows)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

# Main loop
cont = "y"
while cont == "y":
    create_connection()
    cont = input("\nDo you want to continue[y/n]: ")

    if cont == "n":
        print("Here is your list:")
        retrieve_rows()