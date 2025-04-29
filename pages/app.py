from utils.helper_functions import readPDF, convert_to_json
from agents.analyzer_agent import AnalyzerAgent
from agents.summarizer import SummarizerAgent
from agents.matcher import MatcherAgent
from agents.generator import GeneratorAgent
from email_service import EmailService
from utils.DB_utils import connect_db
import streamlit as st
import time
import os

# Database operation to store application
def store_application(user_id, job_id,CV_path):
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Application (userid,jobid,resume) VALUES (?, ?, ?);", (user_id, job_id,CV_path))
            appId = cursor.lastrowid
            conn.commit()
        return appId
    except Exception as e:
        st.error(f"❌ Failed to store application: {e}")
        return None

# Retrieve job details
def getJob(jobId: int):
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Job WHERE jobid=?;", (jobId,))
            return cursor.fetchone()
    except Exception as e:
        return None
      
def updateApplication(status:str,appId):
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE APPLICATION SET status=? WHERE applicationid=?;", (status,appId,))
        return True,"Updated successfully"
    except Exception as e:
        return False,str(e)

# Main app function
def application_page():
    st.set_page_config(page_title="Apply Page", layout="wide")

    if "user" not in st.session_state or st.session_state["user"]["role"] != "user":
        st.warning("Unauthorized access.")
        st.stop()

    user = st.session_state["user"]
    if "selected_job_id" not in st.session_state:
        st.warning("No job selected.")
        st.stop()

    job_id = st.session_state["selected_job_id"]
    job = getJob(job_id)

    st.sidebar.subheader("Job Details")
    if job:
        st.sidebar.subheader(job[2])  # Job role
        st.sidebar.caption(job[1])    # Company
        st.sidebar.markdown(f"**Description:** {job[3]}")
        st.sidebar.markdown(f"**Skills Required:** {job[4]}")
        st.sidebar.markdown(f"**Openings:** {job[5]}")
        st.sidebar.markdown(f"**Salary:** ₹{job[6]}")
    else:
        st.sidebar.info("No such job exists.")

    # Greeting
    st.title(f"👋 Welcome {user['username']}")
    st.write("Please upload your **PDF resume** below to apply for this position.")

    uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

    if uploaded_file:
        with st.spinner("Reading your resume..."):
            # Save file temporarily
            file_path = os.path.join("temp_resumes", uploaded_file.name)
            os.makedirs("temp_resumes", exist_ok=True)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())

            # Process Resume
            pdf_text = readPDF(file_path)
            analyzer = AnalyzerAgent()
            formatted_CV = analyzer.run({"CV_text": pdf_text})

            summarizer = SummarizerAgent()
            job_text = f"""
            Job Title: {job[2]}
            Description: {job[3]}
            Skills: {job[4]}
            """
            print(job_text)
            formatted_JD = summarizer.run({"JD_text": job_text})

            matcher = MatcherAgent()
            match_data = matcher.run({"CV": formatted_CV, "JD": formatted_JD})
            json_data = convert_to_json(match_data)

 

            generator = GeneratorAgent()
            email_content = generator.run({
                "score": json_data["Match_Score"],
                "status": json_data["Recommendation"],
                "reason": json_data["Reason"],
                "name":user["username"],
                "role":user["role"]
            })

            email_json = convert_to_json(email_content)


            # Send Email
            email_service = EmailService("arshan5446@gmail.com") 
            email_success = email_service.send_email(
                user["email"],
                email_json["subject"],
                email_json["body"]
            )

            # Store Application
            appId = store_application(user["id"], job_id,file_path)
            if("Reject" in json_data["Recommendation"]):
                updateApplication("Rejected",appId=appId)
            else:
                updateApplication("Accepted",appId=appId)

            st.success("🎉 Your application has been successfully submitted!")
            if email_success:
                st.info(f"📧 A confirmation email has been sent to **{user['email']}**.")
            else:
                st.warning("⚠️ Email could not be sent.")

            # Redirect to jobs page
            st.info("Redirecting to jobs page in 5 seconds...")
            time.sleep(5)
            st.switch_page("pages/user.py")  
    if st.button("Back",key="back_btn"):
        st.switch_page("pages/user.py")

# Run page
application_page()
