from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

# 제2회 빅분기 기출 작업형1 1번 *** iloc 사용하기
# df = pd.read_csv("../data/boston.csv")
# df.info()
# df = df.sort_values("CRIM", ascending=False)
# df.iloc[0:10, 1] = df.iloc[9, 1]
# df = df.loc[df["AGE"] >= 80]["CRIM"].mean()
# print(df)


# # 제2회 빅분기 기출 작업형1 2번 *** 데이터셋 나누기 80%
# df = pd.read_csv("../data/housing.csv")
# df.info()
# res = 20640 * 0.8
# print(res)
# train = df.iloc[:int(res), :]
# train.info()
# before = train["total_bedrooms"].std()
# train['total_bedrooms'] = train["total_bedrooms"].fillna(
#     train["total_bedrooms"].median())
# after = train["total_bedrooms"].std()
# res = after - before
# res = abs(res)
# print(res)


# # 제2회 빅분기 기출 작업형1 3번 ***** 이상값 | 매우중요 벌써 두번째
# df = pd.read_csv("../data/medicalCost.csv")
# df.info()
# upper = df["charges"].mean() + df["charges"].std() * 1.5
# lower = df["charges"].mean() - df["charges"].std() * 1.5
# df = df.loc[(df["charges"] <= lower) | (df["charges"] >= upper)]
# res = df["charges"].sum()
# print(res)


# # 제 3회 빅분기 기출 작업형1 1번
# df = pd.read_csv("../data/housing.csv")
# df.info()
# print(df.isna().sum())
# df = df.dropna()
# df.info()
# print(20433 * 0.7)
# df = df.iloc[:14303, :]
# res = df["housing_median_age"].quantile(0.25)
# print(res)


# # 제 3회 빅분기 기출 작업형1 2번 **** 결측값 비율 구하는 방법 암기
# df = pd.read_csv("../data/titanic.csv")
# df.info()
# df = df.isna().sum()/len(df)
# print(df)
# df = df.sort_values(ascending=False)
# print(df)
# print(df.index[0])


# # 제 3회 빅분기 기출 작업형1 3번
# df = pd.read_csv("../data/disease.csv")
# df.info()
# print(df)
# df = df.loc[df["year"] == 2000].T
# print(df)
# res = df.iloc[1:, :][2].mean()
# print(round(res, 2))
# df = df.iloc[1:, :]
# res = df.loc[df[2] > res]
# print(len(res))


# # 제 4회 빅분기 기출 작업형1 1번
# df = pd.read_csv("../data/4th_customer.csv")
# df.info()
# print(df)
# Q1 = df["방문 일수"].quantile(0.25)
# Q3 = df["방문 일수"].quantile(0.75)
# IQR = Q3 - Q1
# print(IQR)
# print(int(IQR))

# # 제 4회 빅분기 기출 작업형1 2번
# df = pd.read_csv("../data/4th_facebook.csv")
# df.info()
# print(df)
# df = df.loc[((df["num_loves"] + df["num_wows"])/df["num_reactions"] > 0.4) &
#             ((df["num_loves"] + df["num_wows"])/df["num_reactions"] < 0.5) & (df["status_type"] == "video")]

# print(len(df))

# # 제 4회 빅분기 기출 작업형1 3번
# df = pd.read_csv("../data/4th_netflix.csv")
# df.info()
# df["date_added"] = df["date_added"].str.lstrip()
# df['date_added'] = pd.to_datetime(df['date_added'])
# df = df.loc[(df['date_added'].dt.strftime("%Y-%m") == "2018-01")
#             & (df["country"] == "United Kingdom")]
# print(len(df))

# # 제 5회 빅분기 기출 작업형1 1번
# df = pd.read_csv("../data/전국종량제봉투가격표준데이터.csv", encoding="euckr")
# print(df[["종량제봉투종류", "종량제봉투용도"]])
# df.info()
# df = df.loc[(df["종량제봉투종류"] == '규격봉투') & (
#     df["종량제봉투용도"] == "음식물쓰레기") & (df["2ℓ가격"] > 0)]
# df = df["2ℓ가격"].mean()
# print(round(df))

