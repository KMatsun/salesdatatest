import streamlit as st
import pandas as pd


st.title("ã¦ã™ã¨ãºä¸üüãüü")
st.write("ã‚µãƒ³ãƒ—ãƒ«ãƒüüüüã‚¿")


url="https://drive.google.com/uc?id=11CUOWKfXvZDDGmgbkg4Ht5Kwxgk-mVh3"
df=pd.read_csv(url,index_col=0)


window = 7
df["Srma"] = df["ales results"].rolling(window).mean()
df["Lyma"] = df["Last year"].rolling(window).mean()


st.write(df)
st.line_chart(df)

import matplotlib.pyplot as plt
fig, ax1 = plt.subplots(1,1,figsize=(10,8))
ax2 = ax1.twinx()
ax3 = ax2.twinx()

ax1.bar(df.index,df['Sales budget'],color='lightblue',label='Sales budget')

ax2.plot(df['Sales results'],linestyle='solid',color='k',marker='^',label='Sales results')

ax3.plot(df['Srma'],linestyle='solid',color='k',marker='^',label='Srma')

ax1.set_ylim(0,2000)
ax2.set_ylim(0,2000)
ax3.set_ylim(0,2000)


handler1, label1 = ax1.get_legend_handles_labels()
handler2, label2 = ax2.get_legend_handles_labels()
handler3, label3 = ax3.get_legend_handles_labels()

ax1.legend(handler1+handler2+handler3,label1+label2+label3,borderaxespad=0)
ax1.grid(True)
fig.show()

st.write(fig)
