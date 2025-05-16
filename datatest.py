import streamlit as st
import sqlite3
from place_holder import db_type_write,login_hold_edit
import datetime
def pagefun():
    homePage=st.Page(
    page="views/home.py",
    title="Home Page",
        default=True
    )

    searchPage=st.Page(
        page="views/search.py",
        title="Search"
    )

    postPage=st.Page(
        page="views/post.py",
        title="Post"
    )

    profilePage=st.Page(
        page="views/profile.py",
        title="My Profile"
    )

    # navigation
    pg=st.navigation(pages=[homePage,searchPage,postPage,profilePage])
    pg.run()

def loginPage():
    st.title("Welcome To Alumni Website")
    column1,column2=st.columns(2,gap="large")
    with column1:
        emaillog=st.text_input("Email")
        passwordlog=st.text_input("passord")
        if st.button("login"):
            def check_student_exists(conn,emaillog , passwordlog):
                """Checks if a student exists in the database based on name and email.

                Args:
                    conn: A SQLite database connection.
                    student_name: The student's name.
                    email: The student's email address.

                Returns:
                    True if the student exists, False otherwise.
                """

                cursor = conn.cursor()
                cursor.execute("SELECT * FROM students WHERE email=? AND password=?", (emaillog, passwordlog))
                result = cursor.fetchone()
                return result is not None
            def check_alumni_exists(conn,emaillog , passwordlog):
            
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM alumni WHERE al_email=? AND al_password=?", (emaillog, passwordlog))
                result = cursor.fetchone()
                return result is not None

            # Connect to the database
            conn = sqlite3.connect('students.db')
            all_conn=sqlite3.connect("alumni.db")
            # Check if the student exists
            if check_student_exists(conn, emaillog, passwordlog):
                login_hold_edit(emaillog,passwordlog)
                db_type_write("students.db")
                st.write("welcome to login")
                st.session_state.user_input="user_input"
            elif check_alumni_exists(all_conn,emaillog,passwordlog):
                login_hold_edit(emaillog,passwordlog)
                db_type_write("alumni.db")
                st.write("welcome to login")
                st.session_state.user_input="user_input"        
            else:
                st.write("Wrong email or password")
                

            # Close the database connection
            conn.close()
    
    with column2:        
        # Initialize session state for managing navigation
        if "current_page" not in st.session_state:
            st.session_state.current_page = "home"  # Default to the home page

        # Function to switch to the "Join as" options page
        def show_join_options():
            st.session_state.current_page = "join_options"

        # Function to show the student form
        def show_student_form():
            st.session_state.current_page = "student_form"

        # Function to show the alumni form
        def show_alumni_form():
            st.session_state.current_page = "alumni_form"

        # Home Page
        if st.session_state.current_page == "home":
            #st.write("Click 'Join' to get started.")
            
            # Button to go to the join options
            if st.button("Join"):
                show_join_options()

        # Join Options Page
        elif st.session_state.current_page == "join_options":
            st.title("Join as...")
            st.write("Please select one of the options below:")
            
            # Option to join as alumni
            if st.button("Join as Alumni"):
                show_alumni_form()

            # Option to join as student
            if st.button("Join as Student"):
                show_student_form()

        # Student Form Page
        elif st.session_state.current_page == "student_form":
            st.title("Student Registration Form")
            st.write("Please fill out the form below with your basic details.")
            
            # Form for student details
            with st.form("student_form"):
                student_name = st.text_input("Full Name")
                dob = st.date_input("Date of Birth",datetime.date(2000, 1, 1))
                email = st.text_input("Email Address")
                phone = st.text_input("Phone Number (Optional)")
                course = st.text_input("Course/Program (e.g., B.tech., B.A., M.Sc., etc.)")
                department = st.text_input("Department/Faculty")
                graduation_year = st.number_input("Graduation Year", min_value=1900, max_value=2100, step=1)
                password=st.text_input("Password")
                
                # Image upload option
                #profile_image = st.file_uploader("Upload Profile Image", type=["jpg", "jpeg", "png"])
                
                # Submit button
                if st.form_submit_button("Submit"):
                    # Assuming you have retrieved data from your UI and stored them in variables

                    connection = sqlite3.connect("students.db")  # Connect to the database

                    cursor = connection.cursor()
                    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                           
                                    student_name TEXT,
                                    dob DATE,
                                    email TEXT,
                                    phone TEXT,
                                    course TEXT,
                                    department TEXT,
                                    graduation_year INTEGER,
                                    password TEXT
                                   
                                   )                                  
                        ''')
                    

                    sql = """
                        INSERT INTO students (student_name, dob, email, phone, course, department,graduation_year,password)
                        VALUES (?, ?, ?, ?, ?, ?,?,?)
                    """
                    #profile_image=profile_image.read()
                    data = (student_name,dob,email,phone,course,department,graduation_year,password)

                    cursor.execute(sql, data)

                    connection.commit()  # Save changes to the database

                    connection.close()  # Close the connection
                    st.success(f"Thank you, {student_name}! Your student details have been submitted.")
                    
                    

        # Alumni Form Page
        elif st.session_state.current_page == "alumni_form":
            st.title("Alumni Registration Form")
            st.write("Please fill out the form below with your basic alumni details.")
            
            # Form for alumni details
            with st.form("alumni_form"):
                alumni_name = st.text_input("Full Name")
                al_email=st.text_input("Email")
                al_dob=st.date_input("Date of Birth",datetime.date(2000, 1, 1))
                graduation_year = st.number_input("Graduation Year", min_value=1900, max_value=2100, step=1)
                degree_program = st.text_input("Degree Program (e.g., B.A., M.Sc., etc.)")
                department = st.text_input("Department/Faculty")
                current_job_title = st.text_input("Current Job Title")
                location = st.text_input("Location (City, Country)")
                linkedin = st.text_input("LinkedIn Profile (Optional)")
                al_password=st.text_input("passwordd")
                
                # Image upload option
                #profile_image = st.file_uploader("Upload Profile Image", type=["jpg", "jpeg", "png"])
                
                # Submit button
                if st.form_submit_button("Submit"):
                    al_connection=sqlite3.connect("alumni.db")
                    al_cursor=al_connection.cursor()
                    al_cursor.execute('''CREATE TABLE IF NOT EXISTS alumni (
                           
                                    alumni_name TEXT,
                                    al_email TEXT,
                                    al_dob DATE,    
                                    graduation_year INTEGER,
                                    degree_program TEXT,
                                    department TEXT,
                                    current_job_title TEXT,
                                    location TEXT,
                                    linkedin TEXT,
                                    al_password TEXT
                                   )                                  
                        ''')
                    al_sql = """
                        INSERT INTO alumni (alumni_name, al_email, al_dob, graduation_year, degree_program, department,
                          current_job_title, location,linkedin,al_password)
                        VALUES (?, ?, ?, ?, ?, ?,?,?,?,?)
                    """
                    al_data=(alumni_name,al_email,al_dob,graduation_year,degree_program,department,current_job_title,
                             location,linkedin,al_password)
                    al_cursor.execute(al_sql,al_data)
                    al_connection.commit()
                    al_connection.close()



                    st.success(f"Thank you, {alumni_name}! Your alumni details have been submitted.")
                    
               
    


if __name__=="__main__":
    if "user_input" not in st.session_state:
        loginPage()
    else:
        pagefun()


   
 
