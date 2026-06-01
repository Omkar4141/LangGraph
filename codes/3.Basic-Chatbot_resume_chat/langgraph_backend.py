from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage,HumanMessage
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(model="llama3.2:1b")

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

# Checkpointer
checkpointer = InMemorySaver()

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)


##########calling the node4
# from langchain_core.messages import HumanMessage

CONFIG = {'configurable': {'thread_id': 'thread-1'}}
# response = chatbot.invoke({'messages': [HumanMessage(content="Hi")]}, config=CONFIG)
# print(response)

##streaming
for message_chunk,metadata in chatbot.stream({'messages': [HumanMessage(content="Hi")]},
               config=CONFIG ,
               stream_mode="messages"):

    if message_chunk.content:
        print(message_chunk.content,end="|",flush=True)

# basically this stream restuns generator object so insted of generating entire output once it 
# provide it uses yield 