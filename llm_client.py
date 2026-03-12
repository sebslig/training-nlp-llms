import os
import openai
from openai import OpenAI
from typing import List, Dict, Any

class LLMClient:
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo", temperature: float = 0.7, max_tokens: int = 150):
        if not api_key:
            raise ValueError("OpenAI API key must be provided.")
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate_text(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant for generating synthetic data.
                     Please provide concise and realistic responses."},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
            return response.choices[0].message.content.strip()
        except openai.APIError as e:
            print(f"OpenAI API error: {e}")
            return ""
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return ""

    def generate_batch(self, prompts: List[str]) -> List[str]:
        results = []
        for prompt in prompts:
            results.append(self.generate_text(prompt))
        return results
