import mysql.connector
import time
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Established a connection to MySQL Server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gunjan@091099",
    database="emp_management"
)

# Created a cursor object to interact with the database
cursor = mydb.cursor()

def show():
    # Page content goes here

    col2 = st.columns(2)
    emp_id = col2[0].text_input(" Add ID ")
    name = col2[1].text_input(" Add Name ")

    col2 = st.columns(2)
    salary = col2[0].text_input(" Add Salary")
    designation = col2[1].text_input(" Add Designation ")

    if st.button("✒️Add Employee Details"):
        with st.spinner("Loading employee..."):
            query = "INSERT INTO emp_management.empdata (id, name, salary, designation) VALUES (%s, %s, %s, %s)"
            values = (emp_id, name, salary, designation)
            cursor.execute(query, values)
            mydb.commit()
            time.sleep(0)

        st.success("Employee added successfully.")
        st.balloons()


st.header(" ")
if 'Logged_Username' not in st.session_state:
    switch_page('Login')
else:
    st.success("Add Employee Details")

show()

gif_url = "https://empxtrack.com/wp-content/uploads/2016/05/come_join_the_team_500_wht_10876.gif"
st.image(gif_url, width=300)