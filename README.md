🥗 Healthy Breakfast Idea Generator

A beginner-friendly Generative AI web application built using Python, LangChain, OpenAI, and Streamlit.

This project demonstrates how to connect to a Large Language Model (LLM) using LangChain Expression Language (LCEL), enforce strict output formatting through prompt engineering, extract clean text from LangChain AIMessage objects, and serve the result through an interactive web interface.

✨ Features

LangChain LCEL Integration: Uses ChatPromptTemplate piped (|) directly into ChatOpenAI.

Structured Output: Enforces strict formatting rules via system prompts (numbered list, one line per idea, no conversational filler).

Interactive Web UI: Built with Streamlit to provide a clean, responsive frontend with loading states.

Secure API Handling: Reads credentials safely via environment variables (.env).

🛠️ Tech Stack

Python 3.9+

LangChain (langchain, langchain-openai, langchain-core)

OpenAI API (gpt-4o-mini)

Streamlit

Python-dotenv

🚀 Getting Started

1. Clone or Navigate to Your Project Directory

cd breakfast


2. Create and Activate a Virtual Environment

On Windows (Command Prompt):

python -m venv venv
venv\Scripts\activate


On Windows (PowerShell):

python -m venv venv
venv\Scripts\Activate.ps1


On macOS / Linux:

python3 -m venv venv
source venv/bin/activate


3. Install Dependencies

pip install langchain langchain-openai streamlit python-dotenv


4. Configure Your OpenAI API Key

Create a .env file in the root directory of your project and add your OpenAI API key:

OPENAI_API_KEY=your_actual_openai_api_key_here


(Alternatively, you can set it directly in your terminal session using set OPENAI_API_KEY=your_key on Windows CMD or export OPENAI_API_KEY="your_key" on macOS/Linux).

💻 Usage

Run the Streamlit application using the Streamlit runner command:

streamlit run breakfast_app.py


Once started, Streamlit will automatically open a new tab in your default web browser at http://localhost:8501. Click the "Generate Breakfast Ideas" button to get 5 healthy breakfast suggestions!

📂 Project Structure

breakfast/
│
├── breakfast.py          # Core CLI script demonstrating raw AIMessage vs .content
├── breakfast_app.py      # Streamlit web application frontend
├── .env                  # Environment variables (API keys - do not commit to Git)
└── README.md             # Project documentation


🧠 Key Concepts Learned

Handling invoke() Responses: LangChain's .invoke() returns an AIMessage object containing metadata and token usage. Accessing .content isolates the clean text response.

Prompt Constraints: Explicitly defining output rules in the system message prevents vague answers and conversational preamble.

Temperature Control: Adjusting the temperature parameter controls creativity (0.7) versus deterministic consistency (0.0).