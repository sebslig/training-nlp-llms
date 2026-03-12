# LLM-Synthetic-Data-Generator

This project provides a minimal framework for generating synthetic text data using Large Language Models (LLMs). This data can be used to augment datasets for training domain-specific Natural Language Processing (NLP) models, especially in scenarios with limited real-world data.

## Features

- Define prompts for LLM-based data generation.
- Simple script to generate synthetic text.
- Basic output to CSV format.

## Setup

1. Clone the repository:
   `git clone https://github.com/your-username/LLM-Synthetic-Data-Generator.git`
2. Navigate to the project directory:
   `cd LLM-Synthetic-Data-Generator`
3. Install dependencies:
   `pip install -r requirements.txt`

## Usage

1. Modify `config.py` with your LLM API key and desired prompts.
2. Run the generation script:
   `python generate_data.py`

This will generate a `synthetic_data.csv` file.

## Project Structure

- `README.md`: Project overview.
- `.gitignore`: Files to ignore.
- `requirements.txt`: Python dependencies.
- `config.py`: Configuration for LLM API and prompts.
- `generate_data.py`: Main script to orchestrate data generation.
- `llm_client.py`: Abstraction for LLM API calls.

## Contributing

Feel free to fork, modify, and contribute. Pull requests are welcome!

## License

This project is open-sourced under the MIT License.