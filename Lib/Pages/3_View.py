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

st.header(" ")
if 'Logged_Username' not in st.session_state:
    switch_page('Login')
else:
    st.success("View All Employees")

def search_employee():
    # Page content goes here
    st.subheader("Search Employee")

    emp_id = st.text_input("Enter Employee ID")

    if st.button("Search"):
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
        else:
            st.warning("Employee not found.")

def view_all_employees():
    # Page content goes here

    query = "SELECT * FROM empdata"
    cursor.execute(query)
    employees = cursor.fetchall()

    if employees:
        with st.spinner("Loading employees..."):
            # Prepare the data for the table
            table_data = [["ID", "Name", "Salary", "Designation"]]  # Add column headings

            for employee in employees:
                emp_id, name, salary, designation = employee
                table_data.append([emp_id, name, salary, designation])

            st.table(table_data)  # Display the table without indexes
    else:
        st.info("No employees found.")


# Main script

option = st.radio("Select an option", ("Search Employee", "View All Employees"))

if option == "Search Employee":
    search_employee()
elif option == "View All Employees":
    view_all_employees()

# Close the database connection



gif_url = "https://e-registration.bhic.com.my/eregistration/eleave/sysbootstrap/dist/img/ani3.gif"
st.image(gif_url, width=300)