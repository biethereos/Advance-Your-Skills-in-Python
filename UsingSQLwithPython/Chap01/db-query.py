#!/usr/bin/env python3
# Copyright 2021 Hung Nguyen
# db-query.py as of 2021-09-29

import sqlite3


def main():
    db = sqlite3.connect("../db/scratch.db")
    cur = db.cursor()

    cur.execute("DROP TABLE IF EXISTS temp")
    cur.execute("CREATE TABLE IF NOT EXISTS temp ( a TEXT, b TEXT, c TEXT )")
    cur.execute("INSERT INTO temp VALUES ('one', 'two', 'three')")
    cur.execute("INSERT INTO temp VALUES ('four', 'five', 'six')")
    cur.execute("INSERT INTO temp VALUES ('seven', 'eight', 'nine')")
    db.commit()

    cur.execute("SELECT * FROM temp")
    #1.
    # row = cur.fetchone()
    # while row:
    #     print(row)
    #     row = cur.fetchone()
    #2.
    rows = cur.fetchall()
    for row in rows:
        print(row)
    #3.
    # for row in cur:
    #     print(row)

    cur.execute("DROP TABLE IF EXISTS temp")
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
