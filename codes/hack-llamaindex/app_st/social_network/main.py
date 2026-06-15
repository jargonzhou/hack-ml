import streamlit as st

from view import AddPostView, FeedView
from service import get_feed, add_post

AddPostView(add_post_func=add_post)
st.write('___')
FeedView(get_feed_func=get_feed)
