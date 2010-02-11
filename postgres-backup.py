#!/usr/bin/python2.6

import psycopg2
import sys
import os

if __name__ == '__main__':
    connection = psycopg2.connect(
        database='postgres',
        host='localhost',
        user='postgres',
        password=sys.argv[1],
    )
    cursor = connection.cursor()
    cursor.execute('SELECT datname FROM pg_catalog.pg_database')
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    for row in rows:
        name = row[0]
        if name != 'template0' and name != 'template1':
            os.system('pg_dump -CD -U postgres -f /home/backup/postgres/%s.sql %s' % (name, name))

    sys.exit()
