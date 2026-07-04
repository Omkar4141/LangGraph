import asyncio
import sys
from typing import Annotated, TypedDict

from dotenv import load_dotenv

from langchain_ollama import ChatOllama
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from langchain_mcp_adapters.client import MultiServerMCPClient

# Load environment variables
load_dotenv()

# LLM
llm = ChatOllama(model="llama3.2:1b")

# MCP Client
client = MultiServerMCPClient(
    {
        "arith": {
            "transport": "stdio",
            "command": sys.executable,  # Uses the same Python interpreter
            "args": [
                r"C:\Users\hp\Desktop\LangGraph\codes\6.MCP_with_langgraph\server.py"
            ],
        },
         # "expense": {
        #     "transport": "streamable_http",  # if this fails, try "sse"
        #     "url": "https://splendid-gold-dingo.fastmcp.app/mcp"
        # }
    }
)


# Graph State
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


async def build_graph():
    # Fetch MCP tools
    tools = await client.get_tools()

    print("\nLoaded Tools:")
    for tool in tools:
        print("-", tool.name)

    # Bind tools to LLM
    llm_with_tools = llm.bind_tools(tools)

    # Chat node
    async def chat_node(state: ChatState):
        response = await llm_with_tools.ainvoke(state["messages"])
        return {"messages": [response]}

    # Tool node
    tool_node = ToolNode(tools)

    # Graph
    graph = StateGraph(ChatState)

    graph.add_node("chat_node", chat_node)
    graph.add_node("tools", tool_node)

    graph.add_edge(START, "chat_node")
    graph.add_conditional_edges("chat_node", tools_condition)
    graph.add_edge("tools", "chat_node")

    return graph.compile()


async def main():
    chatbot = await build_graph()

    while True:
        query = input("\nYou: ")

        if query.lower() in ["exit", "quit"]:
            break

        result = await chatbot.ainvoke(
            {
                "messages": [
                    HumanMessage(content=query)
                ]
            }
        )

        print("\nAssistant:")
        print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())