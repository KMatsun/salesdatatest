import streamlit as st
import pandas as pd

st.title("てすとぺ一じ")
st.write("サンプルデータ")
pd.read_csv('/data/data/com.termux/files/home/salesdata/sample.csv',index_col=0)

df = pd

st.write(df)
