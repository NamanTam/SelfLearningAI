# SelfLearningAI

# AI Memory Assistant using Mem0 and Ollama

A Python-based AI assistant that uses persistent memory to personalize responses. It integrates the hosted Mem0 Platform for memory storage and retrieval with a locally running Ollama LLM for response generation.

The goal is to help the assistant remember important user preferences, interests, and ongoing goals instead of relying only on the current message.

## Features

- **Persistent Memory:** Stores useful information about users using Mem0.
- **Memory Retrieval:** Retrieves relevant memories before generating responses.
- **Personalized Responses:** Uses retrieved memories as context for the LLM.
- **Local LLM Inference:** Runs `llama3.2:3b` through Ollama.
- **Memory Extraction:** Uses an LLM to extract key facts rather than intentionally storing every conversation message.
- **Secure Configuration:** Loads the Mem0 API key from environment variables.

## Tech Stack

- Python
- Mem0 Platform
- Ollama
- Llama 3.2 (3B)
- OpenAI Python SDK (Ollama-compatible API)
- python-dotenv

## Architecture

1. The user enters a message.
2. The assistant searches Mem0 for relevant stored memories.
3. Retrieved memories are added to the system prompt.
4. Ollama generates a personalized response.
5. A memory-extraction step identifies potentially useful facts.
6. Extracted facts are submitted to Mem0 for storage or updating.

## Project Structure

```text
ai-memory-assistant/
├── memory_demo.py
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

## Prerequisites

- Python 3.10 or newer
- Ollama installed
- A Mem0 Platform API key
- Internet access for the hosted Mem0 Platform

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd ai-memory-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the Ollama model

```bash
ollama pull llama3.2:3b
```

Make sure Ollama is running locally.

### 5. Configure environment variables

Create a `.env` file in the project root and add:

```dotenv
MEM0_API_KEY=your_mem0_api_key_here
```

Get your API key from the Mem0 Platform.

Never commit your real `.env` file or API key to GitHub.

### 6. Run the application

```bash
python memory_demo.py
```

Type a message to interact with the assistant. Enter `exit` to quit.

## Example

**User:** I don't like thriller movies. I prefer science-fiction movies.

**Assistant:** I'll keep that preference in mind when suggesting movies.

**User (later):** Recommend a movie for tonight.

**Assistant:** The assistant can use the retrieved movie preferences to suggest relevant options.

*Note: Actual behavior depends on successful memory extraction, storage, retrieval, and the LLM's response.*

## Future Improvements

- Improve memory extraction and filtering.
- Handle outdated or conflicting memories.
- Add memory inspection and deletion commands.
- Evaluate memory retrieval relevance.
- Add automated tests.
- Make model and service configuration configurable.
- Add a web interface using FastAPI or Streamlit.

## Security

- Keep API keys in environment variables.
- Exclude `.env`, databases, and local model data from version control.
- Avoid storing sensitive personal information unnecessarily.

## License

Choose an appropriate open-source license before distributing this project.
