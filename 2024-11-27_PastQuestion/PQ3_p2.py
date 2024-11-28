from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

x_train = pd.read_csv("../data/PQ3_p2_x_train.csv")
test = pd.read_csv("../data/PQ3_p2_x_test.csv")

x_train.info()
test.info()

y_train = x_train["TravelInsurance"]
x_train = x_train.drop(columns=["ID", "TravelInsurance"])
x_test = test.drop(columns=["ID"])

ctg_col = x_train.select_dtypes(include=["object", "category"]).columns
encoder = OneHotEncoder()
x_train_encoded = encoder.fit_transform(x_train[ctg_col])
x_test_encoded = encoder.transform(x_test[ctg_col])

x_train_encoded_df = pd.DataFrame(
    x_train_encoded.toarray(), columns=encoder.get_feature_names_out(ctg_col), index=x_train.index)
x_test_encoded_df = pd.DataFrame(
    x_test_encoded.toarray(), columns=encoder.get_feature_names_out(ctg_col), index=x_test.index)

x_train = pd.concat([x_train.drop(columns=ctg_col),
                    x_train_encoded_df], axis=1)
x_test = pd.concat([x_test.drop(columns=ctg_col),
                    x_test_encoded_df], axis=1)
x_train, x_val, y_train, y_val = train_test_split(
    x_train, y_train, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(x_train, y_train)
y_val_pred = model.predict(x_val)
roc = roc_auc_score(y_val, y_val_pred)
print(roc)
test.info()
x_test_pred = model.predict(x_test)
result = pd.DataFrame(x_test_pred, columns=["proba"])
result.info()
result = pd.concat([test["ID"], result], axis=1)
result.to_csv("result.csv", index=False)
result.info()
