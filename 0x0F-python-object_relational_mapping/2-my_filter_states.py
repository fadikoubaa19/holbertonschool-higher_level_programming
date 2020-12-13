#!/usr/bin/python3
''' Module to print all states '''
    import MySQLdb
    from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    woof = db.cursor()
    woof.execute("SELECT * from states WHERE name LIKE '{}' \
                COLLATE latin1_general_cs\
                ORDER BY states.id".format(argv[4]))
    for row in woof.fetchall():
        print(row)
    woof.close()
    db.close()
