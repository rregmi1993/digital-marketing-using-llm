from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

import streamlit as st
import os
import google.generativeai as genai

import facebook_integration

genai.configure(api_key=config['DEFAULT']['GEMINI_API_KEY'])

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro") 
#chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="DIGITAL MARKETING")

st.header("SOCIAL MEDIA DIGITAL MARKETING")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("POST")

if submit and input:
    response=get_gemini_response("You are a content writter, create a caption for social media for " + input + "with less than 50 words")
    
    fb_id = facebook_integration.post_in_facebook(response)
    
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("User", input))
    # st.subheader("The Response is")
    #print(response.text)
    # for chunk in response:
    #     st.write(chunk.text)
    #     st.session_state['chat_history'].append(("AI Response", chunk.text))
    st.session_state['chat_history'].append(("AI Response", response))
    st.write(f"Facebook Post id: {fb_id}")
if st.session_state['chat_history']:
    st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
    