# Sentiment Analysis App

A simple Machine Learning and Natural Language Processing (NLP) based web application that predicts whether a given tweet or text is Positive, Negative, or Neutral.

The project was developed using Python, Scikit-learn, and Streamlit.

---

# Features

- Real-time sentiment prediction
- Positive, Negative, and Neutral classification
- Confidence score display
- Color-coded output interface
- Interactive Streamlit web application

---

# Technologies Used

- Python
- Natural Language Processing (NLP)
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- Streamlit
- Google Colab
- Jupyter Notebook

---

# Dataset Used

Twitter Sentiment Dataset from Kaggle.

Dataset contains:
- Positive tweets
- Negative tweets
- Neutral tweets

---

# Machine Learning Workflow

1. Import dataset
2. Perform text preprocessing
3. Convert text into numerical vectors using TF-IDF
4. Split dataset into training and testing data
5. Train Logistic Regression model
6. Evaluate model accuracy
7. Save trained model using Pickle
8. Build frontend using Streamlit
9. Predict sentiment from user input

---

# Project Structure

```text
project/
│
├── app.py
├── sentiment_model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
