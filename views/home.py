import streamlit as st
import sqlite3
from hometest import get_name_by_email
def display_posts(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("SELECT title, content, post_email, date_of_post FROM posts")
    posts = cursor.fetchall()

    for title, content, email, date in posts:
        st.write(f"**{title}**")
        st.write(f"{content}")
        name=get_name_by_email(email)[0]
        st.write(f"By: {name} on {date}")
        st.write("---")

    conn.close()

display_posts("posts.db")
