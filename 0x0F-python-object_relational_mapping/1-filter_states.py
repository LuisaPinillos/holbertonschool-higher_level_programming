#!/usr/bin/python3
"""
script that lists all states from
the database hbtn_0e_0_usa.
"""


if __name__ == "__main__":

    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY\
                    'N%' ORDER BY states.id ASC")
    val = cursor.fetchall()
    for i in val:
        print(i)

    db.close()
