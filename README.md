# ✉️ Spam Email Detector

An end-to-end Machine Learning web application that classifies email messages as either **Spam** or **Ham (Safe)** in real time[cite: 1].

## 🌐 Live Application
👉 **[Click Here to Access the Live App](https://spam-email-detector-akshaj.streamlit.app/)**[cite: 1]

---

## 📌 Project Overview
* **Track:** Track B - Textual Classification Pipeline (NLP)[cite: 1]
* **Model:** Multinomial Naive Bayes (Optimized Hyperparameters)
* **Vectorizer:** TF-IDF Vectorizer (8,038 vocabulary size)
* **Web UI Framework:** Streamlit[cite: 1]

---

## ⚙️ System Architecture
1. **User Input:** Text entered into Streamlit UI[cite: 1].
2. **Text Preprocessing:** Lowercasing, removing special characters, stopword removal, and Porter Stemming.
3. **Vectorization:** Text transformed using `tfidf_vectorizer.pkl`[cite: 1].
4. **Prediction:** Transformed vector passed to `spam_model.pkl`[cite: 1].
5. **Output:** Real-time classification badge displayed on screen[cite: 1].

---

## 💻 Local Setup Instructions
To run this project on your local machine[cite: 1]:

```bash
# 1. Clone the repository
git clone [https://github.com/AkshajKamra/spam-email-detector.git](https://github.com/AkshajKamra/spam-email-detector.git)

# 2. Navigate into the folder
cd spam-email-detector

# 3. Install required dependencies
pip install -r requirements.txt

# 4. Run the Streamlit web app
streamlit run app.py
