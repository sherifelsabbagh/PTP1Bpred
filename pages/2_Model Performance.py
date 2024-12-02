import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
  page_title='Model performance',
  initial_sidebar_state='expanded')

st.title('PTP1B Activity Prediction App')
#st.info('The LRRK2 Activity Prediction App can be used to predict whether a  molecule is active or inactive for lrrk2 target protein .')
st.subheader("Model Performance")
#st.write("We chosed PubChem fingerprints for building the model using RandomForest Classifier. SMOTE technique was applied to overcome imbalance problem.")


with st.expander('Performance', expanded=True):
    st.write("Sensitivity (SN) : 85%")
    st.write("Specificity (SP) : 78%")
    st.write("Accuracy (Q) : 82%")
    Auc_i = Image.open('AUC.png')
    st.image(Auc_i, use_column_width=True)
