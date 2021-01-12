import streamlit as st
import pandas as pd

st.title("てすとぺ一じ")
st.write("サンプルデータ")

df = pd.DataFrame({
  '1列':[11, 4562, 563, 4324, 5],
  '2列':[1, 2, 3, 4, 5]
})

st.write(df)
st.write("wifiの時だけ成功？")
st.write("Network URL: http://10.114.152.116:8501  External URL: http://103.5.140.148:8501")
st.write("公開されるuRlは変わるのか?!")

