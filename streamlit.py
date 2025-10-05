import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model  import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle

def manual_testing(news):
  testing_news={"text":[news]}
  new_def_test=pd.DataFrame(testing_news)
  new_def_test["text"]=new_def_test["text"].apply(wordopt)
  new_x_test=new_def_test["text"]
  new_xv_test=vectorization.transform(new_x_test)
  pred_LR=LR.predict(new_xv_test)
  pred_DT=DT.predict(new_xv_test)
  pred_GB=GB.predict(new_xv_test)
  pred_RF=RF.predict(new_xv_test)
  return print("\n\nLR Prediction: {} \nDT Prediction: {} \nGB Prediction: {} \nRF Prediction:"
 {}".format(output_label(pred_LR[0]),output_label(pred_GB[0]),output_label(pred_RF[0]))))

  pred_news=[]

  
st.title(' Fake News Detection System')
selected_news=st.selectbox('How would you like to predict?',)


