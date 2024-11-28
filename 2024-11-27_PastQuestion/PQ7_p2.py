from sklearn.preprocessing import StandardScaler
from sklearn.metrics import root_mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

train = pd.read_csv("../data/PQ7_p2_x_train.csv")
test = pd.read_csv("../data/PQ7_p2_x_test.csv")

train.info()
test.info()

x_train = train.drop(columns=["ID", "이용금액"])
x_test = test.drop(columns=["ID"])
y_train = train["이용금액"]
num_col = x_train.select_dtypes(exclude="object").columns
scaler = StandardScaler()
x_train[num_col] = scaler.fit_transform(x_train[num_col])
x_test[num_col] = scaler.fit_transform(x_test[num_col])
ctg_col = x_train.select_dtypes(include=["object", "category"]).columns
encoder = OneHotEncoder(handle_unknown="ignore")
x_train_encoded = encoder.fit_transform(x_train[ctg_col])
x_test_encoded = encoder.transform(x_test[ctg_col])
x_train_encoded_df = pd.DataFrame(x_train_encoded.toarray(
), columns=encoder.get_feature_names_out(ctg_col), index=x_train.index)
x_test_encoded_df = pd.DataFrame(x_test_encoded.toarray(
), columns=encoder.get_feature_names_out(ctg_col), index=x_test.index)
x_train = pd.concat([x_train[num_col],
                    x_train_encoded_df], axis=1)
x_test = pd.concat([x_test[num_col],
                    x_test_encoded_df], axis=1)
x_train, x_val, y_train, y_val = train_test_split(
    x_train, y_train, test_size=0.2, random_state=42)
model = RandomForestRegressor()
model.fit(x_train, y_train)
y_val_pred = model.predict(x_val)
rmse = root_mean_squared_error(y_val, y_val_pred)
print(rmse)
x_test_pred = model.predict(x_test)
result = pd.DataFrame(x_test_pred, columns=["pred"])
result = pd.concat([test["ID"], result], axis=1)
result.to_csv("res.csv", index=False)

df = pd.read_csv("res.csv")
print(df)
