import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model=pickle.load(open('diabetes_model','rb'))

heart_model=pickle.load(open('Hear_model','rb'))

parkinsons_model=pickle.load(open('parkinson_model','rb'))

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Diseases Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity','heart','person'],
                           default_index=0)
