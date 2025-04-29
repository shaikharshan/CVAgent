from langchain_ollama.llms import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from typing import Dict, Any
import json


class BaseAgent:
    def __init__(self, name: str, instructions: str,input_variables:list):
        self.name = name
        self.instructions = instructions
        self.input_variables = input_variables
        self.llm = OllamaLLM(model="mistral:latest")

        # Setup LangChain prompt template
        self.prompt = PromptTemplate(
            input_variables=self.input_variables,
            template=f"""[INSTRUCTIONS]
                            {self.instructions}"""
        )

        # LLM Chain
        # self.chain = LLMChain(prompt=self.prompt, llm=self.llm)
        self.chain = self.prompt | self.llm

    def run(self, input: dict[str:str]) -> str:
        """Run the LLM chain with input and safely parse JSON from output"""
        try:
            response = self.chain.invoke(input)
            return response
        except Exception as e:
            return {"error": str(e)}

