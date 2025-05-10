Developed a full-stack AI-powered job screening platform using Streamlit and LangChain agents. 

Designed agents to analyze resumes, summarize job descriptions, and calculate candidate-job fit using a match score. 

Integrated automated email generation and scheduling using custom prompt templates. 

Deployed mock front-end for demo and tested local Ollama-based models including Mistral.

Tools & technologies used: Python, Streamlit, LangChain, SQLite, Ollama (Mistral), SMTP, LLM Agents

Presentation : https://docs.google.com/presentation/d/1MIA7VF7xmfrFo24zmRlJ4yo1plvaoE64KccbnPWX4V0/edit#slide=id.g34af3b0cb99_0_26

Demo video: https://drive.google.com/file/d/1RmZS3RGDTtUkGTwwLUaZ9iC1iEYttHo_/view

UI overview:
![79fc5471-89c4-4622-9150-0623aba83a14](https://github.com/user-attachments/assets/f3d32021-73b8-45cb-a11e-cb0a54a0f043)

![abece861-a663-44c7-a46d-9fe1d3f22b23](https://github.com/user-attachments/assets/ad8cb038-2d8f-4c7e-bca2-83ad794d70f0)

![ba86cefd-281d-405e-af00-435370cd336e](https://github.com/user-attachments/assets/22a596b1-6110-42d5-ab06-9eee0f036987)

## 🚀 How to Run This Project Locally

🚀 How to Run the Project Locally
Follow these steps to set up and run the full CVAgent application on your local machine:

1. Clone the Repository

git clone https://github.com/shaikharshan/CVAgent_Accenture_Submission.git
cd CVAgent_Accenture_Submission

2. Install Python Dependencies
Ensure you have Python 3.9+ installed. Then, install the required libraries:

pip install -r requirements.txt

3. Install and Set Up Ollama (for LLM Inference)
If you haven’t installed Ollama yet:

curl -fsSL https://ollama.com/install.sh | sh
Once installed, start the Ollama service:


ollama serve
Then pull the required model (e.g., Mistral):


ollama pull mistral
4. Start the Application
In your terminal, run:


streamlit run app.py
This will launch the app in your browser at: http://localhost:8501

5. Set Up the SQLite Database (First-Time Only)
On first launch, the app will automatically create the SQLite DB (db/CVAgentDB.db) and required tables.

To seed jobs or users manually, use the Admin panel or directly via SQLite browser.

6. Login Credentials (Sample)
Admin email: admin@example.com

Admin password: admin123

Or sign up via the Sign Up page

🧠 Optional Notes
Ollama models are served locally — ensure your system has at least 8GB RAM for Mistral

Email functionality uses SMTP — configure credentials in email_service.py if needed
