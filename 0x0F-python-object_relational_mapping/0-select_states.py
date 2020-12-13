#!/usr/bin/python3
'''
lists states from database hbtn_0e_0_usa
'''


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    states_list = cur.fetchall()
    for state in state_list:
        print("({}, '{}')".format(state[0], state[1]))
    cur.close()
