"""
Streamlit for Web Development - Listing 3-7. progress_bar.py
"""

import streamlit as st
import time

progress_text = st.empty()
progress_bar = st.progress(0)

total = 100
cur = 0
for i in range(10):
  cur += 10
  percent = int(cur * 100 / total)
  progress_text.subheader(f'Progress: {percent}')
  progress_bar.progress(percent)
  time.sleep(0.1)
