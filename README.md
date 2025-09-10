# gtc-ml-project2-diabetes-prediction

This project predicts the likelihood of diabetes in patients based on medical attributes such as glucose level, BMI, age, and more.  

---

## 📊 Dataset
- **Target Variable:** `Outcome`  
  - `0` → No diabetes  
  - `1` → Diabetes  
- **Features:**
  - Pregnancies  
  - Glucose  
  - BloodPressure  
  - SkinThickness  
  - Insulin  
  - BMI  
  - DiabetesPedigreeFunction  
  - Age  

---

## ⚙️ Methods
We applied data analysis, visualization, and machine learning techniques to understand the relationships between features and predict the outcome.

### 🔹 Exploratory Data Analysis (EDA)
- Histograms, boxplots, and violin plots to understand feature distributions  
- Correlation heatmap to see linear relationships  
- Mutual information to capture non-linear dependencies  

### 🔹 Preprocessing
- Handling skewed features (log / power transformations)  
- Scaling for algorithms sensitive to feature magnitudes (e.g., SVM)  
- Train-test split with stratification  

### 🔹 Models Used
1. **Support Vector Machine (SVM)**  
   - Preprocessing: Yeo-Johnson transformation + StandardScaler  
   - Kernel: RBF  
2. **Decision Tree Classifier**  
   - No scaling or skew correction needed  
   - Interpretable model with feature importance  

---


