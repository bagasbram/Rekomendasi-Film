import streamlit as st
import joblib
import numpy as np

st.set_page_config(
    page_title="Movie Rating Prediction",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Rating Prediction")
st.write("Prediksi **Rating Film (Vote Average)** menggunakan Machine Learning.")

# ==========================
# PILIH MODEL
# ==========================

model_option = st.selectbox(
    "Pilih Model Machine Learning",
    (
        "Linear Regression",
        "Random Forest"
    )
)

if model_option == "Linear Regression":
    model = joblib.load("linear_regression.pkl")
else:
    model = joblib.load("random_forest.pkl")

# Load scaler
scaler = joblib.load("scaler.pkl")

st.divider()

st.subheader("Input Data Film")

budget = st.number_input(
    "Budget",
    min_value=0.0,
    value=1000000.0
)

revenue = st.number_input(
    "Revenue",
    min_value=0.0,
    value=5000000.0
)

runtime = st.number_input(
    "Runtime (minutes)",
    min_value=1.0,
    value=120.0
)

popularity = st.number_input(
    "Popularity",
    min_value=0.0,
    value=10.0
)

vote_count = st.number_input(
    "Vote Count",
    min_value=0.0,
    value=100.0
)

# Feature Engineering
profit = revenue - budget

st.write(f"**Profit:** {profit:,.0f}")

if st.button("Prediksi Rating"):

    data = np.array([[
        budget,
        revenue,
        runtime,
        popularity,
        vote_count,
        profit
    ]])

    data = scaler.transform(data)

    prediction = model.predict(data)

    st.success(
        f"🎬 Prediksi Rating Film: **{prediction[0]:.2f}/10**"
    )

st.divider()

st.caption(
    "Machine Learning Project | The Movies Dataset | Linear Regression & Random Forest | Streamlit"
)
