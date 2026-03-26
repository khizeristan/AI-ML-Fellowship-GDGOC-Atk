# Week 2 Titanic Dataset Exploratory Data Analysis (EDA)

## Dataset Overview
- Dataset Titanic Passenger Data  
- Source [Kaggle Titanic Dataset](httpswww.kaggle.comdatasetsyasserhtitanic-dataset)  
- Rows 891  
- Columns 12+ (PassengerId, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked, etc.)  
- Target Variable `Survived` (0 = No, 1 = Yes)  

The dataset contains information about passengers aboard the Titanic, including personal, travel, and survival data.

---

## Tools & Libraries Used
- Python 3.x  
- NumPy – for numerical operations  
- Pandas – for data loading, cleaning, and processing  
- Matplotlib – for static visualizations  
- Seaborn – for advanced plotting and statistical visualizations  

---

## Project Steps

### 1. Data Loading & Inspection
- Loaded the dataset into a Pandas DataFrame.  
- Inspected the first few rows, data types, and missing values.  

### 2. Data Cleaning & Preprocessing
- Filled missing `Age` values with the median.  
- Filled missing `Embarked` values with the mode.  
- Dropped the `Cabin` column due to too many missing values.  
- Encoded categorical variables (`Sex` and `Embarked`).  
- Created a new feature `FamilySize = SibSp + Parch + 1`.

### 3. Exploratory Data Analysis (EDA)
- Univariate Analysis Examined distributions of `Survived` and `Age`.  
- Bivariate Analysis Investigated survival patterns by `Sex`, `Pclass`, and `FamilySize`.  
- Correlation Analysis Plotted a heatmap of numeric features to identify relationships with `Survived`.  
- Additional Insights Visualized Age distribution by survival status and family size trends.  

---

## Key Observations
- Female passengers had a higher survival rate than males.  
- Passengers in first-class (`Pclass = 1`) survived more often than those in lower classes.  
- Younger passengers and passengers with smaller families had slightly better chances of survival.  
- `Sex` and `Fare` show strong correlation with survival.  

---

## How to Run the Notebook
1. Open `Week2_Titanic_EDA.ipynb` in Google Colab or Jupyter Notebook.  
2. Ensure that the dataset CSV (`Titanic-Dataset.csv`) is in the same directory, or update the file path accordingly.  
3. Run all cells sequentially.  
4. Required Python packages  
   ```bash
   pip install numpy pandas matplotlib seaborn
