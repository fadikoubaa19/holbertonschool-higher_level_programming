#!/usr/bin/python3
''' lists all states from database '''


if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * from states ORDER BY states.id ASC")
    state_list = cursor.fetchall()
    for states in list:
        print(states)
    cursor.close()
    db.close()
