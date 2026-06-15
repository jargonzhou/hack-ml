"""
Streamlit for Web Development - Listing 3-24. fragmenting.py
"""

import streamlit as st


@st.fragment
def my_fragment():
  """Define a fragment"""
  name = st.text_input('Enter your name')
  if name:
    st.write(f'Hello, {name}!')


st.write('This runs every time. ')
my_fragment()  # Only this part re-runs when the input changes
st.write('This also stays the same.')
