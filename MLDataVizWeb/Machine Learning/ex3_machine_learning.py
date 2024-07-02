import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor


data = pd.read_excel('../final_data/Exercise3Completex.xlsx')

X = data.iloc[:, :2]   # First two columns as independent variables
Y = data.iloc[:, -1]   # Last column as dependent variable

threshold_index1 = 10310  # Starting index of the first test set
threshold_index2 = 11707  # Starting index of the second test set


# Create test sets
X_test1 = X.iloc[threshold_index1:threshold_index2]
Y_test1 = Y.iloc[threshold_index1:threshold_index2]

X_test2 = X.iloc[threshold_index2:]
Y_test2 = Y.iloc[threshold_index2:]

# Create the training set
X_train = X.iloc[:threshold_index1]
Y_train = Y.iloc[:threshold_index1]

print("Training set size:", X_train.shape)
print("1st Test set size:", X_test1.shape)
print("2nd Test set size:", X_test2.shape)

print("------------------------------------")

# Create and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)

# Make predictions on the test sets
y1_pred1 = model.predict(X_test1)
y2_pred1 = model.predict(X_test2)


# Evaluate the model's performance
y1_mse = mean_squared_error(Y_test1, y1_pred1)
y1_r2 = r2_score(Y_test1, y1_pred1)
print("Mean Squared Error (MSE):", y1_mse)
print("R-squared (R2) Score:", y1_r2)

print("------------------------------------")

y2_mse = mean_squared_error(Y_test2, y2_pred1)
y2_r2 = r2_score(Y_test2, y2_pred1)
print("Mean Squared Error (MSE):", y2_mse)
print("R-squared (R2) Score:", y2_r2)


# Calculate residuals
residuals_test1 = Y_test1 - y1_pred1
residuals_test2 = Y_test2 - y2_pred1

# 1. Error Distribution Plot
plt.figure(figsize=(10, 5))
plt.hist(residuals_test1, bins=50, alpha=0.5, label='Test Set 1')
plt.hist(residuals_test2, bins=50, alpha=0.5, label='Test Set 2')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Error Distribution Plot')
plt.legend()
plt.show()

# 2. Linear Relationship Between Actual and Predicted Values
plt.figure(figsize=(10, 5))
plt.plot(Y_test1.values, label='Actual Values Test 1', alpha=0.7)
plt.plot(y1_pred1, label='Predicted Values Test 1', alpha=0.7)
plt.xlabel('Examples')
plt.ylabel('Values')
plt.title('Linear Relationship Between Actual and Predicted Values - Test 1')
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(Y_test2.values, label='Actual Values Test 2', alpha=0.7)
plt.plot(y2_pred1, label='Predicted Values Test 2', alpha=0.7)
plt.xlabel('Examples')
plt.ylabel('Values')
plt.title('Linear Relationship Between Actual and Predicted Values - Test 2')
plt.legend()
plt.show()

# 3. Predicted Balance Score Data for Basketball Player 1
plt.figure(figsize=(10, 5))
plt.plot(y1_pred1, label='Basketball Player 1 Predicted Balance Score', color='blue')
plt.xlabel('Examples')
plt.ylabel('Estimated Balance Score')
plt.title('Basketball Player 1 Predicted Balance Score')
plt.legend()
plt.show()

# 4. Predicted Balance Score Data for Basketball Player 2
plt.figure(figsize=(10, 5))
plt.plot(y2_pred1, label='Basketball Player 2 Predicted Balance Score', color='green')
plt.xlabel('Examples')
plt.ylabel('Estimated Balance Score')
plt.title('Basketball Player 2 Predicted Balance Score')
plt.legend()
plt.show()









