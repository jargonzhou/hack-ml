
import streamlit as st

pages = {
    '🏠 Home': [
        st.Page('nav/home.py', title='Home')
    ],
    '📞 Contact us': [
        st.Page('nav/message.py', title='Message'),
        st.Page('nav/address.py', title='Address'),
    ],
}

pg = st.navigation(pages)
pg.run()
