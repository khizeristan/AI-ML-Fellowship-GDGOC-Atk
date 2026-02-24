# Logistic Regression from Scratch - Breast Cancer Classification

## Overview

This project implements **Logistic Regression** for classifying breast cancer tumors (Benign vs Malignant) using the **Breast Cancer Wisconsin Dataset**.  

The implementation includes:

- Logistic Regression **from scratch** using **NumPy**.
- Comparison with **scikit-learn** Logistic Regression.
- Model evaluation and visualization.

---

## Dataset

- **Source:** Breast Cancer Wisconsin (Diagnostic) Dataset
- **Shape:** 569 rows × 32 columns
- **Features:** 30 numeric features describing cell nuclei
- **Target:** `diagnosis` (`M` = Malignant → 1, `B` = Benign → 0)
- **ID Column:** `id` (dropped before training)

---

## Implementation Details

### 1. Data Preprocessing

- Dropped `id` column
- Converted `diagnosis` to numeric (`M` → 1, `B` → 0)
- Train/Test split: 80% train, 20% test
- Feature scaling using `StandardScaler`

### 2. Logistic Regression from Scratch

- **Sigmoid Function:** Converts linear combination of features into probability
- **Cost Function:** Binary Cross-Entropy (Log Loss)
- **Gradient Descent:** Optimizes weights to minimize cost
- **Prediction:** Threshold at 0.5 for binary classification

### 3. Scikit-Learn Comparison

- `LogisticRegression(max_iter=5000)` used for comparison
- Ensures our scratch implementation matches standard library performance

---

## Model Evaluation & Visualization

1. **Cost vs Iterations** – Shows convergence of gradient descent
2. **Confusion Matrix** – True/False Positives/Negatives
3. **ROC Curve** – AUC evaluates classifier performance
4. **Feature Importance** – Top features by absolute weight
5. **Probability Distribution** – Shows separation of predicted probabilities

> Optional: 2D decision boundary for visualization using `radius_mean` and `texture_mean`.

---

## Results

- **Train Accuracy:** ~97%
- **Test Accuracy:** ~96–98%
- **Top Features:** `concave points_worst`, `area_worst`, `perimeter_worst`, etc.
- **ROC AUC:** ~0.99

> This demonstrates that Logistic Regression is highly effective on this dataset.

---

## How to Run

1. Clone the repository:

```bash
git clone <your_repo_url>

Open the notebook:

cd Week5-LogisticRegression
jupyter notebook
# or open in Google Colab

Run all cells sequentially.

References

Hands-On Machine Learning with Scikit-Learn & TensorFlow (Book PDF
)

Microsoft ML for Beginners (Intro to ML
)

Breast Cancer Wisconsin (Diagnostic) Dataset – UCI Machine Learning Repository

Author

Hizar Abdullah – COMSATS University Islamabad, BS AI, Fellowship Participant
Contact: khizerarena77@gmail.com
 | +92 349 9224226