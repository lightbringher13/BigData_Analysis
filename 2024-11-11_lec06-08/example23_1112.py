import pandas as pd

# grading method "qcut()"
# emp = pd.read_csv("../data/emp.csv")
# emp["rank"] = emp["sal"].rank(method="dense", ascending=False).astype(int)
# cuts = 4
# emp["sal_grade"] = pd.qcut(emp["rank"], q=cuts, labels=[
#                            'Q1', 'Q2', 'Q3', 'Q4'])
# print(emp[["ename", "sal", "rank", "sal_grade"]
#           ].sort_values("sal_grade", ascending=True))

# print ename,age,grade 5 grade of ranked age
# emp20 = pd.read_csv("../data/emp20.csv", encoding="euckr")
# emp20["rank"] = emp20["age"].rank(method="dense", ascending=False).astype(int)
# emp20["age_grade"] = pd.qcut(emp20["rank"], q=5, labels=[
#     'Q1', 'Q2', 'Q3', 'Q4', 'Q5'])
# print(emp20[["ename", "age", "rank", "age_grade"]].sort_values("rank"))

# print age and fill null with age_mean
# tit = pd.read_csv("../data/train.csv")
# tit.info()
# age_mean = tit["Age"].mean()
# tit["Age"].fillna(round(age_mean),i)

# print Age,rank,Age_grade descending order
tit = pd.read_csv("../data/train.csv")
age_mean = round(tit["Age"].mean())
print(age_mean)
tit["Age"].fillna(age_mean, inplace=True)
tit["rank"] = tit["Age"].rank(method="dense", ascending=False).astype(int)
cuts = 4
tit["age_grade"] = pd.qcut(tit["rank"], q=cuts, labels=[
                           'Q1', 'Q2', 'Q3', 'Q4'])
result = tit.sort_values(by="rank", ascending=True)[["Age", "age_grade"]]
print(result)
