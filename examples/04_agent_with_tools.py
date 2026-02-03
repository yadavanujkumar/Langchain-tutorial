"""
Example 4: Agent with Tools

This example demonstrates:
- Creating custom tools
- Setting up an agent
- Letting the agent decide which tools to use
- Agent reasoning and decision-making

Agents are powerful because they can:
- Reason about problems
- Choose appropriate tools
- Execute multi-step plans
- Interact with external systems

Prerequisites:
- Set up your OPENAI_API_KEY in .env file
"""

import os
from datetime import datetime
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain import hub

# Load environment variables
load_dotenv()

def get_current_time(input_text: str) -> str:
    """
    Tool to get the current time.
    """
    now = datetime.now()
    return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"

def calculator(expression: str) -> str:
    """
    Tool to perform basic calculations.
    Safely evaluates mathematical expressions using ast.
    """
    import ast
    import operator
    
    # Define safe operators
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
    }
    
    def safe_eval(node):
        """Safely evaluate an AST node."""
        if isinstance(node, ast.Num):  # number
            return node.n
        elif isinstance(node, ast.BinOp):  # binary operation
            left = safe_eval(node.left)
            right = safe_eval(node.right)
            return operators[type(node.op)](left, right)
        elif isinstance(node, ast.UnaryOp):  # unary operation
            operand = safe_eval(node.operand)
            return operators[type(node.op)](operand)
        else:
            raise ValueError(f"Unsupported operation: {node}")
    
    try:
        # Parse the expression
        tree = ast.parse(expression, mode='eval')
        result = safe_eval(tree.body)
        return f"The result of {expression} is {result}"
    except (SyntaxError, ValueError, TypeError, KeyError, ZeroDivisionError) as e:
        return f"Error calculating '{expression}': {str(e)}. Only basic arithmetic operations (+, -, *, /, **) are supported."

def word_counter(text: str) -> str:
    """
    Tool to count words in a text.
    """
    words = text.split()
    return f"The text contains {len(words)} words"

def reverse_text(text: str) -> str:
    """
    Tool to reverse a string.
    """
    return f"Reversed text: {text[::-1]}"

def main():
    """
    Demonstrate an agent with multiple tools.
    """
    print("=" * 50)
    print("Example 4: Agent with Tools")
    print("=" * 50)
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
        return
    
    print("\nStep 1: Creating custom tools...")
    
    # Define the tools
    tools = [
        Tool(
            name="CurrentTime",
            func=get_current_time,
            description="Useful for getting the current date and time. Input should be an empty string."
        ),
        Tool(
            name="Calculator",
            func=calculator,
            description="Useful for performing mathematical calculations. Input should be a mathematical expression like '2 + 2' or '10 * 5'."
        ),
        Tool(
            name="WordCounter",
            func=word_counter,
            description="Useful for counting the number of words in a text. Input should be the text to count words in."
        ),
        Tool(
            name="TextReverser",
            func=reverse_text,
            description="Useful for reversing a string. Input should be the text to reverse."
        )
    ]
    
    print(f"Created {len(tools)} tools:")
    for tool in tools:
        print(f"  - {tool.name}: {tool.description}")
    
    print("\nStep 2: Setting up the agent...")
    
    # Initialize the LLM
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    
    # Get the ReAct prompt from the hub
    try:
        prompt = hub.pull("hwchase17/react")
    except (ImportError, ConnectionError, Exception) as e:
        # Fallback prompt if hub is unavailable
        print(f"Note: Using fallback prompt (hub unavailable: {e})")
        template = """Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}"""
        
        prompt = PromptTemplate.from_template(template)
    
    # Create the agent
    agent = create_react_agent(llm, tools, prompt)
    
    # Create the agent executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=5
    )
    
    print("Agent is ready!")
    
    # Test queries that require different tools
    queries = [
        "What is the current time?",
        "Calculate 234 + 567",
        "How many words are in this sentence: 'LangChain is an amazing framework for building LLM applications'?",
        "Reverse the text 'Hello World'",
        "What is 15 multiplied by 8, and then tell me the current time?"
    ]
    
    print("\n" + "=" * 50)
    print("Running agent with different queries:")
    print("=" * 50)
    
    for i, query in enumerate(queries, 1):
        print(f"\n{'=' * 50}")
        print(f"Query {i}: {query}")
        print("=" * 50)
        
        try:
            result = agent_executor.invoke({"input": query})
            print(f"\nFinal Answer: {result['output']}")
        except Exception as e:
            print(f"Error: {str(e)}")
        
        print()
    
    print("=" * 50)
    print("Example completed!")
    print("=" * 50)
    print("\nNote: The agent automatically chose the right tools and combined them")
    print("to answer each question. This demonstrates the power of agent-based systems!")

if __name__ == "__main__":
    main()
