import streamlit as st
import sqlite3
import hashlib
from place_holder import db_type_read,login_hold_fetch
ctype=db_type_read()
if ctype=="students.db":
    def authenticate(email, password):
        # Connect to the database
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()

        # Hash the password for comparison

        cursor.execute("SELECT student_name, dob,email, phone, course, department, graduation_year FROM students WHERE email=? AND password=?", (email,password))
        user = cursor.fetchone()
        conn.close()

        return user

    def display_profile(user_data):
        st.write(f"name: {user_data[0]}")
        st.write(f"Date of Birth: {user_data[1]}")
        st.write(f"Email: {user_data[2]}")
        st.write(f"Phone: {user_data[3]}")
        st.write(f"Course: {user_data[4]}")
        st.write(f"Department: {user_data[5]}")
        st.write(f"Graduation Year: {user_data[6]}")

    def main():
        st.title("Student Profile Viewer")
        email,password=login_hold_fetch()
        user_data = authenticate(email, password)
        if user_data:
            display_profile(user_data)
        else:
            st.error("Invalid credentials")


    main()

elif(ctype=="alumni.db"):


    def authenticate(email, password):
        # Connect to the database
        conn = sqlite3.connect('alumni.db')
        cursor = conn.cursor()      

        cursor.execute("SELECT * FROM alumni WHERE al_email=? AND al_password=?", (email, password))
        user = cursor.fetchone()
        conn.close()

        return user

    def display_profile(user_data):
        st.write(f"Alumni Profile: {user_data[0]}")
        st.write(f"Email: {user_data[1]}")
        st.write(f"Date of Birth: {user_data[2]}")
        st.write(f"Graduation Year: {user_data[3]}")
        st.write(f"Degree Program: {user_data[4]}")
        st.write(f"Department: {user_data[5]}")
        st.write(f"Current Job Title: {user_data[6]}")
        st.write(f"Location: {user_data[7]}")
        st.write(f"LinkedIn: {user_data[8]}")

    def main():
        st.title("Alumni Profile Viewer")
        email,password=login_hold_fetch()
        user_data = authenticate(email, password)
        if user_data:
            display_profile(user_data)
        else:
            st.error("Invalid credentials")


    main()

else:
    st.write("not found")