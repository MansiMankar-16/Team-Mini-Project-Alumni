import sqlite3
import streamlit as st
from PIL import Image
from io import BytesIO

# Connect to the SQLite database
conn = sqlite3.connect("students.db")
c = conn.cursor()

# Fetch image data from the database
c.execute("SELECT profile_image FROM students")
images = c.fetchall()  # Fetch all rows
conn.close()

# Display the images in Streamlit
if images:
    for (image_blob,) in images:  # Extract the binary blob from each row
        # Convert binary data back to an image
        image = Image.open(BytesIO(image_blob))
        
        # Resize the image
        new_size = (200, 200)  # Specify the desired width and height
        resized_image = image.resize(new_size)
        
        # Display the resized image in Streamlit
        st.image(resized_image, caption="Student Profile", use_container_width=False)
else:
    st.write("No images found in the database.")
