# langchain-trial

A beginner LangChain project that builds a conversational weather agent with memory, structured output, and tool use.

## What it does

- Identifies the user's city based on their user ID
- Fetches real-time weather data from [wttr.in](https://wttr.in)
- Responds with humor using a funny weather assistant persona
- Remembers previous messages in the same conversation thread
- Returns structured responses with fields like `summary` and `temperature_celcius`

## Project Structure

```
├── main.py        # Agent setup, tools, and conversation logic
├── schemas.py     # Custom data shapes (ResponseFormat, Context)
└── .env           # API keys (not pushed to GitHub)
```

## How it works

The agent uses two tools:

- `locate_user` — looks up the city for a given user ID
- `get_weather` — fetches live weather data for that city

These tools are registered with LangChain using the `@tool` decorator, and the agent automatically decides when to call them based on the user's message.

Conversation memory is handled by `InMemorySaver` from LangGraph, scoped per `thread_id` — so follow-up questions like *"And is this usual?"* work correctly.

## Setup

1. Clone the repo
   ```bash
   git clone https://github.com/Ratnesh-101/langchain-trial.git
   cd langchain-trial
   ```

2. Install dependencies
   ```bash
   pip install langchain langgraph requests python-dotenv
   ```

3. Create a `.env` file and add your OpenAI API key
   ```
   OPENAI_API_KEY=sk-...
   ```

4. Run the agent
   ```bash
   python main.py
   ```

## Tech Stack

- [LangChain](https://langchain.com) — agent and tool framework
- [LangGraph](https://langchain-ai.github.io/langgraph) — memory and checkpointing
- [wttr.in](https://wttr.in) — free weather API
- [OpenAI GPT](https://openai.com) — the underlying language model
