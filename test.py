import streamlit as st
import pandas as pd


st.title("てすとぺ一じ")
st.write("サンプルデータ")

url="https://drive.google.com/file/d/1PgxzIlQpnFbi5jAPLpoNwzSeMap-pJBT/view?usp=drivesdk"
df=pd.read_csv(url,index_col=0)


st.write(df)
st.line_chart(df)

import matplotlib.pyplot as plt
fig, ax1 = plt.subplots(1,1,figsize=(10,8))
ax2 = ax1.twinx()
ax1.bar(df.index,df['予算'],color='lightblue',label='予算')
ax2.plot(df['実績'],linestyle='solid',color='k',marker='^',label='実績')
ax1.set_ylim(0,2000)
ax2.set_ylim(0,2000)
handler1, label1 = ax1.get_legend_handles_labels()
handler2, label2 = ax2.get_legend_handles_labels()
ax1.legend(handler1+handler2,label1+label2,borderaxespad=0)
ax1.grid(True)
fig.show()

st.write(fig)
