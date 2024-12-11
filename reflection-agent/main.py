from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph
from typing import Sequence
from chains import reflection_chain, generate_chain
load_dotenv()

REFLECT ="reflect"
GENERATE = "generate"

def generation_node(state:Sequence[BaseMessage]):
    return generate_chain.invoke({"messages": state})

def reflection_node(state:Sequence[BaseMessage]):
    return reflection_chain.invoke({"messages": state})
if __name__ == "__main__":
    print("\nWelcome to LangGraph...\n")
