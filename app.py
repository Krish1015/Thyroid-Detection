# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pickle
import streamlit as st
import numpy as np
st.title("Classification Model")
st.subheader('Inputs')
col1, col2, col3 = st.columns(3)

with col1:
   age = st.number_input("Enter your age",step= 1)
   sex_options = [0,1]
   binary_options = [0, 1]
   sex = st.selectbox("Sex ('0' for Female and '1' for Male)",options=sex_options)
   thyroid_surgery = st.selectbox("Thyroid surgery (True : 1 , False : 0)",options=binary_options)
   query_hypothyroid = st.selectbox("Query hypothyroid (T : 1 , F : 0)",options=binary_options)
   goitre = st.selectbox("Goitre (T : 1 , F : 0)",options=binary_options)
   psych = st.selectbox(" psychiatric disorder (T : 1 , F : 0)",options=binary_options)
   TSH_measured = st.selectbox("TSH measured (T : 1 , F : 0)",options=binary_options)
   TT4_measured = st.selectbox("TT4 measured (T : 1 , F : 0)",options=binary_options)
   T4U = st.number_input("T4U vales",min_value=0,max_value=5)





with col2:
    on_thyroxine = st.selectbox("On thyroxine (True : 1 , False : 0)", options=binary_options)
    query_on_thyroxine = st.selectbox("Query on thyroxine (True : 1 , False : 0)", options=binary_options)
    I131_treatment = st.selectbox("I131 treatment (T : 1 , F : 0)",options=binary_options)
    query_hyperthyroid = st.selectbox("Query huperthyroid (T : 1 , F : 0)",options=binary_options)
    hypopituitary = st.selectbox("Hypopituitary (T : 1 , F : 0)",options=binary_options)
    TSH = st.number_input("TSH",min_value=0,max_value=550,step = 1)
    T3_measured = st.selectbox("T3 measured (T : 1 , F : 0)",options=binary_options)
    TT4 = st.number_input("TT4 values", min_value=0,max_value=530)
    referal_options = ['referral source_SVHC','referral source_SVHD','referral source_SVI',
                       'referral source_other']
    referal = st.selectbox('Referel options',options=referal_options)
    ref = [0,0,0,0]
    for i in range(len(referal_options)):
        if  referal_options[i] == referal:
            ref[i] = 1



with col3:
    on_antithyroid_medication = st.selectbox("On antithyroid medication (T : 1 , F : 0)",options=binary_options)
    sick = st.selectbox("Sick (True : 1 , False : 0)",options=binary_options)
    pregnant = st.selectbox("Pregnant (True : 1 , False : 0)",options=binary_options)
    lithium = st.selectbox("Lithium (True : 1 , False : 0)",options=binary_options)
    tumor = st.selectbox("Tumor (True : 1 , False : 0)",options=binary_options)
    T3 = st.number_input("T3 value",min_value=0.0,max_value=50.0,step=0.1)
    T4U_measured = st.selectbox("T4U measured (T : 1 , F : 0)",options=binary_options)
    FTI = st.number_input("FTI",min_value=0,max_value=450)


input_list = [age,sex,on_thyroxine,query_on_thyroxine,on_antithyroid_medication,sick,pregnant,thyroid_surgery
              ,I131_treatment,query_hypothyroid,query_hyperthyroid,lithium,goitre,tumor,hypopituitary,psych
              ,TSH_measured,TSH,T3_measured,T3,TT4_measured,TT4,T4U_measured,T4U,FTI,ref[0],ref[1],ref[2],ref[3]]
print(len(input_list))



def make_prediction(input_list):
    with open("model.pkl", "rb") as f:
        clf  = pickle.load(f)
        preds = clf.predict([input_list])
    return preds
results = make_prediction(input_list)
if st.button("Predict"):
    if results == 1:
        st.warning("Hi You have potential Thyroid")
    else:
        st.success("Hi you are safe form Throid")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
