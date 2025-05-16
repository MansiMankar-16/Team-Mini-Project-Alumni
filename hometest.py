import sqlite3
from place_holder import login_hold_fetch,db_type_read
db_type_read()

def get_name_by_email( email):
  conn = sqlite3.connect("alumni.db")
  cursor = conn.cursor()

  cursor.execute("SELECT alumni_name FROM alumni WHERE al_email=?", (email,))
  result = cursor.fetchone()

  conn.close()
  if result!=None:

    return result
  else:
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT student_name FROM students WHERE email=?", (email,))
    result = cursor.fetchone()

    conn.close()
    return result

# Example usage:
db_file = "alumni.db"


