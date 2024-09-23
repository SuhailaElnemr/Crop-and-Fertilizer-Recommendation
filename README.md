# Crop and Fertilizer Recommendation
  
## **Overview**
This web application is designed to help farmers and agricultural professionals make informed decisions about which crops to grow and which fertilizers to use, based on data-driven insights. By leveraging machine learning models, the website provides recommendations tailored to the specific environmental and soil conditions inputted by the user.

### **Key Features:**
- Crop Recommendation: The application suggests the most suitable crop for the given environmental conditions, such as soil type, weather, and geographical location.
- Fertilizer Recommendation: Based on the selected crop and soil properties, the app recommends optimal fertilizers to enhance growth and yield.
- User Input Form: Users can enter relevant details, such as soil properties (e.g., pH, nitrogen content, phosphorus), climatic conditions (e.g., rainfall, temperature), and region information. The model processes these inputs to provide accurate suggestions.

### **Machine Learning Model**
The recommendation system is powered by a machine learning model that has been trained on agricultural datasets. The model takes into account several factors, such as:
- Soil characteristics (e.g., nitrogen, phosphorus, potassium, pH)
- Climate data (e.g., temperature, humidity, rainfall)
- Region-based historical crop data
Using this input, the model predicts the best crops and fertilizers for optimizing yield in a given location.
  
### **Technology Stack:**
- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS
- **Machine Learning:** Scikit-learn
- **Data Handling:** Pandas, NumPy
<!-- - Deployment: Can be hosted on services like Heroku, AWS, or any cloud-based service -->
  
### **How to Use:**
- Navigate to the homepage.
- Fill in the required input fields (e.g., soil characteristics, temperature, soil type).
- Submit the form to get crop and fertilizer recommendations.
- The result will display the best-suited crop(s) and a recommended fertilizer for optimal growth.
  
### **Future Improvements:**
- Integration with real-time weather APIs for dynamic recommendations.
- Expand the database to support a wider variety of crops and fertilizers.
- Include location-based pest and disease prediction for more holistic crop management recommendations.

  
# Preprocessing Notbook

This notebook analyzes a crop and fertilizer dataset to provide recommendations.

## Steps:

1. **Data Loading and Cleaning:**
   - Loads the dataset from 'Crop and fertilizer dataset.csv'.
   - Removes unnecessary columns ('District_Name', 'Link', 'Rainfall').
   - Cleans the 'Soil_color' column by removing leading/trailing spaces.
   - Removes duplicate rows.

2. **Data Encoding:**
   - Identifies categorical columns.
   - Uses LabelEncoder to convert categorical values to numerical representations.

3. **Correlation Analysis:**
   - Generates a heatmap to visualize correlations between features.

4. **Data Saving:**
   - Saves the processed data to 'data.csv'.

## Libraries Used:

- numpy
- pandas
- matplotlib
- seaborn
- sklearn (LabelEncoder)

## Dataset:

- 'Crop and fertilizer dataset.csv' 

## Output:

- 'data.csv' (Processed dataset)
- Correlation heatmap

# Model Notebook

This notebook builds a machine learning model to predict suitable fertilizers based on crop and soil characteristics.

## Steps:

1. **Data Loading:**
    - Loads the processed dataset from 'data.csv'.

2. **Data Splitting:**
    - Splits the data into training and testing sets.

3. **Model Selection and Training:**
    - Selects an appropriate machine learning model (e.g., Random Forest, Decision Tree).
    - Trains the model using the training data.

4. **Model Evaluation:**
    - Evaluates the trained model using the testing data and appropriate metrics (e.g., accuracy, precision, recall).

5. **Model Saving (Optional):**
    - Saves the trained model for future use.

## Libraries Used:

- scikit-learn (model selection, training, evaluation, model saving)

## Dataset:

- 'data.csv' (Processed dataset from the data preparation notebook)

## Output:

- Trained machine learning model
- Model evaluation metrics
