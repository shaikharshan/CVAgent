import streamlit as st
import sqlite3
from datetime import date
import time
from utils.DB_utils import connect_db

# Function to create a new user
def create_user(username, password, email, phone, role):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        
        # Insert new user
        cursor.execute("""
            INSERT INTO User (username, password, email, phone, role)
            VALUES (?, ?, ?, ?, ?)
        """, (username, password, email, phone, role))
        
        conn.commit()
        conn.close()
        return True, "Signup successful!"
    
    except sqlite3.IntegrityError as e:
        return False, "Username or email already exists."
    except Exception as e:
        return False, str(e)

# Streamlit UI
def signup_page():
    st.title("CVAgent")  
    if st.button("Home"):
        st.switch_page("try.py")
    st.title("User Signup")

    with st.form("signup_form",clear_on_submit=True):
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        phone = st.text_input("Phone Number (10 digits)")
        role = st.selectbox("Register as", ["user", "admin"])

        submit = st.form_submit_button("Sign Up")

    if submit:
        if not (username and password and email and phone):
            st.warning("Please fill all fields.")
        elif len(phone) != 10 or not phone.isdigit():
            st.warning("Enter a valid 10-digit phone number.")
        else:
            success, msg = create_user(username, password, email, phone, role)
            if success:
                st.success(msg)
                st.balloons()
                time.sleep(3)
                st.switch_page("pages/login.py")
            else:
                st.error(msg)
    

    st.caption("Already signed up?")    
    if st.button("Go to Login Page"):
        st.switch_page("pages/login.py")
signup_page()
