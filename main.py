# This will be the beginning of my 2nd App - a Web portfolio! I needed one of these, anyway.

import streamlit as st
from annotated_text import annotated_text as at
from streamlit_extras.colored_header import colored_header
from markdownlit import mdlit
from streamlit_extras.switch_page_button import switch_page
from streamlit_card import card
#lmao
from streamlit_extras.let_it_rain import rain
import pandas

st.set_page_config(layout="wide")

rain("👻")

headcol1, headcol2 = st.columns(2)

with headcol1:
    st.image("images/cormanowild.jpg")

with headcol2:
    st.title("Cormano Wild")
    content = """ In reasonable compliment favourable is connection dispatched in terminated. Do esteem object we called father excuse remove. So dear real on like more it. Laughing for two families addition expenses surprise the. If sincerity he to curiosity arranging. Learn taken terms be as. Scarcely mrs produced too removing new old.

Am terminated it excellence invitation projection as. She graceful shy believed distance use nay. Lively is people so basket ladies window expect. Supply as so period it enough income he genius. Themselves acceptance bed sympathize get dissimilar way admiration son. Design for are edward regret met lovers. This are calm case roof and. """
    st.info(content)
#
# greeting = "Below you can find some of the apps I have built in Python and in R. Feel free to contact me!"
# st.subheader(greeting)

at("Below you can find some of the apps I have built in ",
                   ("Python", "", "#fea"),
                   "and in ",
                   ("R", "","#faf"),
                   ". Feel free to contact me!")

import pandas
data = pandas.read_csv ("data.csv", sep=",")

bodycol1, bodycol2 = st.columns(2)

with bodycol1:
    for index, row in data[:10].iterrows():
        st.header(row["title"])

with bodycol2:
    for index, row in data[10:].iterrows():
        st.header(row["title"])