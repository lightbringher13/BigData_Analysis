import datetime
import pandas as pd

# 1
df = pd.read_csv("../data/youtube.csv")
df.info()
res = df.groupby("channelTitle").size().sort_values(ascending=False)
res = res.index[0:10].tolist()
print(res)

# # 2
res = df.loc[df["dislikes"] > df["likes"], "channelTitle"].unique()
res = res.tolist()
print(res)

# # 3
res = df.sort_values(["channelId", "channelTitle"]
                     ).drop_duplicates("channelTitle")
res = res.groupby("channelId", as_index=False)[
    "channelTitle"].size()
res = res.loc[res["size"] > 1]
print(len(res))

# # 4
df["trending_date2"] = pd.to_datetime(df["trending_date2"])
res = df.loc[df["trending_date2"].dt.day_name() == "Sunday"]
res = res.groupby("categoryId").size().sort_values(ascending=False)
res = res.index[0]
print(res)

# # 5
# df["trending_date2"] = df["trending_date2"].dt.day_name()
# res = df.groupby(["categoryId", "trending_date2"]).size().unstack()
res = df.pivot_table(index="categoryId",
                     columns="trending_date2", aggfunc="size")
print(res)

# # 6
df.info()
res = df.loc[df["view_count"] != 0]
res["ratio"] = res["comment_count"]/res["view_count"]
res = res.sort_values("ratio", ascending=False)
print(res.iloc[0, 1])

# # 7
df.info()
res = df.loc[df["view_count"] != 0]
res["ratio"] = res["comment_count"]/res["view_count"]
res = res.loc[res["ratio"] != 0]
res = res.sort_values("ratio", ascending=True)
print(res.iloc[0, 1])

# # 8
df.info()
res = df.loc[(df["likes"] != 0) & (df["dislikes"] != 0)]
res["ratio"] = res["dislikes"]/res["likes"]
res = res.sort_values("ratio")
print(res.iloc[0, 1])

# # 9
df.info()
res = df.groupby("channelTitle")[
    "trending_date2"].size().sort_values(ascending=False)
print(res.index[0])

# # 10
df.info()
res = df.groupby("title", as_index=False)["channelId"].count()
res = res.loc[res["channelId"] >= 20].reset_index(drop=True)
print(len(res))

# # 11
channel = pd.read_csv("../data/channelInfo.csv")
video = pd.read_csv("../data/videoInfo.csv")
video["ct"] = pd.to_datetime(video["ct"])
res = video.groupby("videoname").size()
print(res)

# # 12
res = video.sort_values(["videoname", "ct"], ascending=[True, False])
res = res[["videoname", "ct", "viewcnt"]]
res = res.drop_duplicates("videoname", keep="first")
print(res)

# # 13
res = channel.loc[channel["ct"] >= "2021-10-03"]
res = res.sort_values(["channelname", "ct"])
res = res.drop_duplicates("channelname")[["channelname", "subcnt"]]
print(res)

# # 14
res = channel.loc[(channel["ct"] >= "2021-10-03 03:00:00") &
                  (channel["ct"] <= "2021-11-01 15:00:00")]
start = res.sort_values(["channelname", "ct"]).drop_duplicates(
    "channelname")[["channelname", "subcnt"]]
end = res.sort_values(["channelname", "ct"], ascending=[
                      True, False]).drop_duplicates("channelname")[["channelname", "subcnt"]]
res = pd.merge(start, end, on="channelname", how="inner")
res["del"] = res["subcnt_y"] - res["subcnt_x"]
res = res[["channelname", "del"]]
print(res)

# # 15 2024-11-22
res = video.sort_values(["videoname", "ct"])
print(res)
res["diff"] = res["ct"].diff().dt.total_seconds()/60
res = res.loc[res["videoname"].str.contains("1")]
res = res.loc[(res["diff"] >= 20) |
              (res["diff"] <= 5)]
print(res)

# # 16
res = video.sort_values(["videoname", "ct"])
res = res.drop_duplicates("videoname")
res["date"] = res["ct"].dt.date
res = res[["date", "videoname"]]
print(res)

# # 17
res = video.sort_values(["videoname", "ct"])
res = res.loc[res["ct"].dt.hour >= 21].groupby("videoname").head(1)
print(res[["videoname", "viewcnt", "ct"]])

# # 18
res = video.sort_values(["videoname", "ct"], ascending=[
                        True, False]).groupby("videoname").head(1)