# # 제 5회 빅분기 기출 작업형1 2번
# df = pd.read_csv("../data/body.csv")
# df.info()
# print(df)
# df["BMI"] = df["체중 : kg"] / ((df["신장 : cm"]/100)**2)
# normal = df.loc[(df["BMI"] >= 18.5) & (df["BMI"] < 23)]
# over = df.loc[(df["BMI"] >= 23) & (df["BMI"] < 25)]
# normal.info()
# over.info()
# res = len(normal) - len(over)
# print(res)

# # 제 5회 빅분기 기출 작업형1 3번
# df = pd.read_csv("../data/전출입학생수.csv", encoding="euckr")
# df.info()
# print(df)
# df["순전입학생수"] = df["전입학생수합계(명)"] - df["전출학생수합계(명)"]
# df = df.sort_values("순전입학생수", ascending=False)
# print(df.iloc[0, 47])

# # 제 6회 빅분기 기출 작업형1 1번
# df = pd.read_csv("../data/Fire_Department_Calls_for_Service_Sample.csv")
# df.info()
# print(df[["Received DtTm", "Dispatch DtTm"]])
# df["Received DtTm"] = pd.to_datetime(df["Received DtTm"])
# df["Dispatch DtTm"] = pd.to_datetime(df["Dispatch DtTm"])
# df["prep_time"] = df["Dispatch DtTm"] - df["Received DtTm"]
# df["prep_time"] = df["prep_time"].dt.total_seconds()
# df = df.groupby(
#     ["Battalion", "year", "month"], as_index=False)["prep_time"].mean()
# df = df.sort_values("prep_time", ascending=False)
# print(round(df.iloc[0, 3]/60))

# # 제 6회 빅분기 기출 작업형1 2번
# df = pd.read_csv("../data/school_data.csv")
# print(df)
# df["std/tea"] = (df["student_1"]+df["student_1"]+df["student_1"] +
#                  df["student_1"] + df["student_1"]) / df["teacher"]
# print(df)

# # 제 6회 빅분기 기출 작업형1 3번
# df = pd.read_csv("../data/crime.csv")
# df["년월"] = pd.to_datetime(df["년월"])
# df["총범죄자수"] = df.iloc[:, 1:].sum(axis=1)
# print(df)
# res = df.groupby([df["년월"].dt.year, df["년월"].dt.month])["총범죄자수"].mean()
# res = df.groupby(df["년월"].dt.year)["총범죄자수"].mean().sort_values(ascending=False)
# print(res.iloc[0])

# # 제 7회 빅분기 기출 작업형1 1번
# df = pd.read_csv("../data/PQ7_p1_q1.csv")
# df.info()
# res = df.groupby("학생").count().T
# res["cnt"] = res.iloc[:, :].sum(axis=1)
# res = res.sort_values("cnt", ascending=False)
# df["국어_표준화"] = (df["국어"] - df["국어"].mean())/df["국어"].std(ddof=0)
# res = df["국어_표준화"].sort_values(ascending=False).iloc[0]

# print(res)

# # 제 7회 빅분기 기출 작업형1 2번
# df = pd.read_csv("../data/PQ7_p1_q2.csv")
# df.info()
# res = df.corr().unstack().reset_index(name="corr")
# res = res.loc[res["level_0"] == "var_11"]
# res["corr"] = res["corr"].abs()
# res = res.sort_values("corr", ascending=False)
# print(df["var_44"].mean())

# max_v = df.corr()['var_11'].abs().sort_values().index[-2]
# r = df[max_v].mean()
# print(r)

# # 제 7회 빅분기 기출 작업형1 3번
# df = pd.read_csv("../data/PQ7_p1_q3.csv")
# df.info()
# Q1 = df["var_6"].quantile(0.25)
# Q3 = df["var_6"].quantile(0.75)
# IQR = Q3 - Q1
# Q1_out = Q1 - IQR * 1.5
# Q3_out = Q3 + IQR * 1.5
# res = df["var_6"][(df["var_6"] < Q1_out) | (df["var_6"] > Q3_out)]
# print(len(res))
