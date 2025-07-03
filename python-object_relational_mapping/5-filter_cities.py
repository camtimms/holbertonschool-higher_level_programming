#!/usr/bin/python3
"""
Script that returns cities form the cities table
"""
import MySQLdb
import sys


def get_cities(username, password, dbname, state_name):
    """ Get all cities from cities db table"""
    try:
        # Connect to server (Use with for auto closing and management)
        with MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=dbname) as db:

            with db.cursor() as cur:
                cur.execute("SELECT cities.name "
                            "FROM cities "
                            "LEFT JOIN states ON states.id = cities.state_id "
                            "WHERE states.name LIKE BINARY %s "
                            "ORDER BY cities.id ASC", (state_name,))
                # Fetch and display results
                results = cur.fetchall()
                for i, row in enumerate(results):
                   print(row[0], end="")
                   if i < len(results) - 1:
                       print(", ", end="")
                print()

    except MySQLdb.Error as e:
        print(f"MySQL Error: {e}")


if __name__ == "__main__":
    get_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
