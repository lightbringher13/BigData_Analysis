from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

train = pd.read_csv("../data/PQ4_p2_x_train.csv")
test = pd.read_csv("../data/PQ4_p2_x_test.csv")

train.info()
test.info()

print(train.isna().sum())
print(test.isna().sum())

train = train.fillna(train.median(numeric_only=True))
test = test.fillna(train.median(numeric_only=True))


x_train = train.drop(columns=["ID", "Segmentation"])
x_test = test.drop(columns=["ID"])
y_train = train["Segmentation"]

ctg_col = x_train.select_dtypes(include=["object", "category"]).columns
x_train[ctg_col] = x_train[ctg_col].fillna(x_train[ctg_col].mode().iloc[0])
x_test[ctg_col] = x_test[ctg_col].fillna(x_train[ctg_col].mode().iloc[0])
encoder = OneHotEncoder(handle_unknown="ignore")
x_train_encoded = encoder.fit_transform(x_train[ctg_col])
x_test_encoded = encoder.transform(x_test[ctg_col])
x_train_encoded_df = pd.DataFrame(
    x_train_encoded.toarray(), columns=encoder.get_feature_names_out(ctg_col), index=x_train.index)
x_test_encoded_df = pd.DataFrame(
    x_test_encoded.toarray(), columns=encoder.get_feature_names_out(ctg_col), index=x_test.index)
x_train = pd.concat([x_train.drop(columns=ctg_col),
                    x_train_encoded_df], axis=1)
x_test = pd.concat([x_test.drop(columns=ctg_col), x_test_encoded_df], axis=1)
x_train, x_val, y_train, y_val = train_test_split(
    x_train, y_train, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(x_train, y_train)
y_val_pred = model.predict(x_val)
f1 = f1_score(y_val, y_val_pred, average="macro")
print(f1)
x_test_pred = model.predict(x_test)
result = pd.DataFrame(x_test_pred, columns=["Segmentation"])
result = pd.concat([test["ID"], result], axis=1)
result.to_csv("result.csv", index=False)
result = pd.read_csv("result.csv")
result.info()
