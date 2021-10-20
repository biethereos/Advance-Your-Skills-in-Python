#!/usr/bin/env python3
# Copyright 2021 Hung Nguyen
# as of 2021-29-09

import psycopg2 as pg

def main():
    db = pg.connect(host='localhost', user='postgres', password='*******')
    cur = db.cursor()

    cur.execute('SELECT version()')
    version = cur.fetchone()[0]
    print(f'PostgreSQL version {version}')

    cur.close()
    db.close()

if __name__ == '__main__':
    main()