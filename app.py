import pandas as pd
import seaborn as sns
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from seaborn import load_dataset
import pickle as pk
import streamlit as str


f = open('Day10//model.pkl', 'rb')
model = pk.load(f)

str.title("Enter The data")

Total_bill = str.text("Enter the total bill")
tip = str.text("Enter the tip")
sex = str.text("Enter your sex")
smoker = str.text("Are you a smoker")
day = str.text("What day of the week is it")
time = str.text("What is the Time Now ?")
size = str.text("How Many people are there in your group")

