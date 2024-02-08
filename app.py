import streamlit as st
import pandas as pd


def app():
    st.title("GitHub Forks and User Info")

    page = st.sidebar.selectbox("Choose a page", ["Forks", "User Info"])

    if page == "Forks":
        st.header("Forks")
        file = st.file_uploader("Upload your forks.csv file", type=["csv"])
        if file is not None:
            data = pd.read_csv(file)
            st.dataframe(data)
    elif page == "User Info":
        st.header("User Info")
        file = st.file_uploader("Upload your user_info.csv file", type=["csv"])
        if file is not None:
            data = pd.read_csv(file)
            st.dataframe(data)


if __name__ == "__main__":
    app()
