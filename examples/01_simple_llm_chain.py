"""
Example 1: Simple LLM Chain

This example demonstrates the basics of LangChain:
- Creating a prompt template
- Setting up an LLM
- Creating and running a simple chain

Prerequisites:
- Set up your OPENAI_API_KEY in .env file
"""

import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()

def main():
    """
    Demonstrate a simple LLM chain with a prompt template.
    """
    print("=" * 50)
    print("Example 1: Simple LLM Chain")
    print("=" * 50)
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
        return
    
    # Initialize the LLM
    llm = OpenAI(temperature=0.7)
    
    # Create a prompt template
    template = """
    You are a helpful assistant that explains concepts clearly.
    
    Question: {question}
    
    Answer: Let me explain this in simple terms.
    """
    
    prompt = PromptTemplate(
        input_variables=["question"],
        template=template
    )
    
    # Create a chain
    chain = LLMChain(llm=llm, prompt=prompt)
    
    # Example questions
    questions = [
        "What is LangChain?",
        "What are the benefits of using prompt templates?",
        "How does an LLM chain work?"
    ]
    
    # Run the chain with different questions
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        print("-" * 50)
        
        response = chain.run(question=question)
        print(f"Answer: {response.strip()}")
        print()
    
    print("=" * 50)
    print("Example completed!")
    print("=" * 50)

if __name__ == "__main__":
    main()
