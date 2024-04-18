import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
load_dotenv()  

# setting up api key
# genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# function to load gemini pro and get responses
model = genai.GenerativeModel("gemini-pro-vision")

def call_gemini_vision(system_prompt, image, user_input):   # system_prompt: setting system behavior at backend  
    response = model.generate_content([system_prompt, image, user_input])
    response.text

# setup streamlit UI

st.title("Gemini Invoice Extractor")

with st.sidebar:
    api_key = st.text_input('Enter your Gemini API key: ', type = 'password')
genai.configure(api_key = api_key)

system_prompt = '''
You are an expert invoice extractor. You will be given an image of an invoice.
See the image in detail, extract each and every minute detail and answer the user's query accordingly.
Be precise and to the point. Only answer queries that are related to the invoice. 
If the user inputs image other than invoice or asks for any irrelevant question, 
simply say: "As an Invoice Extractor, I can only answer queries 
specific to your uploaded invoice image. So kindly ask relevant question.". Be polite, generous, humble.

'''

uploaded_file = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, "Your image", use_column_width=True)

input = st.text_input("Ask about the invoice")

submit = st.button("Process")

if submit:
    response = call_gemini_vision(system_prompt, image, input)
    st.write(response)

if not api_key:
    st.warning("Please enter your Gemini API key in the sidebar.")
