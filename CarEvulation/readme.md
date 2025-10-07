# Car Price Prediction

## Description
This project uses a dataset of used cars to predict the selling price based on various features like vehicle age, kilometers driven, fuel type, transmission type, and brand. The workflow includes **data cleaning, feature engineering, visualization, encoding, scaling**, and applying multiple regression models to predict car prices.

---

## Dataset
The dataset (`17-cardekho.csv`) contains **15,242 cleaned entries** and **13 features**:

- `vehicle_age` - Age of the car  
- `km_driven` - Kilometers driven  
- `mileage` - Mileage in km/l or km/kg  
- `engine` - Engine capacity in CC  
- `max_power` - Maximum power of the car  
- `seats` - Number of seats  
- `car_name`, `brand`, `model` - Categorical information about car  
- `seller_type` - Type of seller (Individual, Dealer, Trustmark Dealer)  
- `fuel_type` - Petrol, Diesel, CNG, LPG, Electric  
- `transmission_type` - Manual or Automatic  
- `selling_price` - Target variable (price in INR)

**Data Cleaning and Preprocessing:**  
- Removed duplicates and entries with invalid values (e.g., `seats=0`).  
- Removed outliers in `selling_price` (> 10,000,000 INR) and `km_driven` (> 1,000,000 km).  
- Frequency encoding applied to `car_name`, `model`, and `brand`.  
- One-hot encoding applied to `seller_type`, `fuel_type`, and `transmission_type`.  
- StandardScaler used to scale numerical features.

---

## Exploratory Data Analysis (EDA)
- Scatter plots for `vehicle_age` vs `selling_price` and `km_driven` vs `selling_price`.  
- Boxplots for `fuel_type`, `seller_type`, and `transmission_type`.  
- Correlation heatmap for feature selection and understanding relationships.

---

## Machine Learning Models
The following regression models were trained and evaluated using **R² Score** and **Mean Squared Error (MSE)**:

- **Linear Regression**  
- **Support Vector Regressor (SVR)**  
- **K-Nearest Neighbors Regressor (KNN)**  
- **Gradient Boosting Regressor**  
- **AdaBoost Regressor**

**Performance on test set:**

| Model                     | R² Score | MSE           |
|----------------------------|----------|---------------|
| Linear Regression          | 0.695    | 199,710,242,899 |
| SVR                        | -0.072   | 701,771,232,924 |
| KNeighbors Regressor       | 0.881    | 77,603,363,933 |
| Gradient Boosting Regressor| 0.914    | 56,298,448,542 |
| AdaBoost Regressor         | 0.666    | 218,643,980,642 |

> Gradient Boosting Regressor performed best on the dataset.

---

## Usage
1. Clone the repository:
```bash
git clone <your-repo-url>
