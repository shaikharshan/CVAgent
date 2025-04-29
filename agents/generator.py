from typing import Dict, Any
from agents.baseagent import BaseAgent

class GeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Generator",
            instructions= """
You are an AI assistant that drafts professional emails for recruitment decisions.

You will be provided with:
- Match Score
- Recommendation (Proceed to Interview or Reject)
- Reason (evaluation reasoning from the matcher agent)

Your job is to:
1. Write a professional email based on the recommendation.
2. If the recommendation is "Proceed to Interview", congratulate the candidate, notify them regarding further stages of recruitment (only if available) and let them know they will be contacted to schedule an interview. DO NOT MENTION REASON for selection.
3. If the recommendation is "Reject", politely inform the candidate, summarize and mention the reason and appreciate their interest.
4. Keep it formal, polite, and concise.
5. The email must end with a signature from the sender as **'CVAgent Team'**.

Output response must be in the following JSON format:
{{
    "subject":"<subject_line>",
    "body":"<email_body>"
}}

Here is the input:
Match Score: {score}/100  
Recommendation: {status}  
Reason: {reason}
Candidate_name:{name}
Candidate_role:{role}
"""
,
    input_variables=["score","reason","status","name","role"]
        )

    def run(self, input:dict[str:str]) ->  str | Dict[str, Any]:
        """Generates email based on input given"""
        print(" Generating email...")
        

        # Run the chain with the resume content
        result = super().run(input)

        # Ensure fallback if something breaks
        if "error" in result:
            return {
                "error": {
                   "Could not generate email..."
                }
            }
        
        return result

   
