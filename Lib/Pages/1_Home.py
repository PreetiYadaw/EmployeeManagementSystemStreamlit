import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.header(" ")
if 'Logged_Username' not in st.session_state:
    switch_page('Login')
else:
    st.success("Welcome to Employee Management System")

gif_url = "https://www.iowaemploymentlawblog.com/wp-content/uploads/sites/829/2020/03/source.gif"
st.image(gif_url, width=300)