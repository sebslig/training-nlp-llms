import os
from dotenv import load_dotenv

load_dotenv()

# --- LLM Configuration ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-3.5-turbo"
TEMPERATURE = 0.7
MAX_TOKENS = 150

# --- Generation Configuration ---
NUM_SAMPLES = 10
OUTPUT_FILE = "synthetic_data.csv"

# --- Prompts ---
# Example: Generate product review for a fictional item
PROMPT_TEMPLATES = [
    "Write an enthusiastic product review for a new 'Smart Coffee Mug' considering its smart features and design.",
    "Give a critical review for a 'Quantum Computing Kit' outlining its practical limitations for a hobbyist.",
    "Describe a user interaction with an AI personal assistant, focusing on a successful task completion like booking a flight."
]

# You can add more complex prompt structures or a function to generate prompts dynamically

# Optional: Structure for expected output if using a structured generation approach
EXPECTED_OUTPUT_SCHEMA = {
    "review_text": str,
    "sentiment": str, # e.g., 'positive', 'negative', 'neutral'
    "product_name": str
}
