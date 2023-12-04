
from openai import OpenAI
import streamlit as st 
import pandas as pd

prompt = """Act as an AI assistant to help users find a restaurant based on their preferences.
List the suggestions in a JSON array, one suggestion per line.
"Name" - Name of the restaurant
"Rating" - Rating of the restaurant
"Price" - Price of the restaurant
"Address" - Address of the restaurant
"Phone" - Phone number of the restaurant
"Reviews" - Few reviews of the restaurant
"""
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"


st.title("Food Restaurant Recommendation") 
st.caption("A clean suggestion for easier way to find a restaurant")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

client = OpenAI(api_key=openai_api_key)
st.session_state.messages.append({"role": "user", "content": prompt})
st.chat_message("user").write(prompt)
response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
msg = response.choices[0].message.content
st.session_state.messages.append({"role": "assistant", "content": msg})
st.chat_message("assistant").write(msg)
st.session_state.messages = st.session_state.messages[-5:]  


response = client.completions.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=100,
    temperature=0.9,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["\n"],
)


st.set_page_config(
    page_title="Food Restaurant Recommendation",
    page_icon="🍔",
    layout="centered",
    initial_sidebar_state="expanded",
)





    