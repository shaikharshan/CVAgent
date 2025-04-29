import streamlit as st

st.set_page_config(page_title="CVAgent", layout="centered")


st.sidebar.markdown("Signup/Login to explore job postings.")
st.write("""
#  Welcome to **CVAgent**   👋
Your intelligent job matchmaking companion!

---

🎯 **Find your perfect job** effortlessly with our Multi-AI agentic resume matching system. Whether you're a **fresher** or a **seasoned pro**, CVAgent helps you discover and apply to jobs that truly fit your skills and goals.

---

🚀 **Why CVAgent?**

- ✅ Explore **curated job listings** from top companies  
- 🔁 Avoid duplicate applications with smart **application tracking**  
- 📊 Get a **personalized dashboard** to monitor your job journey  
- 🧠 Coming soon: **AI-powered job recommendations** based on your resume!

---

💡 Let your **skills shine**, and we’ll take care of the matchmaking.  
Get started now and take one step closer to your dream job!
""")


st.sidebar.page_link("pages/signup.py", label="Sign Up")
st.sidebar.page_link("pages/login.py", label="Login")

