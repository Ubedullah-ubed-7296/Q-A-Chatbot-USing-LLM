import streamlit as st
import cohere  # Import Cohere SDK
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load your Cohere API key from environment variables
COHERE_API_KEY = os.getenv("4YPfzWcR3TVOCGo2R6rlqSFkdYPkwxLAhug0FVFM")

# Initialize Cohere client
co = cohere.Client(COHERE_API_KEY)

## Function to load Cohere model and get responses
def get_cohere_response(question):
    # Call Cohere API to generate a response
    response = co.generate(
        model='command-xlarge-nightly',  # Choose the model you want to use
        prompt=question,
        max_tokens=150,
        temperature=0.5
    )
    
    # Return the generated response
    return response.generations[0].text

## Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Langchain-like Application with Cohere")

# Input box for user to ask a question
input_question = st.text_input("Input: ", key="input")

# Button to trigger the generation of a response
submit = st.button("Ask the question")

# If the ask button is clicked, get the response and display it
if submit:
    response = get_cohere_response(input_question)
    st.subheader("The Response is")
    st.write(response)