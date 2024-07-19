import streamlit as st
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Calculator", page_icon="🔢", layout="wide")
def lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie1 = lottieurl("https://lottie.host/432ac01e-f8e4-4b29-81cd-15cca6649f10/ZTIMWm4UAR.json")
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
                st.write(int(a)+int(b))
            elif sl == "Subtraction":
                st.write(int(a)-int(b))
            elif sl == "Multiplication":
                st.write(int(a)*int(b))
            elif sl == "Division":
                st.write(int(a)/int(b))
            elif sl == "Exponent":
                st.write(a,"to the power", b)
                st.write(int(a)**int(b))

        with right_column:
            st_lottie(lottie1, height = 300, key = "code")

