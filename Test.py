import streamlit as st
import requests

st.set_page_config(page_title="Calculator", page_icon="🔢", layout="wide")
with st.container():
    st.header("CALCULATOR")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        a = st.number_input("input a number", value = None , key = "input1")
        b = st.number_input("input a number", value = None , key = "input2")
        st.write("Select an operator")
        left_column1, right_column1 = st.columns(2)
        with left_column1:
            li = ["Addition", "Subtraction", "Multiplication", "Division", "Exponent"]
            sl = st.selectbox("---Choose an operator---", li)
            if sl == "Addition":
                st.write(a+b)
            elif sl == "Subtraction":
                st.write(a-b)
            elif sl == "Multiplication":
                st.write(a*b)
            elif sl == "Division":
                st.write(a/b)
            elif sl == "Exponent":
                st.write(a,"to the power", b)
                st.write(a**b)


