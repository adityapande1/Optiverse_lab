import streamlit as st
from connectors.dbconnector import DBConnector

def run():
    st.title("Candlestick Chart")
    st.write("This is the candlestick chart content.")


    # Add Sidebar
    st.sidebar.title("Candlestick Chart Settings")
    st.sidebar.write("Adjust the settings for the candlestick chart here.")

    dbc = DBConnector()

    print(dbc.database_path)
    print(dbc.expiries_json_path)
    print(dbc.spot_parquet_path)
