import streamlit as st
import sqlite3
from datetime import date
import time
from utils.DB_utils import connect_db,getUser


# Login page
def login_page():
    st.title("CVAgent")

    if st.button("Home"):
        st.switch_page("try.py")

    st.title("Login")

    with st.form("login_form",clear_on_submit=True):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        role = st.selectbox("Login as", ["user", "admin"])

        submit = st.form_submit_button("Login")

    if submit:
        if not (password and email):
            st.warning("Please fill all fields.")
        else:
            result = getUser(email, password, role)
            if result and isinstance(result, tuple):
                # Store user info in session_state
                st.session_state["user"] = {
                    "id": result[0],
                    "username": result[1],
                    "email": result[2],
                    "role": result[4]
                }

                st.success("Login Successful")
                st.balloons()
                time.sleep(2)
                st.switch_page(f"pages/{role}.py")
            else:
                st.error("Please check your credentials again...")

    st.caption("Not registered yet?")
    if st.button("Go to Sign Up Page"):
        st.switch_page("pages/signup.py")

login_page()