res["ratio"] = res["dislikecnt"]/res["likecnt"]
print(res[["videoname", "ratio"]])


# # 19
res = video.loc[(video["ct"] >= "2021-11-01 00:00:00") &
                (video["ct"] <= "2021-11-01 15:00:00")]
res = res.sort_values(["videoname", 'ct'])[["videoname", "viewcnt"]]
start = res.groupby("videoname").head(1)
end = res.groupby("videoname").tail(1)
res = pd.merge(start, end, on="videoname", how="inner")
res["del"] = res["viewcnt_y"] - res["viewcnt_x"]
print(res[["videoname", "del"]])


# # 20
res = video.loc[video.duplicated()]
print(res[["videoname", "ct"]])

# # 21
df = pd.read_csv("../data/worldcupgoals.csv")
res = df.groupby("Country")["Goals"].sum().sort_values(ascending=False).head(5)
print(res)

# # 22
res = df.groupby("Country")["Player"].count(
).sort_values(ascending=False).head(5)
print(res)

# # 23


def check_len_4(x):
    lst = x.split("-")
    for val in lst:
        if len(val) != 4:
            return True
    return False


res = df.loc[df["Years"].apply(check_len_4)]
print(len(res))

# # 24
res = df.loc[~df["Years"].apply(check_len_4)]
print(len(res))

# # 25
df["LenCup"] = df["Years"].str.split("-").str.len()
print(df["LenCup"])
res = df.loc[df["LenCup"] == 4, "Player"]
print(len(res))

# # 26
res = df.loc[(df["Country"] == "Yugoslavia") & (df["LenCup"] == 2), "Player"]
print(len(res))

# # 27


def check(x):
    if "2002" in x:
        return True
    else:
        return False


res = df.loc[df["Years"].str.split("-").apply(check)]
print(len(res))

# # 28
res = df.loc[df["Player"].str.lower().str.contains("carlos")]
print(len(res))

# # 29
res = df.loc[df["LenCup"] == 1].sort_values(
    "Goals", ascending=False).iloc[0, 0]
print(res)

# # 30
res = df.loc[df["LenCup"] == 1].groupby(
    "Country").size().sort_values(ascending=False).index[0]
print(res)

# # 31
df = pd.read_csv("../data/seoul_bi.csv")
df["대여일자"] = pd.to_datetime(df["대여일자"])
res = df.groupby("대여일자").size()
print(res)

# # 32
df["day_name"] = df["대여일자"].dt.day_name()
res = df.groupby("day_name")["이용건수"].sum()
print(res)

# # 33
res = df.groupby(["day_name", "대여소번호"], as_index=False)["이용건수"].sum()
res = res.sort_values(["day_name", "이용건수"], ascending=[True, False])
res = res.groupby("day_name").head(1)
print(res)


# # 34
df.info()
res = df.loc[df["대여구분코드"].str.contains("일일권")]
res = res.groupby("연령대코드", as_index=False)["대여구분코드"].count()
res1 = df.groupby("연령대코드", as_index=False)["대여구분코드"].count()
res["ratio"] = res["대여구분코드"]/res1["대여구분코드"]
print(res)

# # 35
res = df.groupby("연령대코드")["이동거리"].mean()
print(res)

# # 36
df.info()
res = df.loc[df["연령대코드"] == "20대"]
res = res.loc[res["이동거리"] >= res["이동거리"].mean()]
res = res.sort_values(["대여일자", "대여소번호"], ascending=[False, False])
res = res.iloc[0:200, 8].astype(float).mean()
print("%.3f" % res)

# # 37
res = df.loc[df["대여일자"].dt.strftime("%m-%d") == "06-07"]
res = res.loc[res["연령대코드"] == "~10대"]["이용건수"].median()
print(res)

# # 38
res = df.loc[(df["대여일자"].dt.weekday < 5) & (df["사용시간"].isin([6, 7, 8]))]
res = res.groupby(["사용시간", "대여소번호"], as_index=False)["이용건수"].sum()
res = res.sort_values(
    ["사용시간", "이용건수"], ascending=False).groupby("사용시간").head(3)
print(res)

# # 39
res = df.loc[df["이동거리"] >= df["이동거리"].mean()]["이동거리"].std()
print(res)

# # 40
df["sex"] = df["성별"].apply(lambda x: "남" if x.lower() == "m" else "여")
res = df.groupby("sex")["이동거리"].mean()
print(res)

