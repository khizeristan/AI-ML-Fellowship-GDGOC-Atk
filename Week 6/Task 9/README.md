# Iris Dataset – Model Evaluation & Bias-Variance Analysis

## 📌 Project Overview

This project demonstrates evaluation of machine learning models using the Iris dataset.  
The focus is on:

- Classification model evaluation metrics
- Bias and Variance analysis
- Underfitting vs Overfitting
- Cross-validation and learning curves

The dataset used is the Iris Dataset.

---

## 📊 Dataset Description

The Iris dataset contains 150 samples of iris flowers belonging to three classes:

- Setosa
- Versicolor
- Virginica

### Features:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

### Target:
- Species (3 classes)

---

## 🤖 Models Implemented

The following classification algorithms were applied:

1. Logistic Regression  
2. Decision Tree (Shallow – Underfitting Example)  
3. Decision Tree (Deep – Overfitting Example)  
4. Random Forest Classifier  

---

## 📈 Evaluation Metrics Used

The following metrics were used to evaluate performance:

- Accuracy
- Precision (Macro Average)
- Recall (Macro Average)
- F1 Score (Macro Average)
- Confusion Matrix
- Cross-Validation Accuracy

---

## 🧠 Bias–Variance Analysis

### Underfitting (High Bias)
- Decision Tree with max_depth=1
- Model too simple
- Low performance

### Overfitting (High Variance)
- Deep Decision Tree (no depth restriction)
- High training accuracy
- Lower generalization performance

### Balanced Model
- Random Forest
- Reduced variance
- Better generalization

---

## 📊 Learning Curve

A learning curve was plotted to analyze:

- Training accuracy
- Validation accuracy
- Model generalization behavior

---

## 🔍 Conclusion

- Simple models may underfit the data.
- Complex models may overfit.
- Ensemble methods like Random Forest provide better balance.
- Cross-validation improves reliability of evaluation.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 🚀 How to Run

1. Extract iris.zip (if using zipped dataset)
2. Open the Jupyter Notebook
3. Run all cells

---

## 👨‍💻 Author

Hizar Abdullah  
Bachelor's in Artificial Intelligence  