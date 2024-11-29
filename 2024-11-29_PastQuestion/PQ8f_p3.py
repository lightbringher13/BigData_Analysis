import statsmodels.api as sm
import pandas as pd
df = pd.read_csv("../data/PQ7_p3_02.csv")
df.info()
x = df.drop(columns="target")
y = df["target"]
x = sm.add_constant(x)
model = sm.Logit(y, x).fit()
print(model.summary())
