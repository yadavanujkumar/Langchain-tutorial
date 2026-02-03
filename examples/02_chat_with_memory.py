"""
Example 2: Chat Model with Memory

This example demonstrates:
- Using chat models (designed for conversations)
- Implementing conversation memory
- Maintaining context across multiple turns

Prerequisites:
- Set up your OPENAI_API_KEY in .env file
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

# Load environment variables
load_dotenv()

def main():
    """
    Demonstrate a chat model with conversation memory.
    """
    print("=" * 50)
    print("Example 2: Chat Model with Memory")
    print("=" * 50)
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
        return
    
    # Initialize the Chat Model
    chat_model = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")
    
    # Create conversation memory
    memory = ConversationBufferMemory(return_messages=True)
    
    # Create a conversation chain
    conversation = ConversationChain(
        llm=chat_model,
        memory=memory,
        verbose=True  # Shows the conversation flow
    )
    
    print("\nStarting a conversation with memory...")
    print("The model will remember previous exchanges.\n")
    
    # Simulate a multi-turn conversation
    conversations = [
        "Hi! My name is Alex and I'm learning about LangChain.",
        "What are some key features of LangChain?",
        "Can you remind me what my name is?",  # Tests memory
        "Which of those features would be most useful for building a chatbot?"
    ]
    
    for i, user_input in enumerate(conversations, 1):
        print(f"\n{'=' * 50}")
        print(f"Turn {i}")
        print(f"{'=' * 50}")
        print(f"User: {user_input}")
        print()
        
        response = conversation.predict(input=user_input)
        print(f"Assistant: {response}")
    
    print("\n" + "=" * 50)
    print("Conversation History:")
    print("=" * 50)
    
    # Display the conversation history
    print("\nThe model remembered:")
    for message in memory.chat_memory.messages:
        role = "User" if message.type == "human" else "Assistant"
        print(f"{role}: {message.content[:100]}...")
    
    print("\n" + "=" * 50)
    print("Example completed!")
    print("=" * 50)

if __name__ == "__main__":
    main()
