
import pickle 
import streamlit as st 

st.title("DRUG GUARD")


st.image("https://imgs.search.brave.com/H_NnKPrBTK5RJ2xsXmyyNDiwwunRJSGZ8pmw7ZqYORg/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRs/aW5lcGx1cy5nb3Yv/aW1hZ2VzL0hlcm9p/bi5qcGc")

age = st.selectbox("Age",["15 to 22 years", "between 22 to 35 years"])
#workclass = st.selectbox("Working Class", ["Federal-gov","Local-gov","Never-worked","Private","Self-emp-inc","Self-emp-not-inc","State-gov","Without-pay"]) 
education = st.selectbox("Education",["Undergraduate","10th Class"]) 
livewith = st.selectbox("Live With",["Hostel/Hall","With Family/Relatives"]) 
law = st.selectbox("Conflict with law",["Yes","No"])
spent = st.selectbox("Spend most time",["Alone","Friends","Family/ Relatives"])
fail = st.selectbox("Failure in life",["Yes","No"])
family = st.selectbox("Family relationship",["Satisfactory","Average","Communcaiton gap",])
fin = st.selectbox("Financials of family",["Solvent","Medium","Rich / Strong","Poor / weak"])
work = st.selectbox("Satisfied with workplace",["Yes","No"])
court = st.selectbox("Case in court",["Yes","No"])
smoke =  st.selectbox("Smoking",["Yes, every day","Yes, occasionally","No, I don't"])
friend =  st.selectbox("Friends influence",["Yes, often they do","No, they don't"])

# wow = ["Yes","NO" ]
if st.button('Predict'):
    if fail == "Yes":
        st.success("Maybe")
    else:
        st.success("Maybe not")

