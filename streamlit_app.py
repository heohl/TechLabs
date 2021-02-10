import yfinance as yf
import streamlit as st
import pandas as pd 
from datetime import date

st.write(""" # Simple Stock Price App

Shown are the **stock prices** and **volume** of Tesla""")
tickerSymbol ='TSLA'

tickerData=yf.Ticker(tickerSymbol)

heute=date.today()
tickerDf = tickerData.history(perdiod='1d', start = '2015-5-31', end = heute)

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


st.button("Re-run")
