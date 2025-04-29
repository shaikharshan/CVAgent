from typing import Dict, Any
from agents.baseagent import BaseAgent

class MatcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Matcher",
            instructions="""
          You are a recruiting assistant tasked with evaluating how well a candidate matches a job description.
You will be provided with two structured documents:
A Candidate CV Summary
A Job Description Summary

CV = {CV}
JD = {JD}
Based on the information, do the following:
Calculate a Match Score out of 100, giving higher weight to:
Skill overlap (40%)
Relevant years of experience (20%)
Education level (10%)
Domain expertise (20%)
Certifications & achievements (10%)
Provide a short explanation (2–3 sentences) of how this score was derived.
Make a recommendation:
Proceed strictly only if the score is 80 or above
Reject if the score is below 80

Respond in the following JSON format:
{{
"Match_Score": <score>/100
"Recommendation": <Proceed to Interview / Reject>
"Reason": <concise explanation>
}}

    """,
    input_variables=["JD","CV"]
        )

    def run(self, input:dict[str:str]) ->  str | Dict[str, Any]:
        """Matches Candidate CV on JD provided"""
        print(" Matching CV with JD...")
        

        # Run the chain with the resume content
        result = super().run(input)

        # Ensure fallback if something breaks
        if "error" in result:
            return {
                "error": {
                    "Match_Score": "0",
            "Recommendation": "Reject",
            "Reason": "Error in processing your Resume. Reapplying might help..."
                }
            }
        
        return result

   
