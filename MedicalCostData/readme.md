# Insurance Charges Prediction

This project analyzes an **insurance dataset** and predicts insurance charges using multiple regression models. The workflow includes **exploratory data analysis (EDA), data preprocessing, feature encoding, scaling**, and applying various machine learning models.

---

## 📂 Dataset

- File: `insurance.csv`  
- Source: [Kaggle Insurance Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)  

### Features

| Column       | Description                                    | Type    |
|--------------|------------------------------------------------|--------|
| age          | Age of the insured                              | int    |
| sex          | Gender (`male`, `female`)                       | object |
| bmi          | Body Mass Index                                 | float  |
| children     | Number of children                              | int    |
| smoker       | Smoker status (`yes`, `no`)                     | object |
| region       | Residential region (`southwest`, `southeast`, `northwest`, `northeast`) | object |
| charges      | Insurance charges (target variable, USD)       | float  |

- The dataset contains **1,338 observations** and **7 columns**.  
- There are **no missing values** in the dataset.

---

## 📊 Exploratory Data Analysis (EDA)

- Age distribution is fairly balanced; the youngest insured is 18 and the oldest is 64.  
- Most insured individuals are middle-aged, with ages between 25 and 53.  
- BMI distribution shows a few outliers at high BMI values.  
- `Smoker` status significantly impacts insurance charges.  
- Gender and region do not strongly influence charges on their own.  

**Visualizations performed:**
- Histograms and boxplots for continuous variables (`age`, `bmi`, `charges`)
- Stacked histograms for categorical variables vs continuous features (`age` vs `smoker`, `age` vs `sex`)
- Countplots for categorical variables (`sex`, `region`)
- Scatterplots for relationships between `age` and `charges` by other variables
- Correlation heatmap to understand feature relationships  

---

## 🔢 Preprocessing

- **Categorical encoding**:
  - `sex` and `smoker` encoded with **OrdinalEncoder**
  - `region` encoded with **one-hot encoding** (`drop_first=True`)  
- Features scaled where needed for machine learning models
- Target variable transformation applied using **Box-Cox transformation** to normalize distribution

---

## 🤖 Machine Learning Models

The dataset was split into **70% training and 30% testing**. Multiple regression models were trained and evaluated using:

- **R² Score**
- **Mean Squared Error (MSE)**
- **Mean Absolute Error (MAE)**

### Models Used

- Linear Regression  
- LassoCV  
- RidgeCV  
- ElasticNetCV  
- RandomForest Regressor  
- Gradient Boosting Regressor  
- AdaBoost Regressor  
- Support Vector Regressor (SVR)  
- KNeighbors Regressor  
- XGBoost Regressor  
- LightGBM Regressor  
- Decision Tree Regressor  

### Performance on Test Set (Original Target)

| Model                     | R² Score | MSE           | MAE      |
|----------------------------|----------|---------------|----------|
| Linear Regression          | 0.770    | 33,780,510    | 4,145    |
| LassoCV                    | 0.769    | 33,906,489    | 4,178    |
| RidgeCV                    | 0.770    | 33,783,974    | 4,146    |
| ElasticNetCV               | 0.119    | 129,159,370   | 9,061    |
| RandomForest Regressor     | 0.856    | 21,125,736    | 2,550    |
| Gradient Boosting Regressor| 0.865    | 19,765,671    | 2,498    |
| AdaBoost Regressor         | 0.810    | 27,926,633    | 4,271    |
| SVR                        | -0.082   | 158,620,482   | 8,233    |
| KNeighbors Regressor       | 0.194    | 118,216,000   | 7,570    |
| XGBRegressor               | 0.833    | 24,421,056    | 2,836    |
| LGBMRegressor              | 0.858    | 20,782,825    | 2,721    |
| Decision Tree Regressor    | 0.724    | 40,428,591    | 2,898    |

> Gradient Boosting Regressor performed best among all models on original target.

### Power Transformation

- Applied **PowerTransformer** and **Box-Cox** to normalize skewed target variable.  
- Retrained all models on transformed target and inverse-transformed predictions for evaluation.  
- RandomForest, Gradient Boosting, and LightGBM remained the top-performing models.

---

## ⚙️ Usage

1. Clone the repository:
```bash
git clone <your-repo-url>
