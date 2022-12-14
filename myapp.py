# -*- coding: utf-8 -*-
"""myapp.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pHS_f-K7GJ79asy-P3K5qGwIUjQ8m0Ok
"""

!pip install streamlit

import streamlit as st
import pickle

st.__version__

pickle_in = open("classification.pkl","rb")
classification=pickle.load(pickle_in)

def main():
  st.title("#Backorder Prediction")
  html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Backorder Prediction ML App </h2>
    </div>
    """
  national_inv = st.text_input("Enter Inventory","Kindly enter a numerical value")
  in_transit_qty = st.text_input("Enter In-transit Quantity","Kindly enter a numerical value")
  forecast_3_month = st.text_input("Enter forecasted sales for next 3 months","Kindly enter a numerical value")
  forecast_6_month = st.text_input("Enter forecasted sales for next 6 months","Kindly enter a numerical value")
  sales_1_month = st.text_input("Enter sales quantity for previous month","Kindly enter a numerical value")
  sales_3_month = st.text_input("Enter sales quantity for last 3 months","Kindly enter a numerical value")
  sales_6_month = st.text_input("Enter sales quantity for last 6 months","Kindly enter a numerical value")
  sales_9_month = st.text_input("Enter sales quantity for last 9 months","Kindly enter a numerical value")
  min_bank = st.text_input("Enter minimum recommended amt of the item to be present in stock","Kindly enter a numerical value")
  potential_issue= st.radio("Is there a Potential Issue?",("No","Yes"))
  if(potential_issue == "Yes"):
    pot_issue = 1
  else:
    pot_issue = 0
  pieces_part_due = st.text_input("Enter pieces that were overdue from source","Kindly enter a numerical value")
  perf_6_month_avg =  st.text_input("Enter source performance in past 6 months","Kindly enter a numerical value")
  local_bo_qty = st.text_input("Enter amount of stock overdue","Kindly enter a numerical value")
  deck_risk= st.radio("Is there any Deck Risk?",("No","Yes"))
  if(deck_risk == "Yes"):
    deckrisk = 1
  else:
    deckrisk = 0
  ppap_risk = st.radio("Is there PPAP Risk?",("No","Yes"))
  if(ppap_risk == "Yes"):
    ppaprisk = 1
  else:
    ppaprisk = 0
  stop_auto_buy = st.radio("Should we stop Auto Buy?",("No","Yes"))
  if(stop_auto_buy == "Yes"):
    stopautobuy = 1
  else:
    stopautobuy = 0
  rev_stop = st.radio("Select Rev_Stop value?",("No","Yes"))
  if(rev_stop == "Yes"):
    revstop = 1
  else:
    revstop = 0

arr = ["national_inv","in_transit_qty","forecast_3_month","forecast_6_month","sales_1_month","sales_3_month","sales_6_month","sales_9_month","min_bank","pot_issue","pieces_part_due","perf_6_month_avg","local_bo_qty","deckrisk","ppaprisk","stopautobuy","revstop"]

if st.button("Predict if it will go on backorder!"):
    result = classification.predict([arr])
    if result:
      st.text("Item will not go on Backorder")
    else:
      st.text("Item will go on Backorder")

if __name__=='__main__':
  main()

#!streamlit run myapp.py

