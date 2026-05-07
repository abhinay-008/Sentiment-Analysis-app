import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Page config
st.set_page_config(page_title="Sentiment Analysis", layout="wide")

st.title("Sentiment Analysis App")

# Create 2 columns
col1, col2 = st.columns(2)

# LEFT SIDE -> INPUT
with col1:

    st.subheader("Enter Tweet")

    review = st.text_area(
        "",
        height=250,
        placeholder="Type your tweet here..."
    )

    predict = st.button("Predict")


# RIGHT SIDE -> OUTPUT
with col2:

    st.subheader("Prediction Result")

    if predict:

        review_vector = vectorizer.transform([review])

        prediction = model.predict(review_vector)[0]

        # NEGATIVE
        if prediction == 0:

            st.markdown(
                """
                <div style="
                    background-color:#ff4b4b;
                    padding:40px;
                    border-radius:10px;
                    text-align:center;
                    color:white;
                    font-size:35px;
                    font-weight:bold;
                ">
                    NEGATIVE
                </div>
                """,
                unsafe_allow_html=True
            )

        # NEUTRAL
        elif prediction == 1:

            st.markdown(
                """
                <div style="
                    background-color:gray;
                    padding:40px;
                    border-radius:10px;
                    text-align:center;
                    color:white;
                    font-size:35px;
                    font-weight:bold;
                ">
                    NEUTRAL
                </div>
                """,
                unsafe_allow_html=True
            )

        # POSITIVE
        else:

            st.markdown(
                """
                <div style="
                    background-color:green;
                    padding:40px;
                    border-radius:10px;
                    text-align:center;
                    color:white;
                    font-size:35px;
                    font-weight:bold;
                ">
                    POSITIVE
                </div>
                """,
                unsafe_allow_html=True
            )