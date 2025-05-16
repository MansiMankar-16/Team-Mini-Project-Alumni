import streamlit as st
import sqlite3
from place_holder import login_hold_fetch
import datetime



# Connect to the SQLite database
conn = sqlite3.connect('posts.db')
c = conn.cursor()

# Create the posts table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS posts
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT,
              content TEXT,
          post_email TEXT,date_of_post TEXT)''')
conn.commit()

def main():
    st.title("Simple Post Management App")

    # Add a post
    with st.form("add_post_form"):
        title = st.text_input("Enter post title")
        content = st.text_area("Enter post content")
        post_email,pw=login_hold_fetch()
        today = datetime.date.today()
        date_of_post=today.strftime("%d/%m/%Y")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            try:
                c.execute("INSERT INTO posts (title, content,post_email,date_of_post) VALUES (?, ?,?,?)", (title, content,post_email,date_of_post))
                conn.commit()
                st.success("Post added successfully!")
            except Exception as e:
                st.error(f"Error adding post: {str(e)}")

    # Display all posts
    st.header("All Posts")
    c.execute("SELECT * FROM posts WHERE post_email=?",(post_email,))
    posts = c.fetchall()

    if posts:
        for post in posts:
            st.write(f"**Post ID:** {post[0]}")
            st.write(f"**Title:** {post[1]}")
            st.write(f"**Content:** {post[2]}")

            # Update and delete options
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Edit", key=f"edit_{post[0]}"):
                    st.session_state[f"edit_id_{post[0]}"] = post[0]
                    st.session_state[f"edit_title_{post[0]}"] = post[1]
                    st.session_state[f"edit_content_{post[0]}"] = post[2]

            with col2:
                if st.button("Delete", key=f"delete_{post[0]}"):
                    try:
                        c.execute("DELETE FROM posts WHERE id = ?", (post[0],))
                        conn.commit()
                        st.warning("Post deleted successfully!")
                    except Exception as e:
                        st.error(f"Error deleting post: {str(e)}")

        # Edit post form
        for post in posts:
            if f"edit_id_{post[0]}" in st.session_state:
                with st.form(f"edit_post_form_{post[0]}"):
                    new_title = st.text_input("New Title", value=st.session_state[f"edit_title_{post[0]}"] if f"edit_title_{post[0]}" in st.session_state else "")
                    new_content = st.text_area("New Content", value=st.session_state[f"edit_content_{post[0]}"] if f"edit_content_{post[0]}" in st.session_state else "")
                    save_edit_button = st.form_submit_button("Save Edit")

                    if save_edit_button:
                        try:
                            c.execute("UPDATE posts SET title = ?, content = ? WHERE id = ?", (new_title, new_content, st.session_state[f"edit_id_{post[0]}"]))
                            conn.commit()
                            st.success("Post updated successfully!")
                            del st.session_state[f"edit_id_{post[0]}"]
                            del st.session_state[f"edit_title_{post[0]}"]
                            del st.session_state[f"edit_content_{post[0]}"]
                        except Exception as e:
                            st.error(f"Error updating post: {str(e)}")

main()