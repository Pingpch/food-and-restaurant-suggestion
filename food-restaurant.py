import streamlit as st
import openai
import json
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
st.header('Food Restaurant', divider='rainbow')

st.subheader("This is a food restaurant recommendation webpage")

title = st.text_input('Enter a specific place where you want us to make a suggestion.', ' ')


# submit button
st.button("submit", type="primary")

# Show the response from the AI in a box
st.markdown('**AI response:**')
suggestion_dictionary = response.choices[0].message.content

sd = json.loads(suggestion_dictionary)

print (sd)
suggestion_df = pd.DataFrame.from_dict(sd)
print(suggestion_df)
st.table(suggestion_df)