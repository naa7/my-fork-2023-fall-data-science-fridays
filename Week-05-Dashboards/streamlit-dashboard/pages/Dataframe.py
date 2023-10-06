import streamlit as st
import pandas as pd


@st.cache_data
def load_homicide_data(fp):
    print("Loading data...")

    df = pd.read_csv(fp, encoding="ISO-8859-1")
    df = df.drop(columns=["uid", "victim_last", "victim_first", "lat", "lon"])

    df["reported_date"] = pd.to_datetime(
        df["reported_date"].astype(str), format="%Y%m%d", errors="coerce"
    ).dt.date

    default_date = pd.to_datetime("2007-01-01", format="%Y-%m-%d")
    df["reported_date"].fillna(default_date, inplace=True)
    df["victim_sex"].fillna("Unknown", inplace=True)

    return df


fp = "data/homicides.csv"
df = load_homicide_data(fp)
st.dataframe(df, use_container_width=True)
