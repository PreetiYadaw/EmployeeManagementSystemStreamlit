import mysql.connector      #imported mysql.connector to connect to db
import streamlit as st      #imported streamlit and attributed as st
from streamlit_extras.switch_page_button import switch_page  #to switch b/w pages

def show_login():  #define login function
    st.subheader("Login Page")

# Establish a connection to MySQL Server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gunjan@091099",
    database="emp_management"
)
# Create a cursor object to interact with the database
#cursoris a pointer to the db
cursor = mydb.cursor()
# Streamlit configuration
st.set_page_config(page_title="Employee Management System")  #page nav bar/title/extreme upper left

def  login():
    st.text_input("User Name:", key="user_name", placeholder="User Name",value="admin")
    st.text_input("Password:", key="password", type="password", placeholder="Password")
    login_btn = st.button("Login")

    if login_btn:
        user_name = st.session_state.user_name
        password = st.session_state.password
        # Add your authentication logic here using the database
        if user_name == "admin" and password == "password":
            st.success("Logged In")
            st.session_state['Logged_Username'] = user_name
            st.session_state['User_Role'] = "HR admin"
            switch_page("Home")
        else:
            st.error("Incorrect Username or Password")

def login_auth():
    if 'Logged_Username' not in st.session_state:
        st.subheader("Login")
        login()
    else:
        st.success("You are already logged in")

if 'Logged_Username' in st.session_state:
    col1, col2 = st.columns(2)
    with col1:
        st.write("Hello", st.session_state.Logged_Username, "(", st.session_state.User_Role, ")")
    with col2:
        logout = st.button("Logout")
        if logout:
            del st.session_state.Logged_Username
            del st.session_state.User_Role
            st.success("Logged Out Successfully")
            switch_page("Home")

st.title("Welcome to Employee Management System")
login_auth()

gif_url = "https://www.ringcentral.com/us/en/blog/wp-content/uploads/2020/07/Blog_How_to_Build_a_Great_Workplace_Experience_Social_Card_01-1.gif"
st.image(gif_url, width=700)
st.markdown("“Great things in business are never done by one person. They’re done by a team of people.”")