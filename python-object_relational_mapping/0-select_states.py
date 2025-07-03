#!/usr/bin/python3
import MySQLdb
import sys

def get_states(username, password, dbname):
    try:
        # Connect to server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch and display results
        results = cur.fetchall()
        for row in results:
            print(row)

        # Clean up
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"MySQL Error: {e}")


if __name__ == "__main__":
    get_states(sys.argv[1], sys.argv[2], sys.argv[3])