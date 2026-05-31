import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

# st.session_state -> dict -> 
CONFIG = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

#{'role': 'user', 'content': 'Hi'}
#{'role': 'assistant', 'content': 'Hi=ello'}

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # first add the message to message_history
    with st.chat_message('assistant'):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config= {'configurable': {'thread_id': 'thread-1'}},
                stream_mode= 'messages'
            )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})

## when we ask something like can u write 500 word blog on cricket we have to wait some time then 
#it shows response on ui but to make user experence better we can do one thing we can implement streaming
# it gives good user experience

###streaming means : model starts sending tokens as soon as it generated insted of waiting until entire response is generated.

#why streaming : 
# 1)fast response time--wo streaming (user will not wait for 5-6 seconds for generating response)
# 2)it keeps user enegaged.
# lets aassue that u ask agant to book tocket and for next one minute u willnot 
# get to see what things happened. 

# u have to just use stream() insted invoke()-> it provide generator object insted
#  of returing we use yield keyward 

# here we use st.stream(my_generator) - streamlit component that takes generator object.

