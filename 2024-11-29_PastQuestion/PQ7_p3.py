from sklearn.metrics import accuracy_score
import numpy as np
import statsmodels.api as sm
import pandas as pd

# 빅분기 7회 작업형3 1번
df = pd.read_csv("../data/PQ7_p3_01.csv")
df.info()
res = df.corr().unstack().reset_index(name="corr")
res = res.loc[res["level_0"] != res["level_1"]]
res = res.sort_values("corr", ascending=False)
print(res.iloc[0, 2])

# 빅분기 7회 작업형3 2번
x = df.drop(columns="Target")
y = df["Target"]
x = sm.add_constant(x)
model = sm.OLS(y, x).fit()
summary = model.summary()
print(summary)
print("v2: ", model.params["v2"])

# 빅분기 7회 작업형3 3번
print(model.pvalues.max())

# 빅분기 7회 작업형3 3번
df = pd.read_csv("../data/PQ7_p3_02.csv")
df.info()
train = df[:210]
test = df[210:]
x = train.drop(columns="target")
y = train["target"]
x = sm.add_constant(x)
model = sm.Logit(y, x).fit()
summary = model.summary()
print(summary)
odds_ratio = np.exp(model.params["age"])
print(odds_ratio)

# 빅분기 7회 작업형3 4번
residual_deviance = model.llf * -2
print(residual_deviance)

# 빅분기 7회 작업형3 5번
log_likelihood = model.llf
print(log_likelihood)

# 빅분기 7회 작업형3 6번
x = test.drop(columns="target")
y = test["target"]
x = sm.add_constant(x)
x = sm.add_constant(x)
y_pred_prob = model.predict(x)
y_pred = (y_pred_prob > 0.5).astype(int)
accuracy = accuracy_score(y, y_pred)
error_rate = 1-accuracy
print(error_rate)
