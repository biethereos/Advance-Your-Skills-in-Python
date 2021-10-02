#!/usr/bin/env python3
# Copyright 2021 Hung Nguyen
# as of 2021-09-29

import mysql.connector as mysql

MY_HOST = 'localhost'
MY_USER = 'root'
MY_PASS = 'av.nt@$*19b$*'
MY_DATABASE = 'test'


def main():
    db = mysql.connect(host=MY_HOST, 
                        user=MY_USER, 
                        password=MY_PASS, 
                        database=MY_DATABASE)

    cur = db.cursor(prepared=True)

    cur.execute('DROP TABLE IF EXISTS temp')
    cur.execute('CREATE TABLE IF NOT EXISTS temp (a TEXT, b TEXT, c TEXT)')
    # cur.execute('INSERT INTO temp VALUES ("one", "two", "three")')
    # cur.execute('INSERT INTO temp VALUES ("four", "five", "six")')
    # cur.execute('INSERT INTO temp VALUES ("seven", "eight", "nine")')

    values = (
        ('one', 'two', 'three'),
        ('two', 'three', 'four'),
        ('three', 'four', 'five'),
        ('four', 'five', 'six'),
        ('five', 'six', 'seven'),
        ('six', 'seven', 'eight'),
        ('seven', 'eight', 'nine'),
        ('eight', 'nine', 'ten'),
        ('nine', 'ten', 'eleven')
    )

    insert_statment = 'INSERT INTO temp VALUES (?, ?, ?)'
    cur.executemany(insert_statment, values)

    cur.execute('SELECT * FROM temp')
    for row in cur:
        print(row)

    query = 'SELECT * FROM temp WHERE a = ?'
    cur.execute(query, ('four',))

    for row in cur:
        print(f'result is {row}')

    cur.execute('DROP TABLE IF EXISTS temp')

    cur.close()
    db.close()

if __name__== '__main__':
    main()