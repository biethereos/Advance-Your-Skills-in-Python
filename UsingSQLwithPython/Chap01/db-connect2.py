#!/usr/bin/env python3
# Copyright 2021 Hung Nguyen
# as of 2021-29-09

import mysql.connector as mysql

def main():
    db = mysql.connect(host='localhost', user='root', password='*********')    
    cur = db.cursor()

    cur.execute('SELECT VERSION()')
    version = cur.fetchone()[0]
    print(f'MYSQL version {version}')

    cur.close()
    db.close()

if __name__ == '__main__':
    main()
