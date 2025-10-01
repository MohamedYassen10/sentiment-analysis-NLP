# Sentiment Analysis with NLP 🚀

This project demonstrates **text preprocessing, classical machine learning modeling, and deployment of NLP systems**.
It includes step-by-step experiments, model comparison, and a working API to serve predictions.

---

## 📂 Project Structure

* **Sentiment Analysis.ipynb** → Jupyter Notebook with preprocessing, experiments, and results.
* **app.py** → FastAPI script to serve predictions from the trained model.
* **sentiment_model.pkl** → Saved pipeline (vectorizer + classifier).

---

## ⚙️ Features

* Text preprocessing (tokenization, stopwords removal, etc.)
* Representations: **BoW, TF-IDF, Word2Vec**
* Model training & evaluation
* API endpoint (`/predict`) for real-time sentiment classification

---

## 📝 Report Summary

* **Preprocessing:** Lowercasing, tokenization, stopword removal.
* **Models Tested:** Logistic Regression with BoW, TF-IDF, Word2Vec.
* **Best Model:** TF-IDF + Logistic Regression (highest accuracy).
* **Deployment:** Exposed as a FastAPI service.
