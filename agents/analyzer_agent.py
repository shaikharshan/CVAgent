from typing import Dict, Any
from agents.baseagent import BaseAgent
from utils.helper_functions import readPDF

class AnalyzerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Analyzer",
            instructions="""

            You are an AI assistant designed to extract key structured information from a candidate's resume. 
Your goal is to accurately and concisely extract the following elements:
            CV_text:{CV_text}

1. **Technical Skills**: Provide a bullet point list of technical skills mentioned (e.g., programming languages, tools, frameworks).
2. **Years of Experience**: Provide a single numeric value (approximate if not clearly mentioned).
3. **Education Level**: Mention the highest level of education attained (e.g., Bachelor's in Computer Science).
4. **Experience Level**: Categorize into one of the following: Junior / Mid-level / Senior based on role and total experience.
5. **Key Achievements**: Summarize 2–3 impactful accomplishments or responsibilities (avoid generic job duties).
6. **Domain Expertise**: Specify any domains/industries the candidate has worked in (e.g., FinTech,
Only use the information from the given resume. Do NOT add any assumptions or generalizations. Return the result in the specified bullet format. Do not return JSON or prose.
            """,
            input_variables=["CV_text"]
        )

    def run(self, CV_text:dict[str:str]) -> str | Dict[str, Any]:
        """Analyze the extracted resume data using LangChain"""
        print("🔍 Analyzer (LangChain): Analyzing candidate profile")
        

        # Run the chain with the resume content
        result = super().run(CV_text)

        # Ensure fallback if something breaks
        if "error" in result:
            return {
                "error": {
                    "technical_skills": [],
                    "years_of_experience": 0,
                    "education": {"level": "Unknown", "field": "Unknown"},
                    "experience_level": "Junior",
                    "key_achievements": [],
                    "domain_expertise": [],
                },
                "analysis_timestamp": "2024-03-14",
                "confidence_score": 0.5
            }
        
        return result
    

   
