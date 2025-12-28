# Overview
Built a high-performance regression model to predict vehicle CO₂ emissions (g/km) using engine and fuel consumption features.
The project focuses on handling multicollinearity and producing stable, interpretable predictions.

# Dataset
This dataset captures the details of how CO2 emissions by a vehicle can vary with the different features. The dataset has been taken from Canada Government official open data website. This is a compiled version. This contains data over a period of 7 years. There are total 7385 rows and 12 columns. There are few abbreviations that has been used to describe the features. I am listing them out here. The same can be found in the Data Description sheet.

# Tools & Libraries
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

# Approach & Methodology
Performed data preprocessin with Numpy & Pandas
Explored the dataset to understand feature distributions and relationships with CO₂ emissions
Performed correlation analysis using a heatmap to identify strong inter-feature relationships
Detected multicollinearity among fuel consumption and engine-related features
Selected Ridge Regression (L2 regularization) to stabilize coefficients and improve generalization
Standardized numerical features to ensure fair regularization
Split the data into training and testing sets and trained the model
Evaluated performance using R², MAE, and RMSE to assess accuracy and error behavior

# Model Evaluation
R² = 0.99 → Explains 99.2% of emission variability

MAE ≈ 2.77 g/km → Very low average prediction error

RMSE ≈ 4.41 g/km → Strong consistency with minimal outliers

Typical vehicle CO₂ emissions range from 100–400 g/km, making these errors very small.

# Dataset 
link : C02-Emission-Model/CO2 Emissions_Canada.csv
# Streamlit web App 
link : https://c02-emission-model-haziumxyz.streamlit.app/

