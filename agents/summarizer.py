from typing import Dict, Any
from agents.baseagent import BaseAgent

class SummarizerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Summarizer",
            instructions="""
           You will be given a job description. Your task is to extract ONLY the details mentioned in the text.
Extract and format the output as follows:
    JD_text:{JD_text}

1. Job Role / Title  
2. Required Technical Skills (only if explicitly mentioned)  
3. Minimum Years of Experience Required (only if explicitly stated)  
4. Educational Qualifications  
5. Job Responsibilities (summarized using original words)  
6. Preferred Domain Expertise (only if mentioned)  
7. Other Key Requirements or Notes (include only what's in the text)

Only use the information from the given job description. Do NOT add any assumptions or generalizations. Return the result in the specified bullet format. Do not return JSON or prose.
    """,
    input_variables=["JD_text"]
        )

    def run(self, JD_text: dict[str:str]) ->  str | Dict[str, Any]:
        """Summarize JD using agent"""
        print(" Summarizing uploaded JD...")
        

        # Run the chain with the resume content
        result = super().run(JD_text)

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

   
