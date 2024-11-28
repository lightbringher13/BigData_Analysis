from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# Load Data
train = pd.read_csv("../data/PQ5_p2_x_train.csv")
test = pd.read_csv("../data/PQ5_p2_x_test.csv")

# Inspect Data
train.info()
test.info()

# Separate Features and Target
x_train = train.drop(columns=["ID", "price"])
y_train = train["price"]
# Corrected: Now refers to the actual test set
x_test = test.drop(columns="ID")

# Encode Categorical Columns
ctg_col = x_train.select_dtypes(include=["object", "category"]).columns
encoder = OneHotEncoder(handle_unknown="ignore")
x_train_encoded = encoder.fit_transform(x_train[ctg_col])
x_test_encoded = encoder.transform(x_test[ctg_col])
x_train_encoded_df = pd.DataFrame(
    x_train_encoded.toarray(), columns=encoder.get_feature_names_out(ctg_col), index=x_train.index)
x_test_encoded_df = pd.DataFrame(
    x_test_encoded.toarray(), columns=encoder.get_feature_names_out(ctg_col), index=x_test.index)

# Combine Encoded and Non-Categorical Data
x_train = pd.concat([x_train.drop(columns=ctg_col),
                    x_train_encoded_df], axis=1)
x_test = pd.concat([x_test.drop(columns=ctg_col), x_test_encoded_df], axis=1)

# Train-Test Split for Validation
x_train, x_val, y_train, y_val = train_test_split(
    x_train, y_train, test_size=0.2, random_state=42)

# Train RandomForestRegressor
model = RandomForestRegressor(random_state=42)
model.fit(x_train, y_train)

# Validate the Model
y_val_pred = model.predict(x_val)
rmse = mean_squared_error(y_val, y_val_pred, squared=False)
print("RMSE:", rmse)

x_test_pred = model.predict(x_test)
result = pd.DataFrame(x_test_pred, columns=["pred"])
result = pd.concat([test["ID"], result], axis=1)
result.to_csv("result.csv", index=False)

df = pd.read_csv("result.csv")
df.info()
