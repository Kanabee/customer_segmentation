
"""
# My first app
Here's our first attempt at using data to create application:
"""

import os
import streamlit as st
import openai
from apikey import *
# Set the OpenAI API key
openai.api_key= "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 "


with st.form(key='my_form'):
    # Add input fields for the OpenAI Completion API
    prompt = st.text_input(label='Story', value="Created your story's name")
    max_tokens = st.number_input(label='Max Tokens', value=7)
   
    
    # Add input fields for the OpenAI Image API
    
    image_count = st.number_input(label='Image Count', value=2)
    image_size = st.selectbox(label='Image Size', options=['512x512', '1024x1024'], index=1)
    
    submit_button = st.form_submit_button(label='Submit')

    # Create the OpenAI API calls inside the submit_button block
    if submit_button:
        # Call the OpenAI Completion API
        completion = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            
        )
        st.write(completion.choices[0].text)

        # Call the OpenAI Image API
        image = openai.Image.create(
            prompt=prompt,
            n=image_count,
            size=image_size
        )
        st.image(image['data'][0]['url'])
