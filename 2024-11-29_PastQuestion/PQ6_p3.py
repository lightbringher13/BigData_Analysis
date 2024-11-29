import statsmodels.api as sm
from scipy.stats import chi2_contingency
import numpy as np
import pandas as pd

# 빅분기 6회 작업형3 1번
a_man = 600
a_woman = 550
a_man_smoker = 600 * 0.2
a_woman_smoker = 550 * 0.26
data = np.array([
    [a_man_smoker, 600 - a_man_smoker],
    [a_woman_smoker, 550-a_woman_smoker]
])
chi2, p_value, df, expected = chi2_contingency(data)
print(p_value)

# 빅분기 6회 작업형3 2번
df = pd.read_csv("../data/PQ6_p3_01.csv")
df.info()
x = df[["age", 'Cholesterol']]
y = df["weight"]
x = sm.add_constant(x)
model = sm.OLS(y, x).fit()
summary = model.summary()
print(summary)
# 빅분기 6회 작업형3 3번
print(model.params["age"])

# 빅분기 6회 작업형3 4번
if model.pvalues["Cholesterol"] < 0.05:
    print("귀무가설 기각")
else:
    print("귀무가설 채택")

# 빅분기 6회 작업형3 5번
pred = model.predict([1, 55, 72.6])
print(pred)
