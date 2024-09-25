import streamlit as st
import pandas as pd 


st.title("Hello Procurement Team")
st.write("This is a simple web app to help you with your procurement process")

file = st.file_uploader("Upload your file", type = ['csv'])

# define default session state
modes = ["Delivery Date", "Quality", "Price", "Service", "Overall"]
for i in range(5):
    if f"button_{i}" not in st.session_state:
        st.session_state[f"button_{i}"] = False


if file is not None:
    df = pd.read_csv(file)
    with st.expander("Show Data"):
        st.write(df)

        if st.checkbox("Show Summary"):
            st.write(df.describe())

    button_cols = st.columns(5)
    for i, botton_col in enumerate(button_cols):
        st.button(modes[i], key = f"button_{i}", on_click = st.session_state[f"button_{i}"])
        st.write(st.session_state[f"button_{i}"])
        if st.session_state[f"button_{i}"]:
            st.write(f"Button {i} is clicked")