# # 41
df = pd.read_csv("../data/happiness.csv")
df.info()


# # 42
# res = df.loc[df["행복랭킹"] <= 50]
# res = res.groupby("년도")["점수"].mean()
# print(res)

# # 43
# df.info()
# res = df.loc[df["년도"] == 2018]
# res = res[["점수", "부패에 대한인식"]].corr()
# print(res)

# # 44
# res = df.groupby(["행복랭킹", "나라명"], as_index=False).size()
# res = res.loc[res["size"] == 2]
# print(len(res))

# # 45
# res = df.loc[df["년도"] == 2019].drop("나라명", axis=1)
# res = res.corr().unstack().reset_index().dropna()
# res.columns = ["v1", "v2", "corr"]
# res = res.sort_values("corr", ascending=False)
# res = res.loc[res["v1"] != res["v2"]]
# res = res.drop_duplicates("corr")
# print(res.head())

# # 46
# res = df.sort_values(["년도", "점수"]).groupby("년도").head(5)[["년도", "점수"]]
# res = res.groupby("년도")["점수"].mean().reset_index()
# print(res)

# # 47
# over = df.loc[(df["년도"] == 2019) & (df["상대GDP"] >= df["상대GDP"].mean())]
# under = df.loc[(df["년도"] == 2019) & (df["상대GDP"] <= df["상대GDP"].mean())]
# over = over["점수"].mean()
# under = under["점수"].mean()
# res = over - under
# print(res)

# # 48
# res = df.sort_values(["년도", "부패에 대한인식"], ascending=[True, False]).groupby(
#     "년도").head(20)[["년도", "부패에 대한인식"]]
# res = res.groupby("년도")["부패에 대한인식"].mean()
# print(res)

# # 49
# res = df.loc[(df["행복랭킹"] <= 50) & (df["년도"] == 2018)]
# res1 = df.loc[(df["행복랭킹"] >= 50) & (df["년도"] == 2019)]
# ans = res.loc[res["나라명"].isin(res1["나라명"])]
# print(len(ans))

# # 50
# df["size"] = df.groupby("나라명")["나라명"].transform("size")
# res = df.loc[df["size"] >= 2]
# res_2018 = res.loc[res["년도"] == 2018][["년도", "나라명", "점수"]].set_index("나라명")
# res_2019 = res.loc[res["년도"] == 2019][["년도", "나라명", "점수"]].set_index("나라명")
# res = res_2019["점수"] - res_2018["점수"]
# res = res.reset_index()
# res = res.sort_values("점수", ascending=False)
# print(res)

# # 51
# df = pd.read_csv("../data/Tetuan_City_power_consumption.csv")
# df["DateTime"] = pd.to_datetime(df["DateTime"])
# res = df.groupby(df["DateTime"].dt.month).size()
# print(res)

# # 52
# df["month"] = df["DateTime"].dt.month
# df["hour"] = df["DateTime"].dt.hour
# res = df.loc[df["month"] == 3]
# res["hour_temp_mean"] = res.groupby(df["hour"])[
#     "Temperature"].transform("mean")
# res = res.sort_values("hour_temp_mean").drop_duplicates(
#     ["hour", "hour_temp_mean"])
# print(res[["hour", "hour_temp_mean"]])

# # 53
# res = res[["hour", "hour_temp_mean"]].sort_values(
#     "hour_temp_mean", ascending=False)
# print(res)

# # 54
# res = df.loc[df["Zone 1 Power Consumption"] >
#              df["Zone 2 Power Consumption"]]["Humidity"].mean()
# print(res)

# # 55
# res = df[["Zone 1 Power Consumption",
#           "Zone 2 Power Consumption", "Zone 3 Power Consumption"]].corr()
# print(res)

# # 56

# def temp_grade(x):
#     if x < 10:
#         return "A"
#     elif x < 20:
#         return 'B'
#     elif x < 30:
#         return 'C'
#     else:
#         return 'D'

# df["temp_grade"] = df["Temperature"].apply(temp_grade)
# res = df.groupby("temp_grade").size()
# print(res)

# # 57
# res = df.loc[(df["month"] == 6) & (df["hour"] == 12)]["Temperature"].std()
# print(res)

# # 58
# res = df.loc[(df["month"] == 6) & (df["hour"] == 12)]["Temperature"].var()
# print(res)

