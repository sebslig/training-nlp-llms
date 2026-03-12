import csv
from typing import List, Dict

from llm_client import LLMClient
import config

def main():
    if not config.OPENAI_API_KEY:
        print("Error: OPENAI_API_KEY not found. Please set it in your environment or config.py.")
        return

    llm_client = LLMClient(
        api_key=config.OPENAI_API_KEY,
        model=config.OPENAI_MODEL,
        temperature=config.TEMPERATURE,
        max_tokens=config.MAX_TOKENS
    )

    synthetic_data: List[Dict[str, str]] = []

    print(f"Generating {config.NUM_SAMPLES} synthetic data samples...")
    for i in range(config.NUM_SAMPLES):
        # Cycle through prompt templates or pick one randomly
        prompt = config.PROMPT_TEMPLATES[i % len(config.PROMPT_TEMPLATES)]
        print(f"  Generating sample {i+1}/{config.NUM_SAMPLES} with prompt: '{prompt[:50]}...' ")
        generated_text = llm_client.generate_text(prompt)
        
        if generated_text:
            # For simple generation, we just store the prompt and the generated text.
            # For structured generation, you might parse the LLM output here.
            synthetic_data.append({"prompt": prompt, "generated_text": generated_text})
            
    if synthetic_data:
        print(f"Writing {len(synthetic_data)} samples to {config.OUTPUT_FILE}")
        with open(config.OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
            fieldnames = synthetic_data[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(synthetic_data)
        print("Synthetic data generation complete.")
    else:
        print("No synthetic data generated.")

if __name__ == "__main__":
    main()
