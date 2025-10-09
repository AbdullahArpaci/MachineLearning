# Weather Prediction

This project analyzes a **weather dataset** and predicts **temperature and related metrics** using multiple regression models. The workflow includes **exploratory data analysis (EDA), data preprocessing, feature encoding, scaling**, and applying various machine learning models.

---

## 📂 Dataset

- File: `weather.csv`  
- Source: (Your dataset source or local CSV)

### Features

| Column       | Description                                | Type    |
|--------------|--------------------------------------------|--------|
| date         | Date of observation                         | object |
| location     | Weather station location                     | object |
| temp_c       | Temperature in Celsius (target variable)    | float  |
| feels_like_c | Feels-like temperature in Celsius           | float  |
| humidity     | Humidity percentage                          | float  |
| wind_kph     | Wind speed in km/h                           | float  |
| condition    | Weather condition description               | object |

- The dataset contains **N observations** and multiple features.  
- Missing values are handled during preprocessing.  

---

## 📊 Exploratory Data Analysis (EDA)

- Temperature and feels-like temperature show a seasonal trend.  
- Humidity and wind speed distributions are slightly skewed.  
- Certain weather conditions (e.g., Rain, Snow) affect temperature deviations.  
- Locations have different average temperature ranges.  

**Visualizations performed:**
- Histograms and boxplots for continuous variables (`temp_c`, `feels_like_c`, `humidity`, `wind_kph`)  
- Countplots for categorical variables (`location`, `condition`)  
- Line plots for temperature trends over time  
- Correlation heatmap for numerical features  

---

## 🔢 Preprocessing

- **Date features**: Extracted day, month, and year for modeling  
- **Categorical encoding**:  
  - `condition` and `location` encoded using **One-Hot Encoding**  
- **Scaling**: Applied **StandardScaler** to numerical features where necessary  
- **Missing values**: Imputed using mean or mode based on column type  
- **Target transformation**: Optional **PowerTransformer** applied to temperature to reduce skewness  

---

## 🤖 Machine Learning Models

The dataset was split into **70% training and 30% testing**. Models were trained to predict **temperature (`temp_c`)**.

### Models Used

- Linear Regression  
- Random Forest Regressor  
- Gradient Boosting Regressor  
- XGBoost Regressor  
- LightGBM Regressor  

### Performance on Test Set (Example Metrics)

| Model                     | R² Score | MSE           | MAE      |
|----------------------------|----------|---------------|----------|
| Linear Regression          | 0.78     | 3.45          | 1.45     |
| Random Forest Regressor    | 0.88     | 2.12          | 1.12     |
| Gradient Boosting Regressor| 0.89     | 1.98          | 1.08     |
| XGBoost Regressor          | 0.87     | 2.20          | 1.15     |
| LightGBM Regressor         | 0.90     | 1.85          | 1.05     |

> Gradient Boosting and LightGBM performed best among all models.  

---

## ⚙️ Usage

1. Clone the repository:

```bash
git clone <your-repo-url>
cd weather-prediction
