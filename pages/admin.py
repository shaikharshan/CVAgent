import streamlit as st
import sqlite3
from datetime import date
from utils.DB_utils import connect_db
import time


# Function to create a new user
def create_job(role: str,company:str ,JD: str, skills: str, openings: int, salary: str, user_id: int):
    try:
        with connect_db() as conn:
            cursor = conn.cursor()

            # Insert into Job table
            cursor.execute("""
                    INSERT INTO Job (role,company ,description, skills, openings, salary, created_by)
                    VALUES (?, ? ,?, ?, ?, ?, ?)
                """, (role,company ,JD, skills, openings, salary, user_id))

            conn.commit() 

        return True, "Job created successfully!"

    except sqlite3.IntegrityError:
        return False, "Job already exists."
    except Exception as e:
        return False, str(e)

def getJobs(userId: int):
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT jobid, role, salary, openings FROM Job WHERE created_by = ?
            """, (userId,))
            return cursor.fetchall()
    except Exception as e:
        return []





def admin_page():
    st.title("CVAgent")

    st.title("Welcome Admin")
    

    with st.form("create_job_form",clear_on_submit=True):
        company = st.text_input("Company Name")
        role = st.text_input("Role")
        JD = st.text_area("Write a descriptive JD for suitable matching with agents.. (at least 750 characters)", height=300)
        skills = st.text_input("Mention important skills required")
        openings = st.number_input("No. of openings", min_value=1)
        salary = st.text_input("Salary")
        submit = st.form_submit_button("Create Job")

    if submit:
        if not (company and role and JD and skills and openings and salary):
            st.warning("Please fill all fields.")
        elif len(JD) <= 750:
            st.warning("JD needs to be more descriptive.")
        elif st.session_state["user"]["role"] != "admin":
            st.warning("Access denied. Cannot create job.")
            time.sleep(2)
            st.switch_page("try.py")
        else:
            success, msg = create_job(role,company, JD, skills, openings, salary,st.session_state["user"]["id"])
            if success:
                st.success(msg)
                st.balloons()

            else:
                st.error("Error:" +msg)
    
    st.markdown("Add your jobs here..")
    # Sidebar - Show all jobs created by admin
    st.sidebar.subheader("Your Posted Jobs")

    jobs = getJobs(st.session_state["user"]["id"])

    if not jobs:
        st.sidebar.info("No jobs created yet.")
    else:
        for job in jobs:
            jobid, role, salary, openings = job
            with st.sidebar.expander(f"Job ID: {jobid}"):
                st.markdown(f"**Role**: {role}")
                st.markdown(f"**Salary**: {salary}")
                st.markdown(f"**Openings**: {openings}")


    st.caption("Logout?")
    if st.button("Home", key="logout_btn"):
        # Delete all the items in Session state
        for key in st.session_state.keys():
            del st.session_state[key]
        st.switch_page("try.py")

admin_page()