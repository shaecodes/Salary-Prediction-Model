# Employee Salary Prediction Model

This project demonstrates how to predict employee salaries based on various factors such as age, gender, education level, job title, and years of experience. The model uses machine learning techniques such as Label Encoding and Feature Scaling to process the data, followed by linear regression for salary prediction.

## Project Workflow

1. **Data Preprocessing**
   - **Label Encoding**: Converts categorical variables (e.g., gender, education level, job title) into numerical values.
   - **Feature Scaling**: Standardizes the continuous variables (e.g., age, experience years) to improve model performance.

2. **Modeling**
   - **Linear Regression**: A simple model used to predict salaries based on the independent features.

3. **Prediction**
   - The trained model can predict an employee's salary based on input values for age, gender, education level, job title, and experience years.

## Requirements

- Python 3.x
- pandas
- scikit-learn
- joblib

You can install the required dependencies using:

```bash
pip install pandas scikit-learn joblib
