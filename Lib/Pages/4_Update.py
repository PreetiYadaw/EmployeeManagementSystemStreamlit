import mysql.connector
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Establish a connection to MySQL Server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gunjan@091099",
    database="emp_management"
)

# Create a cursor object to interact with the database
cursor = mydb.cursor()

def show():
    # Page content goes here

    emp_id = st.text_input("Enter Employee ID")

    if st.checkbox("📝 Update Employee Details"):
        query = "SELECT * FROM empdata WHERE id = %s"
        values = (emp_id,)
        cursor.execute(query, values)
        employee = cursor.fetchone()

        if employee:
            st.write("Employee details:")
            st.write("ID:", employee[0])
            st.write("Name:", employee[1])
            st.write("Salary:", employee[2])
            st.write("Designation:", employee[3])
            st.write("Update employee details:")

            new_name = st.text_input("New Name", value=employee[1])
            new_salary = st.text_input("New Salary", value=employee[2])
            new_designation = st.text_input("New Designation", value=employee[3])

            if st.button("Update"):
                update_query = "UPDATE emp_management.empdata SET name = %s, salary = %s, designation = %s WHERE id = %s"
                update_values = (new_name, new_salary, new_designation, emp_id)
                cursor.execute(update_query, update_values)
                mydb.commit()

                if cursor.rowcount > 0:
                    st.success("Employee updated successfully.")
                    st.balloons()
                else:
                    st.error("Failed to update employee details.")
        else:
            st.warning("Employee not found.")
st.header(" ")
if 'Logged_Username' not in st.session_state:
    switch_page('Login')
else:
    st.success("Update Employee Details")
# Display the "Update Employee" section
show()

# Close the database connection
mydb.close()

# Display the GIF at the bottom of the main frame
gif_url = "https://www.aou.edu.om/units/hr/PublishingImages/Pages/default/hr-g.gif"  # Replace with your GIF URL
st.image(gif_url, width=300)