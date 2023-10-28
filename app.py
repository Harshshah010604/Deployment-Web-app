import streamlit as st
import joblib
model=joblib.load('spam-ham model')
st.title('Spam_Ham classifier')
ip=st.text_input('Enter your text')
op=model.predict([ip])
if st.button('Predict')
  st.title(op[0])
  st.ballons()
