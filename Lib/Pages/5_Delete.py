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
# gif_url = ""
# st.image(gif_url, width=300)

# Created a cursor object to interact with the database
cursor = mydb.cursor()

st.header(" ")
if 'Logged_Username' not in st.session_state:
    switch_page('Login')
else:
    st.success("Delete Employee Details")
def show():
    # Page content goes here

    col3 = st.columns(2)
    emp_id = col3[0].text_input("Enter Employee ID")

    if st.button("☠️Delete Employee"):
        with st.spinner("Removing employee..."):
            query = "DELETE FROM emp_management.empdata WHERE id = %s"
            values = (emp_id,)
            cursor.execute(query, values)
            mydb.commit()
            time.sleep(0)

        if cursor.rowcount == 1:
            st.success("Employee removed successfully.")
            st.snow()
        else:
            st.error("Employee not found.")



show()

gif_url = "https://www.mazzeschi.it/mazzeschi-asiadesk/wp-content/uploads/2020/10/Untitled-design-7.gif"
st.image(gif_url, width=600)