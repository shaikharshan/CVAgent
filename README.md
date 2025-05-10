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

🚀 How to Run This Project Locally
Follow these steps to run the CVAgent application on your local machine. This project uses Streamlit for frontend, LangChain agents, and Ollama for local LLM inference (e.g., Mistral 7B).

⚠️ Make sure your system has at least 8GB RAM to support the Ollama model.

📦 Step 1: Clone the Repository
```bash
git clone https://github.com/<your-username>/CVAgent_Accenture_Submission.git
cd CVAgent_Accenture_Submission
```
📌 This command copies the project to your local system and navigates into the project directory.

🧠 Step 2: Install Python Dependencies
Make sure you have Python 3.9+ installed. Then, install the required libraries:

```bash

pip install -r requirements.txt
```
📌 This installs all necessary Python packages like streamlit, langchain, pypdf, sqlite3, etc.

🧠 Step 3: Install and Start Ollama (for LLM Inference)
Install Ollama (if not already installed):

bash
Copy
Edit
curl -fsSL https://ollama.com/install.sh | sh
Then, start the Ollama server:

```bash

ollama serve
```
📌 Ollama runs the local LLM models (like Mistral 7B) used by LangChain agents.

🤖 Step 4: Pull the Required LLM Model
Pull the Mistral model locally using:

```bash
ollama pull mistral
```
📌 This downloads the Mistral 7B model needed for job and resume analysis.

🎮 Step 5: Run the Application
Now, launch the Streamlit app:

```bash
streamlit run app.py
```
📌 This starts the frontend of the application. A browser window will open at http://localhost:8501.

🧪 Step 6: Test the Workflow
Signup/Login as admin to add job descriptions.

Login as user to view jobs and upload resume PDFs.

Backend agents will analyze resumes, match to job descriptions, and generate interview emails.

🗃️ (Optional) Reset or Inspect the Database
The app uses SQLite located at:

```
db/CVAgentDB.db
```
You can explore or modify it using tools like DB Browser for SQLite.

🛠️ Troubleshooting
If you face issues with ollama, ensure you're using the latest version and your system meets hardware requirements.

If models fail to load, verify you ran ollama serve and pulled mistral successfully.
