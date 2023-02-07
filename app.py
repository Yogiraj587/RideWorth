import streamlit as st
import pickle
import numpy as np
    
def load_model():
    model = pickle.load(open("C:/Users/Yogiraj/VS Code/EndtoEndMl/Streamlit/Cars/carprice.pkl","rb"))
    return model

model = load_model()

st.header("Car Price Prediction App")
st.subheader("Made with Streamlit and Python")
st.write("This app predicts the price of a car based on the following parameters")
## fueltype
st.sidebar.subheader("Select Fueltype")
fueltype = st.sidebar.selectbox(" ", ['gas','diesel'])
if fueltype == 'gas':
    fueltype_inp = 0
else:
    fueltype_inp = 1

st.sidebar.write("Fuel Type -- ",fueltype_inp)

### carbody
st.sidebar.subheader("Select the carbody")
carbody = st.sidebar.selectbox(" ",['convertible','hatchback','sedan','wagon','hardtop'])
if carbody == 'convertible':
    carbody_inp = 0
elif carbody == 'hatchback':
    carbody_inp = 1
elif carbody == 'sedan':
    carbody_inp = 2
elif carbody == 'wagon':
    carbody_inp = 3
elif carbody == 'hardtop':
    carbody_inp = 4

st.sidebar.write("Car Body --",carbody_inp)

st.sidebar.subheader("Select the enginetype")
enginetype = st.sidebar.selectbox(" ",['dohc','ohcv','ohc','l','rotor','ohcf','dohcv'])
if enginetype == 'dohc':
    enginetype_inp = 0
elif enginetype == 'ohcv':
    enginetype_inp = 1
elif enginetype == 'ohc':
    enginetype_inp = 2
elif enginetype == 'l':
    enginetype_inp = 3
elif enginetype == 'rotor':
    enginetype_inp = 4
elif enginetype == 'ohcf':
    enginetype_inp = 5
elif enginetype == 'dohcv':
    enginetype_inp = 6

st.sidebar.write("Engine Type --",enginetype_inp)

st.sidebar.subheader("Select the Cylindernumber")
cylindernumber  = st.sidebar.selectbox(" ",["four","six","five","three","twelve","two","eight"])
if cylindernumber == 'four':
    cylindernumber_inp = 0
elif cylindernumber == 'six':
    cylindernumber_inp = 1
elif cylindernumber == 'five':
    cylindernumber_inp = 2
elif cylindernumber== 'three':
    cylindernumber_inp = 3
elif cylindernumber == 'twelve':
    cylindernumber_inp = 4
elif cylindernumber == 'two':
    cylindernumber_inp = 5
elif cylindernumber == 'eight':
    cylindernumber_inp = 6

st.sidebar.write("Cylinder Number --",cylindernumber_inp)

carwidth = st.number_input("Carwidth",60,100)
carlength = st.number_input("Carlength",140,240)
curbweight = st.number_input("Curbweight",1400,5000)
enginesize = st.number_input("Engine size",60,350)
boreratio = st.number_input("Bore ratio",2.5,4.0)
horsepower = st.number_input("Horsepower",10,300)
wheelbase = st.number_input("wheelbase",86,130)
fueleconomy = st.number_input("fueleconomy",14,60)


if st.checkbox("PREDICT"):
    pred = model.predict([[fueltype_inp,carbody_inp,enginetype_inp,cylindernumber_inp,carwidth,carlength,curbweight,enginesize,boreratio,horsepower,wheelbase,fueleconomy]])
    for i in pred:
        st.write("Your Car price is: ",round(i,3))
        st.write("Good Luck with your new car.....")
