import streamlit as st
from utils.DB_utils import connect_db
import datetime

# -- Helper Functions --
def get_applied_jobs(user_id: int):
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT Job.*,Application.applied_at FROM Job
                INNER JOIN Application ON Job.jobid = Application.jobid
                WHERE Application.userid = ?
            """, (user_id,))
            return cursor.fetchall()
    except Exception as e:
        return []

def get_unapplied_jobs(user_id: int):
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM Job
                WHERE jobid NOT IN (
                    SELECT jobid FROM Application WHERE userid = ?
                )
            """, (user_id,))
            return cursor.fetchall()
    except Exception as e:
        return []

def getAlljobs():
        try:
            with connect_db() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM Job
                """)
                return cursor.fetchall()
        except Exception as e:
            return []

# -- Streamlit User Page --
def user_page():
    st.set_page_config(page_title="User Dashboard", layout="wide")
    
    # Check session
    if "user" not in st.session_state or st.session_state["user"]["role"] != "user":
        st.warning("Unauthorized access.")
        st.stop()

    user = st.session_state["user"]
    # st.sidebar.title(f"👋 Hello, {user['username']}!")

    # Applied Jobs in sidebar
    st.sidebar.subheader("📌 Applied Jobs")
    applied_jobs = get_applied_jobs(user["id"])
    if applied_jobs:
        for job in applied_jobs:
            with st.sidebar.expander(f"**Role**: {job[2]}"):
                st.markdown(f"**Company**: {job[1]}")
                st.markdown(f"**Salary**: {job[6]}")
                st.markdown(f"**Applied On**: {job[8]}")
    else:
        st.sidebar.info("No jobs applied yet.")

    # Greeting
    st.title(f"Welcome {user['username']} 👋")
    st.write("Here are the available job listings. Apply to any job you like!")

    # Show Unapplied Jobs
    unapplied_jobs = get_unapplied_jobs(user["id"])
    
    if not unapplied_jobs:
        st.info("🎉 You have applied to all available jobs.")
    else:
        cols = st.columns(2)
        for idx, job in enumerate(unapplied_jobs):
            with cols[idx % 2]:
                with st.container():
                    st.subheader(job[2])  # Role
                    st.caption(job[1])
                    st.markdown(f"**Description:** {job[3][:50]}...")  # JD
                    st.markdown(f"**Skills Required:** {job[4]}")
                    st.markdown(f"**Openings:** {job[5]}")
                    st.markdown(f"**Salary:** ₹{job[6]}")
                    
                    if st.button(f"Apply to {job[2]}", key=f"apply_{job[0]}"):
                        st.session_state["selected_job_id"] = job[0]
                        st.switch_page("pages/app.py")

    st.caption("🔚 Logout?")
    if st.button("Logout"):
        st.session_state.clear()
        st.switch_page("try.py")

user_page()
