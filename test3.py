import streamlit as st
import pandas as pd


st.title("Sample")
st.write("Sales")


url="https://drive.google.com/uc?id=11CUOWKfXvZDDGmgbkg4Ht5Kwxgk-mVh3"
df=pd.read_csv(url,index_col=0)

df["Sr_ruikei"]=df["Sales results"].cumsum()
st.line_chart(df["Sr_ruikei"])


window = 7
df["Srma"] = df["Sales results"].rolling(window).mean()
df["Lyma"] = df["Last year"].rolling(window).mean()


st.write(df)
st.line_chart(df)

import matplotlib.pyplot as plt
fig, ax1 = plt.subplots(1,1,figsize=(10,8))
ax2 = ax1.twinx()
ax3 = ax2.twinx()
ax4= ax3.twinx()

ax1.bar(df.index,df['Sales budget'],color='lightblue',label='Sales budget')

ax2.plot(df['Sales results'],linestyle='solid',color='k',marker='^',label='Sales results')

ax3.plot(df['Srma'],linestyle='solid',color='b',marker='^',label='Srma')

ax4.plot(df['Lyma'],linestyle='solid',color='m',marker='^',label='Lyma')



ax1.set_ylim(0,2000)
ax2.set_ylim(0,2000)
ax3.set_ylim(0,2000)
ax4.set_ylim(0,2000)


handler1, label1 = ax1.get_legend_handles_labels()
handler2, label2 = ax2.get_legend_handles_labels()
handler3, label3 = ax3.get_legend_handles_labels()
handler4, label4 = ax4.get_legend_handles_labels()

ax1.legend(handler1+handler2+handler3+handler4,label1+label2+label3+label4,borderaxespad=0)
ax1.grid(True)
fig.show()

st.write(fig)
