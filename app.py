import streamlit as st
import pandas as pd
import pickle
import re
import nltk 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')
words = stopwords.words('english')
stemmer = PorterStemmer()

st.title('Streamlit Project')
st.write("News Classification")

with open('LogisticRegression.pickle','rb') as file:
    model = pickle.load(file)

data = st.text_area("Enter News for Classification")

if st.button('Submit'):
    d = {'news':[data]}
    df = pd.DataFrame(d)
    
    # ✅ Fix: df['predict_news'] → df['news']
    df['Predict news'] = list(map(lambda x: " ".join([i for i in x.lower().split() if i not in words]),df['news']))
    
    df['Predict news'] = df['Predict news'].apply(lambda x: " ".join([stemmer.stem(i) for i in re.sub("[^a-zA-Z]"," ",x).split() if i not in words]).lower())
    
    predict_news_cat = model.predict(df['Predict news'])

    st.write(predict_news_cat)