# Week 5 – Linear Regression From Scratch

## Overview
This project implements **Linear Regression from scratch** on the **California Housing Dataset (Kaggle version)**. The objective is to predict **median house values** using numerical features such as median income, house age, total rooms, population, and more.  

All model components — including **train-test split, feature scaling, gradient descent, cost calculation, and evaluation metrics** — are implemented **manually without using any sklearn model training functions**.  

This notebook demonstrates a complete **end-to-end ML pipeline** suitable for fellowship submission.

---

## Dataset
- **Name:** California Housing Dataset (Kaggle)  
- **Source:** [Kaggle](https://www.kaggle.com/datasets/camnugent/california-housing-prices)  
- **File:** `housing.csv`  
- **Features:** 
  - `longitude`, `latitude`, `housing_median_age`, `total_rooms`, `total_bedrooms`, `population`, `households`, `median_income`
- **Target:** `median_house_value`  
- **Preprocessing:**  
  - Dropped categorical column `ocean_proximity`  
  - Standardization performed manually  
  - Train-test split implemented manually

---

## Implementation Highlights

1. **Train-Test Split (Manual)**  
   Random 80/20 split.

2. **Feature Scaling (Standardization)**  
   Ensures stable and fast convergence for gradient descent.

3. **Linear Regression (Gradient Descent)**  
   - Fully vectorized implementation  
   - Parameters (`weights` and `bias`) updated iteratively  
   - Cost function: Mean Squared Error (MSE)  
   - Tracks **loss convergence** over epochs

4. **Evaluation Metrics (From Scratch)**  
   - Mean Squared Error (MSE)  
   - R² Score

5. **Normal Equation (Closed-Form Solution)**  
   Analytical solution for comparison with gradient descent.

6. **Model Visualization**  
   - Loss convergence curve  
   - Actual vs Predicted scatter plot  
   - Residual distribution plot  
   - Residuals vs Predicted plot  
   - Feature importance plot (learned weights)

---

## How to Run

1. Open the notebook in **Google Colab** or **Jupyter**.  
2. Upload the `housing.csv` file.  
3. Run cells in order:  
   - Data loading → Preprocessing → Model definition → Training → Evaluation → Visualization  
4. Recommended workflow:  
   - Runtime → Restart & Run All  
   - Ensure zero errors before submission.

---

## Repository Structure


Main-Fellowship-Repo/
│
├── README.md
└── Week_5/
├── linear_regression_from_scratch.ipynb
├── data/
│ └── housing.csv (optional, can be .gitignored)
├── images/ (optional, for plots)
└── report.md (optional explanation file)


---

## Key Observations

- Gradient Descent converges smoothly after feature standardization.  
- Residuals are centered around 0 — good fit.  
- Feature weights indicate variables with the largest impact on median house value.  
- Normal Equation provides similar results but is computationally heavier for large datasets.

---

## Lessons Learned

1. Feature scaling is crucial for gradient-based optimization.  
2. Manual implementation strengthens understanding of ML internals.  
3. Visualization is essential for diagnosing model performance and assumptions.  
4. Even simple regression requires careful preprocessing on real-world datasets.

---

## References

1. Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow – Aurélien Géron  
2. [Microsoft ML for Beginners](https://microsoft.github.io/ML-For-Beginners/#/1-Introduction/README)  
3. [Kaggle – California Housing Dataset](https://www.kaggle.com/datasets/camnugent/california-housing-prices)  

---

## Author

**Hizar Abdullah**  
- BS in Artificial Intelligence – COMSATS University Islamabad  
- Digital Marketing & Data Science Enthusiast  
- Contact: khizerarena77@gmail.com | +92 349 9224226