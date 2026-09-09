# 🚗 Vehicle Fuel Efficiency Prediction 

> An intelligent Machine Learning project that predicts vehicle fuel efficiency (MPG) based on various automobile characteristics using regression algorithms.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Data%20Analysis-013243?logo=numpy)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikit-learn)
![Google Colab](https://img.shields.io/badge/Google%20Colab-Notebook-F9AB00?logo=googlecolab)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

# 📖 Project Overview

Fuel efficiency is an important factor when evaluating the performance and economy of a vehicle. It represents how efficiently a vehicle uses fuel and is commonly measured in **Miles Per Gallon (MPG)**.

This project uses **Machine Learning regression algorithms** to predict the fuel efficiency of a vehicle based on its specifications, such as:

- 🚘 Number of cylinders
- ⚙️ Engine displacement
- 🔧 Horsepower
- ⚖️ Vehicle weight
- ⏱️ Acceleration
- 📅 Model year
- 🌎 Origin

The project follows a complete Machine Learning workflow, from **data preprocessing and exploratory data analysis to model training, evaluation, and prediction on new vehicle data**.

---

# 🎯 Project Objectives

The main objectives of this project are:

- 📊 Analyze automobile data
- 🧹 Clean and preprocess the dataset
- 🔍 Identify important factors affecting fuel efficiency
- 🤖 Train multiple Machine Learning regression models
- 📈 Evaluate model performance using regression metrics
- 🏆 Compare the performance of different algorithms
- 🔮 Predict the fuel efficiency of a new vehicle

---

# 📂 Dataset

The project uses the **Auto MPG dataset**, which contains information about different automobile models and their fuel efficiency.

## Dataset Features

| Feature | Description |
|---|---|
| `mpg` | Fuel efficiency in Miles Per Gallon |
| `cylinders` | Number of engine cylinders |
| `displacement` | Engine displacement |
| `horsepower` | Engine horsepower |
| `weight` | Vehicle weight |
| `acceleration` | Acceleration performance |
| `model year` | Year of vehicle manufacture |
| `origin` | Region of vehicle origin |
| `car name` | Name of the vehicle |

## 🎯 Target Variable

The target variable of this project is:

**MPG (Miles Per Gallon)**

---

# 🔄 Machine Learning Workflow

The project follows the following Machine Learning workflow:

**Dataset → Data Exploration → Data Preprocessing → Feature Selection → Train-Test Split → Feature Scaling → Model Training → Model Evaluation → Model Comparison → New Data Prediction**

---

# 🧹 Data Preprocessing

The dataset is prepared before training the Machine Learning models.

### Preprocessing steps include:

1. 📥 Load the dataset
2. 🔎 Inspect the dataset
3. 🧹 Remove duplicate records
4. ❓ Check and handle missing values
5. 🔄 Convert data types where required
6. 🗑️ Remove unnecessary columns such as `car name`
7. 🎯 Separate features and target variable
8. ✂️ Split the dataset into training and testing sets
9. ⚖️ Apply feature scaling where required

---

# 📊 Exploratory Data Analysis

Exploratory Data Analysis is performed to understand the dataset and identify relationships between vehicle characteristics and fuel efficiency.

The analysis includes:

- 📈 Distribution of MPG
- 📊 Feature distributions
- 🔗 Correlation analysis
- 📉 Relationship between vehicle weight and MPG
- ⚙️ Relationship between displacement and MPG
- 🔧 Relationship between horsepower and MPG
- 🔢 Relationship between cylinders and MPG

Visualization libraries such as **Matplotlib** and **Seaborn** are used for data visualization.

---

# 🤖 Machine Learning Algorithms

Three regression algorithms are used in this project.

## 1️⃣ Linear Regression

Linear Regression is a supervised Machine Learning algorithm used to predict a continuous numerical value.

In this project, Linear Regression learns the relationship between vehicle features and fuel efficiency.

**Input Features → Linear Regression → Predicted MPG**

### Advantages

- Simple and easy to understand
- Fast to train
- Easy to interpret
- Suitable for linear relationships

---

## 2️⃣ Decision Tree Regressor 🌳

Decision Tree Regression predicts the target value by dividing the dataset into different decision-based regions.

### Advantages

- Easy to understand
- Captures non-linear relationships
- Requires less preprocessing
- Can model complex relationships

---

## 3️⃣ Random Forest Regressor 🌲

Random Forest Regression combines multiple decision trees to produce a more robust prediction.

### Advantages

- Handles non-linear relationships
- Reduces overfitting compared with a single decision tree
- Provides strong predictive performance
- Works well with multiple features

---

# 🏆 Model Performance

The performance of the regression models was evaluated using **MAE, MSE, RMSE, and R² Score**.

## 📈 Linear Regression Performance

- **MAE:** 2.25
- **MSE:** 8.20
- **RMSE:** 2.86
- **R² Score:** 0.8476

---

## 🌳 Decision Tree Regression Performance

- **MAE:** 2.21
- **MSE:** 11.15
- **RMSE:** 3.34
- **R² Score:** 0.7926

---

## 🌲 Random Forest Regression Performance

- **MAE:** 1.59
- **MSE:** 4.61
- **RMSE:** 2.15
- **R² Score:** 0.9143

---

# 📊 Model Comparison

| Model | MAE ↓ | MSE ↓ | RMSE ↓ | R² Score ↑ |
|---|---:|---:|---:|---:|
| 📈 Linear Regression | 2.25 | 8.20 | 2.86 | 0.8476 |
| 🌳 Decision Tree Regression | 2.21 | 11.15 | 3.34 | 0.7926 |
| 🌲 Random Forest Regression | **1.59** | **4.61** | **2.15** | **0.9143** |

> **Note:** Lower values of MAE, MSE, and RMSE indicate better performance, while a higher R² Score indicates better performance.

---

# 🥇 Best Performing Model

Based on the evaluation results, the **Random Forest Regressor** achieved the best overall performance.

### Random Forest Results:

- 🟢 **MAE:** 1.59
- 🟢 **MSE:** 4.61
- 🟢 **RMSE:** 2.15
- 🟢 **R² Score:** 0.9143

The Random Forest model achieved an **R² Score of 91.43%**, meaning it explains approximately **91.43% of the variation in vehicle fuel efficiency** in the test data.

Therefore, **Random Forest Regressor** is selected as the best-performing model among the three algorithms tested.

---

# 🔮 Predict New Data

After training the Machine Learning models, a new vehicle sample can be provided to predict its fuel efficiency.

The new vehicle contains the following features:

- Cylinders
- Displacement
- Horsepower
- Weight
- Acceleration
- Model Year
- Origin

The trained model then predicts the expected **MPG** of the vehicle.

---

# 🚗 Example New Vehicle

Example vehicle specifications:

| Feature | Value |
|---|---:|
| Cylinders | 4 |
| Displacement | 140.0 |
| Horsepower | 90.0 |
| Weight | 2400 |
| Acceleration | 15.5 |
| Model Year | 82 |
| Origin | 1 |

The model uses these values to estimate the vehicle's fuel efficiency.

---

# 📈 Project Highlights

✨ Complete Machine Learning regression pipeline

✨ Data cleaning and preprocessing

✨ Exploratory Data Analysis

✨ Feature selection

✨ Multiple regression algorithms

✨ Model performance comparison

✨ Regression evaluation metrics

✨ New vehicle MPG prediction

✨ Beginner-friendly implementation

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Programming language |
| 🐼 **Pandas** | Data manipulation |
| 🔢 **NumPy** | Numerical operations |
| 📊 **Matplotlib** | Data visualization |
| 🎨 **Seaborn** | Statistical visualization |
| 🤖 **Scikit-learn** | Machine Learning |
| ☁️ **Google Colab** | Development environment |
| 🐙 **GitHub** | Version control and project hosting |

---

# 📁 Project Structure

```
Project_4_Vehicle_Fuel_Efficiency_Prediction_Using_Machine_Learning/
│
├── Vehicle_Fuel_Efficiency_Prediction.ipynb
├── Vehicle_Fuel_Efficiency_Prediction.py
├── Dataset/
│   ├── auto-mpg.csv
├── Images/
│   ├── actual_vs_predicted_fuel_efficiency.png
│   ├── feature_importance.png
│   └── model_R²_score_comparison.png
├── best_model.pkl
├── scaler.pkl
├── feature_names.pkl
├── label_encoders.pkl
├── requirements.txt
├── README.md 
└── LICENSE
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/Tuhin092005/Project_4_Vehicle_Fuel_Efficiency_Prediction_Using_Machine_Learning.git
```

### Navigate to the project

```bash
cd Project_4_Vehicle_Fuel_Efficiency_Prediction_Using_Machine_Learning
```

### Install required libraries

```bash
pip install -r requirements.txt
```

### ▶️ Run the project

### Using Python

```bash
python Vehicle_Fuel_Efficiency_Prediction.py
```

### Using Google Colab Using Python

Open

```text
Vehicle_Fuel_Efficiency_Prediction.ipynb
```

Upload:

- auto-mpg.csv

Run all cells.


---

# 📌 Future Improvements

Possible improvements for this project include:

- 🚀 Hyperparameter tuning
- 📊 More advanced data visualization
- 🔍 Feature importance analysis
- 🤖 Testing additional regression algorithms
- 📈 Cross-validation
- 🌐 Creating a web-based prediction interface
- ☁️ Deploying the trained Machine Learning model

---

# 👨‍💻 Author

**Tuhin Maji**

B.Tech CSE (Artificial Intelligence & Machine Learning)

Meghnad Saha Institute of Technology (MSIT)

---

# ⭐ If you found this project useful

If you found this project helpful or interesting, consider giving this repository a ⭐ **Star** on GitHub!

Your support is appreciated! ❤️

---

# 📜 License

This project is licensed under the **MIT License**.
