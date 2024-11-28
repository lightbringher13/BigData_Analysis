import numpy as np
import pandas as pd

# 제2회 빅분기 기출 작업형1 1번
df = pd.read_csv("../data/boston.csv")
df = df.sort_values("CRIM", ascending=False)
df.iloc[0:10, 1] = df.iloc[9, 1]
df = df.loc[df["AGE"] >= 80]
print("%.2f" % df["CRIM"].mean())

# 제2회 빅분기 기출 작업형1 2번
df = pd.read_csv("../data/housing.csv")
# df.info()
# print(df.isna().sum())
res = 20640 * 0.8
df = df.iloc[:int(res), :]
before_mean = df["total_bedrooms"].std()
df["total_bedrooms"] = df["total_bedrooms"].fillna(
    df["total_bedrooms"].median())
# print(df.isna().sum())
after_mean = df["total_bedrooms"].std()
res = before_mean - after_mean
print("%.2f" % res)

# 제2회 빅분기 기출 작업형1 3번
df = pd.read_csv("../data/medicalCost.csv")
df.info()
upper = df["charges"].mean() + df["charges"].std() * 1.5
lower = df["charges"].mean() - df["charges"].std() * 1.5
df = df.loc[(df["charges"] >= upper) | (df["charges"] <= lower)]
df = df.sum()
print(df)

# 제 3회 빅분기 기출 작업형1 1번
df = pd.read_csv("../data/housing.csv")
print(df.isna().sum())
df = df.dropna()
print(len(df) * 0.7)
df = df.iloc[:14303, :]
df.info()
res = df["housing_median_age"].quantile(0.25)
print(res)

# 제 3회 빅분기 기출 작업형1 2번
df = pd.read_csv("../data/titanic.csv")
df.info()
df = df.isna().sum()/len(df)
print(df)
df = df.sort_values(ascending=False)
print(df)
print(df.index[0])

# 제 3회 빅분기 기출 작업형1 3번
df = pd.read_csv("../data/disease.csv")
df.info()
print(df)
df = df.loc[df["year"] == 2000].T
print(df)
df = df.iloc[1:]
mean = df[2].mean()
print(mean)
df = df.loc[df[2] > mean]
print(len(df))

# 제 4회 빅분기 기출 작업형1 1번
df = pd.read_csv("../data/4th_customer.csv")
df.info()
print(df)
Q1 = df["방문 일수"].quantile(0.25)
Q3 = df["방문 일수"].quantile(0.75)
IQR = Q3 - Q1
print(IQR)
print(int(IQR))

# 제 4회 빅분기 기출 작업형1 2번
df = pd.read_csv("../data/4th_facebook.csv")
df.info()
print(df)
df = df.loc[((df["num_loves"] + df["num_wows"])/df["num_reactions"] > 0.4) &
            ((df["num_loves"] + df["num_wows"])/df["num_reactions"] < 0.5) & (df["status_type"] == "video")]

print(len(df))

# 제 4회 빅분기 기출 작업형1 3번
df = pd.read_csv("../data/4th_netflix.csv")
df.info()
df["date_added"] = df["date_added"].str.lstrip()
df['date_added'] = pd.to_datetime(df['date_added'])
df = df.loc[(df['date_added'].dt.strftime("%Y-%m") == "2018-01")
            & (df["country"] == "United Kingdom")]
print(len(df))

# 제 5회 빅분기 기출 작업형1 1번
df = pd.read_csv("../data/전국종량제봉투가격표준데이터.csv", encoding="euckr")
print(df[["종량제봉투종류", "종량제봉투용도"]])
df.info()
df = df.loc[(df["종량제봉투종류"] == '규격봉투') & (
    df["종량제봉투용도"] == "음식물쓰레기") & (df["2ℓ가격"] > 0)]
df = df["2ℓ가격"].mean()
print(round(df))

# 제 5회 빅분기 기출 작업형1 2번
df = pd.read_csv("../data/body.csv")
df.info()
print(df)
df["BMI"] = df["체중 : kg"] / ((df["신장 : cm"]/100)**2)
normal = df.loc[(df["BMI"] >= 18.5) & (df["BMI"] < 23)]
over = df.loc[(df["BMI"] >= 23) & (df["BMI"] < 25)]
normal.info()
over.info()
res = len(normal) - len(over)
print(res)

# 제 5회 빅분기 기출 작업형1 3번
df = pd.read_csv("../data/전출입학생수.csv", encoding="euckr")
df.info()
print(df)
df["순전입학생수"] = df["전입학생수합계(명)"] - df["전출학생수합계(명)"]
df = df.sort_values("순전입학생수", ascending=False)
print(df.iloc[0, 47])

# 제 6회 빅분기 기출 작업형1 1번
df = pd.read_csv("../data/Fire_Department_Calls_for_Service_Sample.csv")
df.info()
print(df[["Received DtTm", "Dispatch DtTm"]])
df["Received DtTm"] = pd.to_datetime(df["Received DtTm"])
df["Dispatch DtTm"] = pd.to_datetime(df["Dispatch DtTm"])
df["prep_time"] = df["Dispatch DtTm"] - df["Received DtTm"]
df["prep_time"] = df["prep_time"].dt.total_seconds()
df = df.groupby(
    ["Battalion", "year", "month"], as_index=False)["prep_time"].mean()
df = df.sort_values("prep_time", ascending=False)
print(round(df.iloc[0, 3]/60))

# 제 6회 빅분기 기출 작업형1 2번
df = pd.read_csv("../data/school_data.csv")
print(df)
df["std/tea"] = (df["student_1"]+df["student_1"]+df["student_1"] +
                 df["student_1"] + df["student_1"]) / df["teacher"]
print(df)

# 제 6회 빅분기 기출 작업형1 3번
df = pd.read_csv("../data/crime.csv")
df["년월"] = pd.to_datetime(df["년월"])
df["총범죄자수"] = df.iloc[:, 1:].sum(axis=1)
print(df)
res = df.groupby([df["년월"].dt.year, df["년월"].dt.month])["총범죄자수"].mean()
res = df.groupby(df["년월"].dt.year)["총범죄자수"].mean().sort_values(ascending=False)
print(res.iloc[0])
