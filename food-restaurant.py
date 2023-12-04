from openai import OpenAI
import streamlit as st 
import pandas as pd
# Get the API key from the sidebar called OpenAI API key
user_api_key = st.sidebar.text_input("OpenAI API key", type="password")
client = openai.OpenAI(api_key=user_api_key)



prompt = """Create a 20 recommendation according to higher rating to lowest rating list of restaurants in 
a place where clients request in the request box, rating score is from 5 to 1. And write a short review of the food, 
according to real reviews. And then show the price range of each restaurant, switch and calculate the price from 
any currency to USD and then calculate it to THB. And then show the location of the restaurant on the map by the following information:
province, district, subdistrict, and street name. And then show the opening time and closing time of the restaurant.
"""




#title = st.text_input('Enter a specific place where you want us to make a suggestion.', ' ')







with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
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


