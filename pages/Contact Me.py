import streamlit as st
from streamlit_extras.let_it_rain import rain
from annotated_text import annotated_text as at
from streamlit_extras.colored_header import colored_header
from streamlit_card import card
from markdownlit import mdlit
from streamlit_extras.switch_page_button import switch_page
from streamlit_card import card
from send_email import send_email

st.set_page_config(layout="wide")

rain("📧")

st.title("Contact Me:")

with st.form(key="contact_form"):
    user_email = st.text_input("Enter your e-mail address here:", placeholder="Your e-mail...")
    user_message = st.text_area("Enter your message to me here:", placeholder="Your message...")
    formatted_message = f"""Subject: {user_email} has reached out to you! \n
     
     They wrote:\n
     
     {user_message}
     \n\n
     This message was sent by:\n
     {user_email}."""

    submit_button = st.form_submit_button("Send me your message!")
    if submit_button:
        print("e-mail sent!")
        send_email(formatted_message)
        st.info("Your e-mail was successfully delivered!")



st.divider()
take_me = st.button("Take me back to the projects!")
if take_me:
    switch_page("My Projects")