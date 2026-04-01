import numpy as np
from sklearn.linear_model import LinearRegression

# Step 1: Dataset
hours = np.array([1,2,3,4,5,6,7,8,2,3,4,5,6,7,8,9,10,3,5,7]).reshape(-1,1)
marks = np.array([20,25,30,35,45,50,55,60,22,28,33,48,52,58,65,70,75,29,47,60])

# Step 2: Train Model
model = LinearRegression()
model.fit(hours, marks)

# Step 3: Take input from user
user_input = float(input("Enter study hours (0–12): "))

if user_input < 0 or user_input > 12:
    print("Invalid input! Enter between 0 and 12.")
else:
    prediction = model.predict([[user_input]])
    print("Predicted Marks:", round(prediction[0], 2))

