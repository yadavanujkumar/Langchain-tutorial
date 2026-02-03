"""
Example 3: Retrieval Augmented Generation (RAG)

This example demonstrates:
- Loading and processing documents
- Creating embeddings and vector stores
- Performing similarity search
- Answering questions based on custom documents

RAG allows you to:
- Give LLMs access to your own data
- Answer questions based on specific documents
- Reduce hallucinations by grounding responses in real data

Prerequisites:
- Set up your OPENAI_API_KEY in .env file
"""

import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.schema import Document

# Load environment variables
load_dotenv()

def create_sample_documents():
    """
    Create sample documents about LangChain for demonstration.
    In a real application, you would load these from files, databases, etc.
    """
    documents = [
        Document(
            page_content="""
            LangChain is a framework for developing applications powered by language models.
            It provides tools and abstractions for working with LLMs, including prompt management,
            chains, memory, agents, and more. LangChain makes it easier to build complex 
            applications that leverage the power of large language models.
            """,
            metadata={"source": "intro", "topic": "overview"}
        ),
        Document(
            page_content="""
            Chains in LangChain are sequences of calls to LLMs or other utilities.
            They allow you to combine multiple components to create more complex applications.
            Common chain types include LLMChain, SequentialChain, and TransformChain.
            Chains can be simple (single LLM call) or complex (multiple steps with logic).
            """,
            metadata={"source": "concepts", "topic": "chains"}
        ),
        Document(
            page_content="""
            Memory in LangChain allows you to persist state between chain or agent calls.
            This is crucial for applications like chatbots that need to remember conversation history.
            LangChain provides different memory types including ConversationBufferMemory,
            ConversationSummaryMemory, and ConversationBufferWindowMemory.
            """,
            metadata={"source": "concepts", "topic": "memory"}
        ),
        Document(
            page_content="""
            Agents in LangChain use LLMs to decide which actions to take.
            They can use tools to interact with external systems, search the web,
            perform calculations, and more. Agents are powerful for building autonomous
            systems that can reason about problems and take appropriate actions.
            """,
            metadata={"source": "concepts", "topic": "agents"}
        ),
        Document(
            page_content="""
            Vector stores in LangChain store embeddings of text and enable similarity search.
            Popular vector stores include Chroma, Pinecone, FAISS, and Weaviate.
            They are essential for Retrieval Augmented Generation (RAG) applications
            where you need to find relevant documents to answer user queries.
            """,
            metadata={"source": "concepts", "topic": "vectorstores"}
        )
    ]
    return documents

def main():
    """
    Demonstrate RAG by creating a question-answering system over custom documents.
    """
    print("=" * 50)
    print("Example 3: Retrieval Augmented Generation (RAG)")
    print("=" * 50)
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
        return
    
    print("\nStep 1: Creating sample documents...")
    documents = create_sample_documents()
    print(f"Created {len(documents)} documents about LangChain")
    
    print("\nStep 2: Splitting documents into chunks...")
    text_splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    texts = text_splitter.split_documents(documents)
    print(f"Split into {len(texts)} text chunks")
    
    print("\nStep 3: Creating embeddings and vector store...")
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(
        documents=texts,
        embedding=embeddings,
        collection_name="langchain_docs"
    )
    print("Vector store created successfully!")
    
    print("\nStep 4: Setting up the QA chain...")
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),
        return_source_documents=True
    )
    print("QA chain ready!")
    
    # Ask questions about the documents
    questions = [
        "What is LangChain?",
        "How do chains work in LangChain?",
        "What memory types are available?",
        "What can agents do?",
        "What are vector stores used for?"
    ]
    
    print("\n" + "=" * 50)
    print("Asking questions based on the documents:")
    print("=" * 50)
    
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        print("-" * 50)
        
        result = qa_chain.invoke({"query": question})
        print(f"Answer: {result['result']}")
        
        # Show which documents were used
        print(f"\nSources used:")
        for doc in result['source_documents']:
            print(f"  - Topic: {doc.metadata['topic']}")
    
    print("\n" + "=" * 50)
    print("Example completed!")
    print("=" * 50)
    print("\nNote: RAG allows the LLM to answer questions based on your specific documents,")
    print("reducing hallucinations and providing more accurate, grounded responses.")

if __name__ == "__main__":
    main()
