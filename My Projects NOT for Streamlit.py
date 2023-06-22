"""This is the most advanced version of my Web Portfolio currently. Uses local images which will be a problem for deployment
using streamlit, but presumably there's a way around that."""


import streamlit as st
from annotated_text import annotated_text as at
from streamlit_extras.colored_header import colored_header
from markdownlit import mdlit
from streamlit_extras.switch_page_button import switch_page
from streamlit_card import card
from streamlit_extras.let_it_rain import rain # Hahaha
import pandas

st.set_page_config(layout="wide")

rain("💻", falling_speed=-10)

headcol1, headcol2 = st.columns(2)

with headcol1:
    st.image("images/cormanowild.jpg")

with headcol2:
    st.title("Cormano Wild")
    content = """ In reasonable compliment favourable is connection dispatched in terminated. Do esteem object we called father excuse remove. So dear real on like more it. Laughing for two families addition expenses surprise the. If sincerity he to curiosity arranging. Learn taken terms be as. Scarcely mrs produced too removing new old.

Am terminated it excellence invitation projection as. She graceful shy believed distance use nay. Lively is people so basket ladies window expect. Supply as so period it enough income he genius. Themselves acceptance bed sympathize get dissimilar way admiration son. Design for are edward regret met lovers. This are calm case roof and. """
    st.info(content)

    contact_me2 = st.button("Contact me!")
    if contact_me2:
        switch_page("Contact Me")
#
# greeting = "Below you can find some of the apps I have built in Python and in R. Feel free to contact me!"
# st.subheader(greeting)
st.divider()

at("Below you can find some of the apps I have built in ",
                   ("Python", "", "#ffeeaa"),
                   "and in ",
                   ("R", "","#faf"),
                   ". Feel free to contact me!")
at("(By the way, this entire Web page was written in ",
   ("Python", "", "#fea"),
   " using ",
   ("Streamlit","", "#92fa34"),
   "!)")
st.divider()

data = pandas.read_csv ("data.csv", sep=",")

bodycol1, bodycolspace, bodycol2 = st.columns([1.5, 0.2, 1.5])

with bodycol1:
    for index, row in data[:10].iterrows():
        # st.header(row["title"])
        colored_header(label=row["title"], description="", color_name="orange-70")
#       colored_header(label=row["title"], description=f'{row["description"]}', color_name="orange-70")
        st.write(row["description"])
        st.image("images/" + row["image"], use_column_width=True)
        st.write(f"[Placeholder Source Code Link]({row['url']})")

with bodycol2:
    for index, row in data[10:].iterrows():
        # st.header(row["title"])
        colored_header(label=row["title"], description="", color_name="yellow-70")
        st.write(row["description"])
        st.image("images/" + row["image"], use_column_width=True)
        st.write("[Placeholder Source Code Link](https://en.wikipedia.org)")

st.divider()
contact_me = st.button("How can I contact you?")
if contact_me:
    switch_page("Contact Me")