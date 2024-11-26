import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv("admission.csv")

# Drop the Serial No. column
df = df.drop(columns=["Serial No."])

# Separate independent variables (X) and dependent variable (y)
X = df.drop(columns=["Chance of Admit"])
y = df["Chance of Admit"]

# Split the data into training and testing sets (optional but recommended)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train a Random Forest Regressor
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Extract feature importances
feature_importances = model.feature_importances_

# Create a DataFrame to display feature importance
importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": feature_importances
}).sort_values(by="Importance", ascending=False)

# Display feature importance
print(importance_df)

# # 96 unsolved
# df = pd.read_csv("../data/admission.csv")
# df.info()

# # 97 unsolved
# df = pd.read_csv("../data/redwine.csv")
# df.info()
