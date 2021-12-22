#!/usr/bin/python3
"""
script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""


if __name__ == "__main__":

    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{}'ORDER BY states.id ASC" .format(argv[4]))
    val = cursor.fetchall()
    for i in val:
        print(i)

    db.close()
