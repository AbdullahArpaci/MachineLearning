# Housing Price Prediction with Regression Models

## Description
This project uses the **California housing dataset** to predict `median_house_value` using multiple regression models. The workflow includes data cleaning, feature engineering, outlier removal, scaling, transformation, and model evaluation.

Models included:

- Linear Regression  
- Lasso Regression  
- Ridge Regression  
- K-Nearest Neighbors Regressor  
- Decision Tree Regressor  
- Random Forest Regressor  
- AdaBoost Regressor  
- Gradient Boost Regressor  
- XGBoost Regressor  

Both **raw and transformed data** (using PowerTransformer and Box-Cox) are used to improve model performance.

---

## Dataset
The dataset contains **20,640 rows** and **10 columns**:

- `longitude`, `latitude`  
- `housing_median_age`  
- `total_rooms`, `total_bedrooms`  
- `population`, `households`  
- `median_income`, `median_house_value`  
- `ocean_proximity` (categorical)

**Missing Values:**  
- `total_bedrooms` contains missing values and is filled with the column median.

---

## Data Preprocessing
1. Handle missing values by filling `total_bedrooms` with median.  
2. Remove outliers in `median_house_value` using the IQR method.  
3. Encode `ocean_proximity` using one-hot encoding.  
4. Transform numerical features using **PowerTransformer (Yeo-Johnson)**.  
5. Transform target variable with **Box-Cox**.  
6. Split data into training (80%) and testing (20%) sets.

---

## Model Evaluation
Models are evaluated using:

- **Mean Absolute Error (MAE)**  
- **Root Mean Squared Error (RMSE)**  
- **R² Score**

Predictions are inversely transformed if Box-Cox was applied.

---

## Usage
1. Clone the repository:
```bash
git clone <your-repo-url>
