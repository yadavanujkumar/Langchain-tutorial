# LangChain Tutorial

A comprehensive tutorial repository for learning LangChain - a powerful framework for developing applications powered by large language models (LLMs).

## 📚 What is LangChain?

LangChain is a framework designed to simplify the creation of applications using large language models. It provides:
- **Prompt management**: Templates and utilities for working with prompts
- **Chains**: Sequences of calls to LLMs or other utilities
- **Memory**: Persistence of state between chain/agent calls
- **Agents**: Decision-making systems that use LLMs to determine actions
- **RAG (Retrieval Augmented Generation)**: Combining your data with LLMs

## 🚀 Getting Started

**New to LangChain?** Check out our [Quick Start Guide](QUICKSTART.md) for a fast setup!

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (or other LLM provider credentials)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yadavanujkumar/Langchain-tutorial.git
cd Langchain-tutorial
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your environment variables:
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_api_key_here
```

## 📖 Tutorial Examples

This repository contains several examples demonstrating different LangChain capabilities:

### 1. Basic LLM Chain (`examples/01_simple_llm_chain.py`)
Learn the fundamentals of creating a simple LLM chain with prompt templates.
- Basic prompt templates
- LLM integration
- Simple chain execution

```bash
python examples/01_simple_llm_chain.py
```

### 2. Chat Model with Memory (`examples/02_chat_with_memory.py`)
Understand how to maintain conversation context using memory.
- Chat models
- Conversation buffer memory
- Multi-turn conversations

```bash
python examples/02_chat_with_memory.py
```

### 3. Retrieval Augmented Generation - RAG (`examples/03_rag_example.py`)
Learn how to build a system that answers questions based on your own documents.
- Document loading and splitting
- Vector embeddings
- Similarity search
- Question answering over documents

```bash
python examples/03_rag_example.py
```

### 4. Agent with Tools (`examples/04_agent_with_tools.py`)
Discover how to create an agent that can use tools to accomplish tasks.
- Custom tool creation
- Agent initialization
- Tool selection and execution

```bash
python examples/04_agent_with_tools.py
```

## 📁 Project Structure

```
Langchain-tutorial/
├── examples/
│   ├── 01_simple_llm_chain.py
│   ├── 02_chat_with_memory.py
│   ├── 03_rag_example.py
│   └── 04_agent_with_tools.py
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

## 🔑 API Keys

This tutorial uses OpenAI's API by default. You'll need to:
1. Sign up at [OpenAI](https://platform.openai.com/)
2. Generate an API key
3. Add it to your `.env` file

You can also use other LLM providers supported by LangChain (Anthropic, Cohere, HuggingFace, etc.).

## 📚 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [LangChain Blog](https://blog.langchain.dev/)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) to learn how you can help:
- Report bugs
- Suggest new examples
- Improve documentation
- Submit pull requests

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

These examples use the OpenAI API which may incur costs. Please be aware of your API usage and associated charges.

## 💡 Tips

- Start with the simple examples and progress to more complex ones
- Experiment with different prompts and parameters
- Read the comments in each example for detailed explanations
- Check the [LangChain documentation](https://python.langchain.com/) for more advanced features

Happy Learning! 🎉