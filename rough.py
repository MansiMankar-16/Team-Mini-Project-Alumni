'''import datetime

today = datetime.date.today()
print(today.strftime("%d/%m/%Y"))'''

import sqlite3

def print_all_data(db_file, table_name):
    """Prints all data from a specified table in a SQLite database.

    Args:
        db_file (str): The path to the SQLite database file.
        table_name (str): The name of the table to query.
    """

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Fetch all rows from the table
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Print the column names
    column_names = [description[0] for description in cursor.description]
    print(column_names)

    # Print the data
    for row in rows:
        print(row)

    conn.close()

# Example usage:
db_file = 'students.db'  # Replace with your database file name
table_name = 'students'  # Replace with your table name

print_all_data(db_file, table_name)

