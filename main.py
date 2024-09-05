import streamlit as st 
from streamlit_option_menu import option_menu 
import os 
working_directory=os.path.dirname(os.path.abspath(__file__))


#setting the page configuration 
st.set_page_config(
  page_title="Gemini-AI"
  , 
  layout='centered'
)

with st.sidebar :
     selected=option_menu(menu_title="GEMINI-AI",options=["chatbot","Image Captioning ","Embed text","Ask me Anything"] ,       menu_icon="robot",icons=['chat-dots-fill','card-image','card-text','question-diamond-fill'] ,
                          default_index=0)