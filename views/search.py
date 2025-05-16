import sqlite3
import streamlit as st

def show_data(db_file, table):
    """Shows all data from a table in a SQLite database without using pandas."""
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        conn.close()
        return columns, rows
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return None, None

# Example:
alum=['alumni_name', 'al_email', 'al_dob', 'graduation_year', 'degree_program', 'department', 'current_job_title', 'location', 'linkedin']
student=['student_name', 'dob', 'email', 'phone', 'course', 'department', 'graduation_year']
def search_name(name):
    for data in ["alumni","students"]:
        cols, data = show_data(data+".db", data) #or alumni.db and alumni
        
        if cols and data:
              # Print column names
            for row in data:
                if row[0]==name:
                    if alum==cols[:-1]:
                        #print("alumni")
                        #print(cols[:-1])
                        #print(row[:-1]) # Print each row
                        return "alumni.db",row[:-1],cols[:-1]
                    else:
                        #print("student")
                        #print(cols[:-1])
                        #print(row[:-1])
                        return "students.db",row[:-1],cols[:-1]
                    break



la_name=st.text_input("Name")
if st.button("Search"):
    
    status,ro,col=search_name(la_name)
    #st.write(status)
    #st.write(ro)
    if status=="alumni.db":
   
        st.title("Statue: "+status[:-3])
        st.write("Name:            ",ro[0])
        st.write("Email:           ",ro[1])
        st.write("Date of Birth:   ",ro[2])
        st.write("Graduating Year: ",ro[3])
        st.write("Progrma:         ",ro[4])
        st.write("Department:      ",ro[5])
        st.write("Job Title:       ",ro[6])
        st.write("Location:        ",ro[7])
        st.write("Linkedin:        ",ro[8])
    elif status=="students.db":
         
         st.title("Statue: "+status[:-3])
         st.write("Name:            ",ro[0])
         st.write("Date of Birth:   ",ro[2])
         st.write("Email:           ",ro[1])
         st.write("Phone No:        ",ro[3])
         st.write("Course:          ",ro[4])
         st.write("Department:      ",ro[5])
         st.write("Graduation Yeat: ",ro[6])
    


