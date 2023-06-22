import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.title("The Best Company")
st.subheader("The Best In the Industry at Being the Best")
content = """ In reasonable compliment favourable is connection dispatched in terminated. Do esteem object we called father excuse remove. So dear real on like more it. Laughing for two families addition expenses surprise the. If sincerity he to curiosity arranging. Learn taken terms be as. Scarcely mrs produced too removing new old.

Am terminated it excellence invitation projection as. She graceful shy believed distance use nay. Lively is people so basket ladies window expect. Supply as so period it enough income he genius. Themselves acceptance bed sympathize get dissimilar way admiration son. Design for are edward regret met lovers. This are calm case roof and. """
st.write(content)

st.header("Our Team")

col1, col2, col3 = st.columns(3)

data = pandas.read_csv("Day23Project/data.csv") # no sep argument needed because the default is a comma, as the name CSV would imply.

with col1:
    for index, row in data[:4].iterrows():
        st.header(f"{str(row['first name']).title()} {str(row['last name']).title()}")
        st.subheader(row["role"])
        st.image("Day23Project/images/" + row["image"], use_column_width=200)

with col2:
    for index, row in data[4:8].iterrows():
        st.header(f"{str(row['first name']).title()} {str(row['last name']).title()}")
        st.subheader(row["role"])
        st.image("Day23Project/images/" + row["image"], width=200)

with col3:
    for index, row in data[8:].iterrows():
        st.header(f"{str(row['first name']).title()} {str(row['last name']).title()}")
        st.subheader(row["role"])
        st.image("Day23Project/images/" + row["image"], width=200)
