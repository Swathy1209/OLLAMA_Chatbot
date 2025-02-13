import streamlit as st
from langchain_community.llms import Ollama

# Initialize Llama 2 Model
llm = Ollama(model="llama2")

st.title('Llama 2 Chatbot')

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role': 'assistant', 'content': "How can I help you?"}]

# Display message history
for msg in st.session_state['messages']:
    st.chat_message(msg['role'], avatar='👤' if msg['role'] == 'user' else '🤖').write(msg['content'])

# Generate response
def generate_response():
    messages = [{'role': msg['role'], 'content': msg['content']} for msg in st.session_state['messages']]
    prompt = messages[-1]['content']
    response = llm.stream(input=prompt, messages=messages)
    full_response = ''
    for token in response:
        full_response += token
        yield token
    st.session_state['full_message'] = full_response

# Handle user input
if prompt := st.chat_input():
    st.session_state['messages'].append({'role': 'user', 'content': prompt})
    st.chat_message('user', avatar='👤').write(prompt)
    
    with st.chat_message('assistant', avatar='🤖'):
        response = st.write_stream(generate_response())
    
    st.session_state['messages'].append({'role': 'assistant', 'content': st.session_state['full_message']})