# # 59
# res = df.loc[df["Temperature"] >=
#              df["Temperature"].mean()].sort_values("Temperature", ascending=True)["Humidity"].iloc[3]
# print(res)

# # 60
# res = df.loc[df["Temperature"] >=
#              df["Temperature"].median()].sort_values("Temperature")["Humidity"].iloc[3]
# print(res)

# # 61
# df = pd.read_csv("../data/pokemon.csv")
# df.info()

# Legendary_HP_mean = df.loc[df["Legendary"] == True]["HP"].mean()
# Non_Legendary_HP_mean = df.loc[df["Legendary"] == False]["HP"].mean()
# res = Legendary_HP_mean - Non_Legendary_HP_mean
# print(res)

# # 62
# res = df.groupby("Type 2", as_index=False).size(
# ).sort_values("size", ascending=False)
# print(res.iloc[0])

# # 63
# res = df.groupby("Type 1", as_index=False).size(
# ).sort_values("size", ascending=False)
# water_Attack_mean = df.loc[df["Type 1"] == "Water"]["Attack"].mean()
# water_Defense_mean = df.loc[df["Type 1"] == "Water"]["Defense"].mean()
# print(water_Attack_mean)
# print(water_Defense_mean)
# res = water_Attack_mean/water_Defense_mean
# print(res)

# # 64
# res = df.loc[df["Legendary"] == True].groupby("Generation")["Legendary"].size()
# res = res.reset_index(name="size").sort_values("size", ascending=False)
# print(res)

# # 65
# res = df[["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]].corr()
# res = res.unstack().reset_index(name="corr")
# res = res.loc[res["level_0"] != res["level_1"]]
# res = res.sort_values("corr", ascending=False)
# res = res.iloc[0]
# print(res)

# # 66
# res = df.sort_values(["Generation", "Attack"], ascending=[
#                      True, True]).groupby("Generation").head(3)
# res = res["Attack"].mean()
# print(res)

# # 67
# res = df.sort_values(["Generation", "Attack"], ascending=[
#                      True, False]).groupby("Generation").head(5)["Attack"].mean()
# print(res)

# # 68
# res = df.groupby(["Type 1", "Type 2"],
#                  as_index=False).size().sort_values("size", ascending=False).iloc[0]
# print(res)

# # 69
# res = df.groupby(["Type 1", "Type 2"], as_index=False).size()
# res = res.loc[res["size"] == 1].reset_index(drop=True)
# print(len(res))

# # 70
# res = df.groupby(["Type 1", "Type 2"], as_index=False).size()
# res = res.loc[res["size"] == 1]
# df = pd.merge(res, df, on=["Type 1", "Type 2"], how="inner")
# res = df.groupby("Generation")["size"].sum()
# print(res)

# # 71
# df = pd.read_csv("../data/body.csv")
# df.info()

# res = df["수축기혈압(최고) : mmHg"] - df["이완기혈압(최저) : mmHg"]
# res = res.mean()
# print(res)

# # 72
# res = df.loc[df["측정나이"].between(50, 59)]["신장 : cm"].mean()
# print(res)

# # 73
# df["연령대"] = df["측정나이"] // 10 * 10
# res = df.groupby("연령대").size()
# print(res)

# # 74
# res = df.groupby(["연령대", "등급"], as_index=False).size()
# print(res)

# # 75
# df.info()
# M_A_mean = df.loc[(df["등급"] == "A") & (df["측정회원성별"] == "M")]["체지방율 : %"].mean()
# M_D_mean = df.loc[(df["등급"] == "D") & (df["측정회원성별"] == "M")]["체지방율 : %"].mean()
# if M_A_mean > M_D_mean:
#     res = M_A_mean - M_D_mean
# else:
#     res = M_D_mean - M_A_mean
# print(res)

# # 76
# df.info()
# F_A_mean = df.loc[(df["등급"] == "A") & (df["측정회원성별"] == "F")]["체중 : kg"].mean()
# F_D_mean = df.loc[(df["등급"] == "D") & (df["측정회원성별"] == "F")]["체중 : kg"].mean()
# if F_A_mean > F_D_mean:
#     res = F_A_mean - F_D_mean
# else:
#     res = F_D_mean - F_A_mean
# print(res)

# # 77
# df["bmi"] = df["체중 : kg"] / ((df["신장 : cm"]/100) ** 2)
# res = df.loc[df["측정회원성별"] == "M"]["bmi"].mean()
# print(res)

