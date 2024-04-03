# service/openAi_service.py
from openai import OpenAI
from dotenv import load_dotenv
import os
import time
import logging

load_dotenv()

MODEL = "gpt-3.5-turbo-0125"

__all__ = ["OpenAIService"]

class OpenAIService:
    client: OpenAI = None

    def __init__(self, OpenAI_Instance: OpenAI) -> None:
        self.client = OpenAI_Instance

    def run(self, content: str):
        llm_response = self.client.chat.completions.create(
            model=MODEL,
            temperature=0,
            messages=[
                {"role": "user", "content": content},
            ],
        )
        llm_response_text = llm_response.choices[0].message
        json_string = str(llm_response_text.content)
        print(f"++> : {json_string}")
        return json_string
