from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# Load data
x_train = pd.read_csv("../data/PQ2_p2_x_train.csv")
y_train = pd.read_csv("../data/PQ2_p2_y_train.csv")
x_test = pd.read_csv("../data/PQ2_p2_x_test.csv")

# drop unnecessary columns and set train and test data
x_train = x_train.drop(columns=["ID"])
x_test = x_test.drop(columns=["ID"])
y_train = y_train.drop(columns=["ID"])

# preprocess category columns
ctg_col = x_train.select_dtypes(include=["object", "category"]).columns
encoder = OneHotEncoder(handle_unknown="ignore")
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

# split the data
x_train, x_val, y_train, y_val = train_test_split(
    x_train, y_train, test_size=0.2, random_state=42)

# fit the model
model = RandomForestClassifier()
model.fit(x_train, y_train)
y_val_pred = model.predict(x_val)

# model score
f1_score = f1_score(y_val_pred, y_val)
print(f1_score)

# final result
x_val_pred = model.predict(x_test)
result = pd.DataFrame(x_val_pred, columns=["preds"])
result.to_csv("result.csv")