# # 78
# res = df.loc[df["체지방율 : %"] >= df["bmi"]]["체중 : kg"].mean()
# print(res)

# # 79
# M = df.loc[df["측정회원성별"] == "M"]["악력D : kg"].mean()
# F = df.loc[df["측정회원성별"] == "F"]["악력D : kg"].mean()
# res = M - F
# print(res)

# # 80
# M = df.loc[df["측정회원성별"] == "M"]["교차윗몸일으키기 : 회"].mean()
# F = df.loc[df["측정회원성별"] == "F"]["교차윗몸일으키기 : 회"].mean()
# res = M - F
# print(res)

# # 81
# df = pd.read_csv("../data/weather2.csv")
# df.info()
# df["time"] = pd.to_datetime(df["time"])
# df["month"] = df["time"].dt.month
# df["hour"] = df["time"].dt.hour
# res = df.loc[(df["month"].isin([6, 7, 8])) & (df["이화동기온"] > df["수영동기온"])]
# print(len(res))

# # 82
# res = df.sort_values("이화동강수", ascending=False).iloc[0]
# res1 = df.sort_values("수영동강수", ascending=False).iloc[0]
# print(res, res1)

# # 83
# df = pd.read_csv("../data/customerInfo.csv")
# df.info()
# res = df.loc[df["Gender"] == "Male"].groupby(
#     "Geography", as_index=False)["Exited"].sum()
# res = res.sort_values("Exited", ascending=False)
# print(res.iloc[0])

# # 84
# res = df.loc[(df["HasCrCard"] == 1) & (
#     df["IsActiveMember"] == 1)]["Age"].mean()
# print("%.4f" % res)

# # 85
# res = df.loc[df["Balance"] >= df["Balance"].median()]["CreditScore"].std()
# print("%.3f" % res)

# # 86
# df = pd.read_csv("../data/adult_health_2018.csv")
# df.info()
# df["혈압차"] = df["수축기혈압"] - df["이완기혈압"]
# res = df.groupby("연령대코드(5세단위)", as_index=False)["혈압차"].var()
# res = res.rename(columns={"혈압차": "분산"})
# res = res.sort_values("분산", ascending=False).iloc[4]
# print(res)

# # 87
# df["비만도"] = df["허리둘레"]/df["신장(5Cm단위)"]
# df["비만"] = 0
# df.loc[df["비만도"] >= 0.58, "비만"] = 1
# print(df[["비만도", "비만"]])
# ratio = df.loc[df["성별코드"] == "M"]["비만"].sum()/df.loc[df["성별코드"]
#                                                      == "F"]["비만"].sum()
# print(ratio)

# # 88
# df = pd.read_csv("../data/carInsurance.csv")
# df.info()
# res = df.loc[df["Vehicle_Age"].str.contains("> 2")]
# res = res.loc[res["Annual_Premium"] >= df["Annual_Premium"].median()]
# res = res["Vintage"].mean()
# print(res)

# # 89
# res = df.pivot_table(values="Annual_Premium",
#                      index="Vehicle_Age", columns="Gender", aggfunc="mean")
# print(res)

# # 90
# df = pd.read_csv("../data/mobilePhone.csv")
# df.info()
# res = df.groupby(["price_range", "n_cores"], as_index=False).size()
# res = res.sort_values(["price_range", "size"], ascending=[True, False])
# res = res.groupby("price_range").head(1).reset_index(drop=True)
# print(res)

# # 91
# res = df.loc[df["price_range"] == 3]
# res = res.corr().unstack().reset_index()
# res = res.rename(columns={0: "corr"})
# res = res.loc[res["level_0"] != res["level_1"]]
# res = res.loc[res["level_0"] < res["level_1"]]
# res = res.sort_values("corr",
#                       ascending=False)
# print(res.iloc[1])

# # 92
# df = pd.read_csv("../data/airlineSatisfaction.csv")
# df.info()
# res = df.loc[(df["Arrival Delay in Minutes"].isna())]
# res = res.groupby(["Class", "satisfaction"]).size().unstack()
# res = res.loc[res["neutral or dissatisfied"] < res["satisfied"]]
# print(res)

# # 93
# df = pd.read_csv("../data/waterPotability.csv")
# df.info()
# res = df.dropna(subset="ph")
# Q1 = res["ph"].quantile(0.25)
# res = res.loc[res["ph"] <= Q1]["ph"].mean()
# print(res)

