"""
PITS: personalized intelligent tutoring system

The main entry point for the Streamlit app. This handles the initialization of the
application and manages the navigation between different screens based on the application logic
"""

# WARN: SHOULD NOT named app.py

import streamlit as st
from app.pits.training_interface import show_training_UI
from app.pits.quiz_interface import show_quiz
from app.pits.logging_functions import reset_log
from app.pits.session_functions import load_session, delete_session
from app.pits.user_onboarding import user_onboarding
from app.pits.global_settings import touch_storage

import asyncio


async def main():
  st.set_page_config(layout="wide")
  st.sidebar.title('P.I.T.S.')
  st.sidebar.markdown('### Your Personalized Intelligent Tutoring System')

  # if 'OPENAI_API_KEY' not in st.session_state or not st.session_state['OPENAI_API_KEY']:
  #   api_key = st.text_input(
  #       "Enter your OpenAI API Key (or leave blank if running locally): ")
  #   st.session_state['OPENAI_API_KEY'] = api_key
  #   os.environ['OPENAI_API_KEY'] = api_key

  # Check if the user is returning and has opted to take a quiz
  if 'show_quiz' in st.session_state and st.session_state['show_quiz']:
    # Show the quiz screen immediately
    show_quiz(st.session_state['study_subject'])
  elif 'resume_session' in st.session_state and st.session_state['resume_session']:
    # If resuming, clear previous content and show the training UI
    st.session_state['show_quiz'] = False  # Ensure quiz is not shown
    await show_training_UI(st.session_state['user_name'],
                           st.session_state['study_subject'])
  elif not load_session(st.session_state):
    user_onboarding()  # Show the onboarding screen for new users
  else:
    # For returning users, display options to resume or start a new session
    st.write(f"Welcome back {st.session_state['user_name']}!")
    col1, col2 = st.columns(2)
    if col1.button(f"Resume your study of {st.session_state['study_subject']}"):
      # Mark the session to be resumed and rerun to clear previous content
      st.session_state['resume_session'] = True
      st.rerun()
    if col2.button('Start a new session'):
      delete_session(st.session_state)
      reset_log()
      # Clear session state and rerun for a fresh start
      for key in list(st.session_state.keys()):
        del st.session_state[key]
      st.rerun()


# if __name__ == "__main__":
#   touch_storage()

#   main()

touch_storage()
asyncio.run(main())
