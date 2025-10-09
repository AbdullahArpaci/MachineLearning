# Iris Dataset Machine Learning Analysis

This project focuses on **classifying Iris flowers** using the famous Iris dataset. It includes **data analysis, visualization, preprocessing, and applying basic machine learning models** for classification.

---

## 📂 Dataset

- File: `11-iris.csv`  
- Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris)  

### Features

| Column         | Description                                      | Type     |
|----------------|--------------------------------------------------|---------|
| Id             | Observation ID                                   | int     |
| SepalLengthCm  | Sepal length (cm)                                | float   |
| SepalWidthCm   | Sepal width (cm)                                 | float   |
| PetalLengthCm  | Petal length (cm)                                | float   |
| PetalWidthCm   | Petal width (cm)                                 | float   |
| Species        | Flower species (`Iris-setosa`, `Iris-versicolor`, `Iris-virginica`) | string |

- The dataset contains **150 observations** and **6 columns**.

---

## 📊 Exploratory Data Analysis (EDA)

- Summary statistics were obtained using `describe()` and `info()`.  
- No missing values are present.  
- The `Species` column contains three unique classes.  
- Visualization techniques used:
  - Histograms and boxplots
  - Pairplots (`sns.pairplot`) to show relationships between features
  - Scatterplots for Sepal (`SepalLengthCm` vs `SepalWidthCm`) and Petal (`PetalLengthCm` vs `PetalWidthCm`) dimensions

---

## 🔢 Preprocessing

- The `Id` column was removed as it is not informative for classification.  
- The `Species` column was converted to numeric labels using **Ordinal Encoding**:  

- Features were **scaled** using StandardScaler where required for machine learning models.

---

## 🤖 Machine Learning Models

The dataset was split into **80% training and 20% testing**. The following classification models were trained and evaluated:

1. **Gaussian Naive Bayes (GNB)**  
2. **Logistic Regression (LR)**  
3. **Support Vector Classifier (SVC)**  

### Evaluation Metrics

- **Accuracy**
- **Confusion Matrix**
- **Classification Report (Precision, Recall, F1-Score)**

**Performance on the test set:**

| Model                     | Accuracy |
|----------------------------|---------|
| Gaussian Naive Bayes       | 100%    |
| Logistic Regression        | 100%    |
| Support Vector Classifier  | 100%    |

> All models achieved perfect accuracy due to the simplicity and separability of the Iris dataset.

---

## ⚙️ Usage

1. Clone the repository:
```bash
git clone <your-repo-url>
