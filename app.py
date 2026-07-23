import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download NLTK data inside app
nltk.download('stopwords')
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

# Define the exact text cleaning function from Week 3
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
    words = text.split()
    words = [ps.stem(word) for word in words if word not in stop_words]
    return ' '.join(words)

# Page configuration
st.set_page_config(page_title="Spam Email Detector", page_icon="✉️")

st.title("✉️ Spam Email Detector")
st.write("Enter any email or message text below to check if it's **Ham** or **Spam**.")

# Load the exported models
@st.cache_resource
def load_artifacts():
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    model = joblib.load('spam_model.pkl')
    return vectorizer, model

tfidf, model = load_artifacts()

# User Input Box
user_input = st.text_area("Email Content", placeholder="Type or paste message here...", height=150)

if st.button("Analyze Message"):
    if user_input.strip() == "":
        st.warning("Please enter a sentence or email to test!")
    else:
        # Preprocess, Transform, and Predict
        cleaned_input = clean_text(user_input)
        vectorized_input = tfidf.transform([cleaned_input])
        prediction = model.predict(vectorized_input)[0]
        
        # Display Results
        st.subheader("Result:")
        if prediction.lower() == 'spam':
            st.error("🚨 **SPAM DETECTED!** Be careful with this email.")
        else:
            st.success("✅ **SAFE (HAM)!** This email looks legitimate.")