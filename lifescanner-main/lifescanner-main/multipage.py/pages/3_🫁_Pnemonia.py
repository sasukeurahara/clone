import streamlit as st
import os
import numpy as  np
import cv2
from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from PIL import Image

var = """
    <div class="header">
        
    </div>
    <span class="span">
       Pnemonia
    </span>
    <style>
    [data-testid="stAppViewContainer"]{
      background-repeat: no-repeat; 
      background-size: cover;
      background-image:url("https://images.unsplash.com/photo-1464618663641-bbdd760ae84a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8d2Vic2l0ZSUyMGJhY2tncm91bmR8ZW58MHx8MHx8fDA%3D");
      }
      .span{
        color:black;
        font-weight:bold;
        font-size:50px;
        # border:2px solid white;
        # border-radius:20px;
        # background-color:white;
     
      }
      
    </style>
 """
st.markdown(var,unsafe_allow_html=True)

with open('pages/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
   

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color:#2F4F4F;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Main Company Firewall</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Insta <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">YouTube</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Twitter</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)





uploaded_file = st.file_uploader("Choose a image file")
if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

from tensorflow.keras.models import load_model

model = load_model('C:/Users/bhanu/python/ModelPneumonia.h5')



def finall():

  pic= cv2.resize(opencv_image ,(224,224))
  pic1=[]
  pic1.append(pic)

  pic1= np.array(pic1)/255.0
  pict=model.predict(pic1)
  final = pd.DataFrame(pict)

  if(final.iloc[0,0]>final.iloc[0,1]):
      st.success('Safe from Pnemonia',icon="✅")
  else:
      st.error('Diagnosed by Pnemonia')

st.button('Predict',on_click= finall)