import yfinance as yf
import streamlit as st
import pandas as pd 

st.write(""" # Simple Stock Price App

Shown are the **stock prices** and **volume** of Tesla""")
tickerSymbol ='TSLA'

tickerData=yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(perdiod='1d', start = '2010-5-31', end = '2021-1-21')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


st.button("Re-run")