# # 94
# df = pd.read_csv("../data/medicalCost.csv")
# df.info()
# Q4_y = df.loc[df["smoker"] == "yes"]["charges"].quantile(0.90)
# Q4_n = df.loc[df["smoker"] == "no"]["charges"].quantile(0.90)
# mean_y = df.loc[(df["smoker"] == "yes") & (
#     df["charges"] >= Q4_y)]["charges"].mean()
# mean_n = df.loc[(df["smoker"] == "no") & (
#     df["charges"] >= Q4_n)]["charges"].mean()
# res = mean_y - mean_n
# print(res)

# # 95
# df = pd.read_csv("../data/kingcountyPrice.csv")
# df.info()
# res = df.groupby("bedrooms", as_index=False).size()
# res_up = df.loc[df["bedrooms"] == 3]["price"].quantile(0.9)
# res_un = df.loc[df["bedrooms"] == 3]["price"].quantile(0.1)
# res = res_up - res_un
# print(res)

# # 96 unsolved
# df = pd.read_csv("../data/admission.csv")
# df.info()

# # 97 unsolved
# df = pd.read_csv("../data/redwine.csv")
# df.info()

# # 98
# df = pd.read_csv("../data/drug.csv")
# df.info()
# df["Age2"] = df["Age"].apply(lambda x: x//10 * 10)
# res = df.loc[df["Sex"] == "M"].groupby("Age2")["Na_to_K"].mean()
# print(res)

# # 99
# df = pd.read_csv("../data/audit.csv")
# df.info()
# res = df.groupby("Risk").mean(numeric_only=True)[["Score_A", "Score_B"]]
# print(res)

# # 100
# df = pd.read_csv("../data/motion.csv")
# df.info()
# res0 = df.loc[df["pose"] == 0].median()
# res1 = df.loc[df["pose"] == 1].median()
# res = res1 - res0
# res = res.abs().sort_values(ascending=False)
# print(res)

# # 101 unsolved
# df = pd.read_csv("../data/hyundai.csv")
# df.info()
# df["size"] = df.groupby("model").transform("size")
# res = df.sort_values("size", ascending=False).groupby("model").head(3)
# print(res)

# # 102
# df = pd.read_csv("../data/diabetes.csv")
# df.info()
# res0 = df.loc[df["Outcome"] == 0].mean()
# res1 = df.loc[df["Outcome"] == 1].mean()
# res = res1 - res0
# print(res)

# # 103
# df = pd.read_csv("../data/NFLX.csv")
# df.info()
# df["Date"] = pd.to_datetime(df["Date"])
# res = df.loc[df["Date"].dt.month == 5]
# res = res.groupby(df["Date"].dt.year)["Open"].mean()
# print(res)

# # 104
# df = pd.read_csv("../data/nba.csv", encoding='latin', sep=';')
# df.info()
# res = df.loc[df["Tm"] == "TOR"]["Age"].mean()
# print("%.4f" % res)

# # 105
# res = df.loc[df["Age"] == df["Age"].min()]
# res = res.groupby("Pos", as_index=False).size(
# ).sort_values("size", ascending=False)
# print(res.iloc[0])

# # 106
# df["first_name"] = df["Player"].apply(lambda x: x.split(" ")[0])
# res = df.groupby("first_name", as_index=False).size(
# ).sort_values("size", ascending=False)
# print(res.iloc[0])

# # 107
# res = df.groupby("Pos")["PTS"].mean().sort_values(ascending=True)
# print(res)

# # 108 == 107 duplicated

# # 109
# res = df.groupby("Tm")["G"].max()
# res = res.mean()
# print(res)

# # 110
# res = df.loc[(df["Pos"].isin(["C", "PF"])) & (df["Tm"] == "MIA")]["MP"].mean()
# print(res)

# # 111
# res = df["G"].mean() * 1.5
# res = df.loc[df["G"] >= res]["3P"].mean()
# print(res)

# # 112
# res_over = df.loc[df["Age"] >= df["Age"].mean()]["G"].mean()
# res_under = df.loc[df["Age"] < df["Age"].mean()]["G"].mean()
# res = res_over - res_under
# print(res)

# # 113
# res = df.groupby("Tm", as_index=False)[
#     "Age"].mean().sort_values("Age", ascending=True).iloc[0, 0]
# print(res)

# # 114
# res = df.groupby("Pos")["MP"].mean()
# print(res)
