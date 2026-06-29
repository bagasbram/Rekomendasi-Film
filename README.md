# 🎬 Movie Rating Prediction

Aplikasi ini dibuat menggunakan **Machine Learning** dan **Streamlit** untuk memprediksi **rating film (vote_average)** berdasarkan data film.

---

## Dataset

The Movies Dataset

https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset

---

## Algoritma

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

---

## Preprocessing

1. Data Cleaning
2. Feature Engineering
3. StandardScaler

---

## Feature

Input yang digunakan:

- Budget
- Revenue
- Runtime
- Popularity
- Vote Count

Feature tambahan:

```
Profit = Revenue - Budget
```

---

## Cara Menjalankan

Install library

```bash
pip install -r requirements.txt
```

Jalankan

```bash
streamlit run app.py
```

---

## Struktur Project

```
Movie-Rating-Prediction
│
├── app.py
├── requirements.txt
├── README.md
├── scaler.pkl
├── linear_regression.pkl
├── random_forest.pkl
└── gradient_boosting.pkl
```

---

## Author

Bagas Bramundito Suyitno

Universitas Amikom Yogyakarta