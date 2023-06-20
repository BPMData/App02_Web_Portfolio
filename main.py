# This will be the beginning of my 2nd App - a Web portfolio! I needed one of these, anyway.

import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/cormanowild.jpg", width=600)

with col2:
    st.title("Cormano Wild")
    content = """ In reasonable compliment favourable is connection dispatched in terminated. Do esteem object we called father excuse remove. So dear real on like more it. Laughing for two families addition expenses surprise the. If sincerity he to curiosity arranging. Learn taken terms be as. Scarcely mrs produced too removing new old.

Am terminated it excellence invitation projection as. She graceful shy believed distance use nay. Lively is people so basket ladies window expect. Supply as so period it enough income he genius. Themselves acceptance bed sympathize get dissimilar way admiration son. Design for are edward regret met lovers. This are calm case roof and. """
    st.info(content)

greeting = "Below you can find some of the apps I have built in Python and in R. Feel free to contact me!"
st.subheader(greeting)
