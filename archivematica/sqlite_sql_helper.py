#!/usr/bin/env python

"""
Helper script for running SQL command against SQLite database

e.g. python sqlite_sql_helper.py /path/to/transfers.db "DELETE FROM aip WHERE uuid=?" "683bd419-5467-4d41-878b-acc88e3edf74"

"""

import argparse
import os
import sqlite3

def _make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("db", help="Path to SQLite file")
    parser.add_argument("command", help="Command to run")
    parser.add_argument("value", help="Value to use in command")

    return parser

def main():

    parser = _make_parser()
    args = parser.parse_args()

    db = os.path.abspath(args.db)
    conn = sqlite3.connect(db)
    c = conn.cursor

    mydata = c.execute(args.command, (args.value,))
    conn.commit()
    c.close()

    return mydata
