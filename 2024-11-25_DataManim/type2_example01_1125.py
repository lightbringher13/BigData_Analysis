from sklearn.metrics import roc_auc_score, accuracy_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("../data/admission.csv")
df.info()

x_train = df.drop(columns=["Serial No.", "TOEFL Score"])
y_train = df["TOEFL Score"]
x_test = df.drop(columns=["Serial No.", "TOEFL Score"])

scaler = StandardScaler()

num_columns = x_train.select_dtypes(exclude="object").columns
x_train[num_columns] = scaler.fit_transform(x_train[num_columns])
x_test[num_columns] = scaler.transform(x_test[num_columns])

encoder = LabelEncoder()
x_train["Chance of Admit"] = encoder.fit_transform(x_train["Chance of Admit"])
x_test["Chance of Admit"] = encoder.transform(x_test["Chance of Admit"])

x_train, x_val, y_train, y_val = train_test_split(
    x_train, y_train, test_size=0.2, random_state=42)

model = RandomForestRegressor()
model.fit(x_train, y_train)
y_val_pred = model.predict(x_val)

msa = mean_squared_error(y_val, y_val_pred)
print(msa)

x_test_pred = model.predict(x_test)
result = pd.DataFrame(x_test_pred, columns=["pred"])
result.to_csv("result.csv", index=False)
res = pd.read_csv("result.csv")
print(res, y_train)

# # 96 unsolved
# df = pd.read_csv("../data/admission.csv")
# df.info()

# # 97 unsolved
# df = pd.read_csv("../data/redwine.csv")
# df.info()
