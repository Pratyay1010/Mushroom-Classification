import streamlit as st
import pickle

data = pickle.load(open("./Pickle Files/dataset.pkl","rb"))
model = pickle.load(open("./Pickle Files/model.pkl","rb"))

x=[]
j=0
for i in data.keys():
    if j!=0:
        x.append(i)
    j+=1



st.title("Mushroom Classification System")

options=[]
for i in x:
    options.append(st.selectbox(i, (tuple(data[i]))))

for i in options:
    st.write(i)