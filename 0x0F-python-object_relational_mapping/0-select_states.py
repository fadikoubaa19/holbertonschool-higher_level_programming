#!/usr/bin/python3
'''
lists states from database hbtn_0e_0_usa
'''


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * from states ORDER BY states.id")
    state_list = cursor.fetchall()
    for states in list:
        print(states)
    cursor.close()
    db.close()
