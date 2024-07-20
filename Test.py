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
        try:
            # Ensure the inputs are not None before converting to int
            num1 = int(a) if a else 0
            num2 = int(b) if b else 0
        except ValueError:
            st.write("Please enter valid numbers")
        with left_column1:
            li = ["Addition", "Subtraction", "Multiplication", "Division", "Exponent"]
            sl = st.selectbox("---Choose an operator---", li)
            if sl == "Addition":
                st.write(num1 + num2)
            elif sl == "Subtraction":
                st.write(num1 - num2)
            elif sl == "Multiplication":
                st.write(num1 * num2)
            elif sl == "Division":
                st.write(num1 / num2)
            elif sl == "Exponent":
                st.write(a,"to the power", b)
                st.write(num1 ** num2)


