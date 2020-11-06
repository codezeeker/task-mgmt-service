import sqlite3
from sqlite3 import Error


def create_connection():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(':memory:')
        #conn = sqlite3.connect('mydatabase.db')
        curs = conn.cursor()
        curs.execute("CREATE TABLE IF NOT EXISTS todo (item TEXT)")

        curs.execute("INSERT INTO todo values('first item')")


        #test
        curs.execute("SELECT * from todo")
        rows = curs.fetchall()
        print(rows)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


create_connection()

#if __name__ == '__main__':
#    create_connection()