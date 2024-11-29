from sklearn.preprocessing import LabelEncoder
import datetime
import pandas as pd

# # 1
# df = pd.read_csv("../data/youtube.csv")
# df.info()
# res = df.groupby("channelId", as_index=False).size(
# ).sort_values("size", ascending=False).iloc[0:10, 0]
# res = df.loc[df["channelId"].isin(res)]["channelTitle"].unique()
# print(res)

# # # # 2
# res = df.loc[df["dislikes"] > df["likes"]]["channelTitle"].unique()
# print(res)

# # # # 3
# res = df.sort_values(["channelId", "channelTitle"]
#                      ).drop_duplicates("channelTitle", keep="first")
# res = res.groupby("channelId", as_index=False).size(
# ).sort_values("size", ascending=False)
# res = res.loc[res['size'] > 1]

# print(len(res))

# # # # 4
# df["trending_date2"] = pd.to_datetime(df["trending_date2"])
# res = df.loc[df["trending_date2"].dt.day_name() == "Sunday"]
# res = res.groupby("categoryId").size().sort_values(ascending=False).index[0]
# print(res)

# # # # 5
# df["day_name"] = df["trending_date2"].dt.day_name()
# res = df.groupby(["categoryId", "day_name"]).size().unstack()
# print(res)

# # # # 6
# df.info()
# res = df.loc[df["view_count"] > 0]
# res['ratio'] = res['comment_count']/res['view_count']
# res = res.sort_values('ratio', ascending=False)
# print(res.iloc[0, 1])

# # # # 7
# # df.info()
# # res = df.loc[df["view_count"] != 0]
# # res["ratio"] = res["comment_count"]/res["view_count"]
# # res = res.loc[res["ratio"] != 0]
# # res = res.sort_values("ratio", ascending=True)
# # print(res.iloc[0, 1])

# # # # 8
# df.info()
# res = df.loc[(df['likes'] > 0) & (df['dislikes'] > 0)]
# res['ratio'] = res['dislikes']/res['likes']
# res = res.sort_values("ratio").iloc[0, 1]
# print(res)

# # # # 9
# df.info()
# res = df.groupby("channelTitle", as_index=False)["trending_date2"].count()
# res = res.sort_values("trending_date2").iloc[-1, 0]
# print(res)


# # # # 10
# df.info()
# res = df.groupby("title", as_index=False)["trending_date2"].count()
# res = res.rename(columns={"trending_date2": "count"})
# res = res.loc[res["count"] >= 20]
# print(len(res))


# # # # 11
# channel = pd.read_csv("../data/channelInfo.csv")
# video = pd.read_csv("../data/videoInfo.csv")
# video["ct"] = pd.to_datetime(video["ct"])
# channel["ct"] = pd.to_datetime(channel["ct"])
# res = video.groupby("videoname").size()
# print(res)

# # # # ***** 12 틀림 가장 최신의 날짜의 비디오 ascending=False
# res = video.sort_values(['videoname', 'ct'], ascending=[True, False]).drop_duplicates(
#     "videoname")[['videoname', 'viewcnt', 'ct']]
# print(res)

# # # # 13
# res = channel.loc[channel['ct'] >= "2021-10-03"]
# res = res.sort_values(['channelname', 'ct']).drop_duplicates(
#     'channelname', keep='first')
# res = res[["channelname", 'subcnt']]
# print(res)

# # # # 14 **** pd.merge 사용
# channel.info()
# res = channel.loc[(channel["ct"] >= "2021-10-03 03:00:00") &
#                   (channel["ct"] <= "2021-11-01 15:00:00")]
# res = res.sort_values(['channelname', 'ct'])[['channelname', 'subcnt']]
# first = res.groupby('channelname').head(1)
# last = res.groupby('channelname').tail(1)
# res = pd.merge(first, last, on='channelname', how='inner')
# res["del"] = res['subcnt_y'] - res['subcnt_x']
# print(res[['channelname', "del"]])


# # # # 15 **** total_seconds()
# res = video.loc[video['videoname'].str.contains('1')]
# res = res.sort_values('ct')
# res["diff"] = res["ct"].diff().dt.total_seconds()
# res = res.loc[(res['diff']/60 <= 5) |
#               (res['diff']/60 >= 20)]
# print(res)

# # # # 16 **** res['ct'].dt.date
# res = video.sort_values(['ct', 'videoname'])
# res = res.drop_duplicates('videoname')
# res['date'] = res['ct'].dt.date
# print(res[['date', 'videoname']])

# # # # 17
# res = video.loc[video["ct"].dt.strftime("%H") == '21']
# res = res.sort_values(['videoname', 'ct']).drop_duplicates('videoname')
# print(res[['videoname', 'viewcnt', 'ct']].sort_values(
#     'viewcnt', ascending=False))

# # # # 18
# video['ratio'] = video['dislikecnt']/video['likecnt']
# res = video.sort_values(['videoname', 'ratio'], ascending=[
#     True, False]).drop_duplicates('videoname')
# print(res[['videoname', 'ratio']])

# # # # 19
# res = video.loc[(video['ct'] <= "2021-11-01 15:00:00") &
#                 (video['ct'] >= "2021-11-01 00:00:00")]
# first = res.sort_values(["videoname", 'ct']).groupby(
#     "videoname").head(1)[["videoname", 'viewcnt']]
# last = res.sort_values(["videoname", 'ct']).groupby(
#     "videoname").tail(1)[["videoname", 'viewcnt']]
# res = pd.merge(first, last, on='videoname', how='inner')
# res['del'] = res['viewcnt_y'] - res['viewcnt_x']
# print(res[['videoname', 'del']])

# # # # 20
# res = video.loc[video.duplicated()]
# print(res)

# # # # 21
# df = pd.read_csv("../data/worldcupgoals.csv")
# res = df.groupby("Country", as_index=False)["Goals"].sum().sort_values(
#     "Goals", ascending=False).head(5)
# print(res)

# # # # 22
# df.info()
# res = df.groupby("Country", as_index=False)["Player"].count().sort_values(
#     "Player", ascending=False).head(5)
# print(res)

# # # # 23


# def check(x):
#     x = x.split("-")
#     for i in x:
#         if len(i) != 4:
#             return True
#     return False


# res = df.loc[df["Years"].apply(check)]

# print(len(res))

# # # # 24


# def check(x):
#     x = x.split("-")
#     for i in x:
#         if len(i) != 4:
#             return True
#     return False


# res = df.loc[~df["Years"].apply(check)]

# print(len(res))

# # # # 25
# df["LenCup"] = df['Years'].str.split("-").str.len()
# print(df["LenCup"])
# res = df.loc[df['LenCup'] == 4]
# print(len(res))

# # # # 26
# res = df.loc[df["Country"] == "Yugoslavia"]
# res = res.loc[res["LenCup"] == 2]
# print(len(res))
# # # # 27
# res = df.loc[df["Years"].str.contains("2002")]
# print(len(res))

# # # # 28
# res = df.loc[df["Player"].str.lower().str.contains("carlos")]
# print(len(res))

# # # # 29
# res = df.loc[df["LenCup"] == 1]
# res = res.sort_values("Goals", ascending=False).iloc[0, 0]
# print(res)

# # # # 30
# res = df.loc[df["LenCup"] == 1]
# res = res.groupby("Country")["Player"].count(
# ).sort_values(ascending=False).head(1)
# print(res)
# # # # 31
# df = pd.read_csv("../data/seoul_bi.csv")
# df["대여일자"] = pd.to_datetime(df['대여일자'])
# res = df.groupby("대여일자").size().sort_values(ascending=False)
# print(res.head(1))

# # # # 32
# df["day_name"] = df["대여일자"].dt.day_name()
# res = df.groupby("day_name")["이용건수"].sum()
# print(res)

# # # # 33
# res = df.groupby(["day_name", "대여소번호"], as_index=False)["이용건수"].sum()
# res = res.sort_values(["day_name", "이용건수"], ascending=[True, False])
# res = res.groupby("day_name").head(1)
# print(res)

# # # # 34
# res = df.groupby("연령대코드", as_index=False)["대여구분코드"].count()
# res1 = df.loc[df["대여구분코드"].str.contains("일일권")]
# res1 = res1.groupby("연령대코드", as_index=False)["대여구분코드"].count()
# res = pd.merge(res, res1, on="연령대코드", how="inner")
# res['ratio'] = res['대여구분코드_y']/res['대여구분코드_x']
# print(res[['연령대코드', 'ratio']])

# # # # 35
# df.info()
# res = df.groupby("연령대코드")["이동거리"].mean()
# print(res)

# # # # 36
# res = df.loc[df["연령대코드"] == "20대"]
# res = res.loc[res["이동거리"] >= res['이동거리'].mean()]
# res = res.sort_values(["대여일자", "대여소번호"], ascending=[
#                       False, False]).head(200)["탄소량"].astype(float).mean()

# print(round(res, 3))


# # # # 37
# res = df.loc[(df["대여일자"].dt.strftime("%m-%d") == "06-07")
#              & (df['연령대코드'] == '~10대')]
# res = res["이용건수"].median()
# print(res)

# # # # 38
# res = df.loc[(~df["대여일자"].dt.day_name().isin(["Sunday,Saturday"]))
#              & (df["대여시간"].isin([6, 7, 8]))]
# res = res.groupby(["대여시간", "대여소번호"], as_index=False)["이용건수"].sum()
# res = res.sort_values(["대여시간", "이용건수"], ascending=[False, False])
# res = res.groupby("대여시간").head(3)
# print(res)

# # # # 39
# res = df.loc[df["이동거리"] >= df["이동거리"].mean()]
# res = res["이동거리"].std()
# print(res)

# # # # 40
# df["sex"] = df["성별"].apply(lambda x: "남" if x.lower() == 'm' else "여")
# res = df.groupby("sex")["이동거리"].mean()
# print(res)


# # # # 41
# df = pd.read_csv("../data/happiness.csv")
# df.info()
# res = df.loc[df["행복랭킹"] == 10]["점수"].mean()
# print(res)

# # # # 42
# res = df.loc[df["행복랭킹"] <= 50]
# res = res.groupby("년도")["점수"].mean()
# print(res)

# # # # 43
# res = df.loc[df["년도"] == 2018]
# res = res[["점수", '부패에 대한인식']].corr()
# print(res)


# # # # 44
# res = df.groupby(["행복랭킹", "나라명"], as_index=False).size()
# res = res.loc[res['size'] > 1]
# print(len(res))

# # # # 45
# res = df.loc[df["년도"] == 2019]
# encoder = LabelEncoder()
# res["나라명"] = encoder.fit_transform(res['나라명'])
# res = res.corr().unstack().reset_index(name="corr")
# res.columns = ['v1', 'v2', 'corr']
# res = res.loc[res['v1'] != res['v2']]
# res = res.loc[res['v2'] > res['v1']].reset_index(drop=True)
# res = res.sort_values("corr", ascending=False).head(5)
# print(res)

# # # # 46
# res = df.groupby("년도").tail(5)
# res = res.groupby("년도")["점수"].mean()
# print(res)

# # # # 47
# ress = df.loc[df["년도"] == 2019]
# res = ress.loc[ress['상대GDP'] >= ress['상대GDP'].mean()]
# res1 = ress.loc[ress['상대GDP'] <= ress['상대GDP'].mean()]
# res = res["점수"].mean() - res1["점수"].mean()
# print(res)

# # # # 48
# res = df.sort_values(["년도", "부패에 대한인식"], ascending=[
#     True, False]).groupby("년도").head(20).groupby("년도")["부패에 대한인식"].mean()
# print(res)

# # # # 49 ***** merge 적극활용
# res = df.loc[(df["년도"] == 2018) & (df["행복랭킹"] <= 50)]
# res1 = df.loc[(df["년도"] == 2019) & (df["행복랭킹"] >= 50)]
# res = pd.merge(res, res1, on="나라명", how="inner")
# print(len(res))

# # # # 50
# res = df.loc[df["년도"] == 2018][["나라명", '점수']]
# res1 = df.loc[df['년도'] == 2019][["나라명", '점수']]
# res = pd.merge(res, res1, on="나라명", how="inner")
# res['del'] = res['점수_y'] - res['점수_x']
# res = res.sort_values("del", ascending=False)
# print(res.iloc[0, 3])

# # 51
# df = pd.read_csv("../data/Tetuan_City_power_consumption.csv")
# df["DateTime"] = pd.to_datetime(df["DateTime"])
# res = df.groupby(df["DateTime"].dt.month).size()
# print(res)

# # # 52
# res = df.loc[df["DateTime"].dt.month == 3].groupby(
#     df["DateTime"].dt.hour)["Temperature"].mean().sort_values().iloc[0]
# print(res)

# # # 53
# res = df.loc[df["DateTime"].dt.month == 3].groupby(
#     df["DateTime"].dt.hour)["Temperature"].mean().sort_values(ascending=False).iloc[0]
# print(res)

# # # 54
# res = df.loc[df["Zone 1 Power Consumption"] >
#              df["Zone 2 Power Consumption"]]["Humidity"].mean()
# print(res)


# # # 55
# res = df[["Zone 1 Power Consumption", "Zone 2 Power Consumption",
#           "Zone 3 Power Consumption"]].corr()
# print(res)

# # # 56


# def Temp_grade(x):
#     if x >= 30:
#         return "D"
#     elif x >= 20:
#         return "C"
#     elif x >= 10:
#         return "B"
#     else:
#         return "A"


# df["grade"] = df["Temperature"].apply(Temp_grade)
# res = df.groupby("grade").size()
# print(res)

# # # 57
# res = df.loc[(df["DateTime"].dt.month == 6) & (
#     df["DateTime"].dt.hour == 12)]["Temperature"].std()
# print(res)


# # # 58
# res = df.loc[(df["DateTime"].dt.month == 6) & (
#     df["DateTime"].dt.hour == 12)]["Temperature"].var()
# print(res)

# # # 59
# df.info()
# res = df.loc[df["Temperature"] >=
#              df["Temperature"].mean()].sort_values("Temperature").iloc[3, 2]
# print(res)

# # # 60
# df.info()
# res = df.loc[df["Temperature"] >=
#              df["Temperature"].median()].sort_values("Temperature").iloc[3, 2]
# print(res)

# # # 61
# df = pd.read_csv("../data/pokemon.csv")
# df.info()
# res = df.loc[df["Legendary"] == True]["HP"].mean()
# es = df.loc[df["Legendary"] == False]["HP"].mean()
# res = res - es
# print(res)

# # # 62
# res = df.groupby("Type 2").size().sort_values(ascending=False)
# print(res.index[0])

# # # 63
# res = df.groupby("Type 1").size().sort_values(ascending=False)
# print(res.index[0])
# res = df.loc[df["Type 1"] == "Water"]["Attack"].mean()
# res1 = df.loc[df["Type 1"] == "Water"]["Defense"].mean()
# res = res / res1
# print(res)

# # # 64
# res = df.loc[df["Legendary"] == True]
# res = res.groupby("Generation").size().sort_values(ascending=False)
# print(res.index[0])

# # # 65
# res = df[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
#          ].corr().unstack().reset_index(name="corr")

# res = res.loc[res["level_0"] != res["level_1"]]
# res = res.loc[res["level_0"] > res["level_1"]]
# res["corr"] = res["corr"].abs()
# res = res.sort_values("corr", ascending=False)

# print(res.iloc[0])

# # # 66
# res = df.sort_values(["Generation", "Attack"]).groupby(
#     "Generation").head(3)["Attack"].mean()
# print(res)


# # # 67
# res = df.sort_values(["Generation", "Attack"], ascending=False).groupby(
#     "Generation").head(5)["Attack"].mean()
# print(res)

# # # 68
# res = df.groupby(['Type 1', 'Type 2']).size().sort_values(ascending=False)
# print(res.index[0])

# # # 69
# res = df.groupby(['Type 1', 'Type 2'],
#                  as_index=False).size().sort_values("size", ascending=False)
# res = res.loc[res['size'] == 1]
# print(len(res))

# # # 70
# res = df.groupby(['Type 1', 'Type 2'],
#                  as_index=False).size().sort_values("size", ascending=False)
# res = res.loc[res['size'] == 1]
# res1 = df.groupby(["Generation", "Type 1", "Type 2"], as_index=False).size()
# print(res1)
# res = pd.merge(res, res1, on=["Type 1", "Type 2"], how='inner')
# res = res.groupby("Generation").size()
# print(res)

# # # 71
# df = pd.read_csv("../data/body.csv")
# df.info()
# res = df["수축기혈압(최고) : mmHg"] - df["이완기혈압(최저) : mmHg"]
# print(res.mean())

# # # 72
# res = df.loc[df["측정나이"].between(50, 59)]["신장 : cm"].mean()
# print(res)

# # # 73
# df["연령대"] = df["측정나이"].apply(lambda x: (x//10)*10)
# print(df.groupby("연령대").size())

# # # 74
# print(df.groupby(["연령대", "등급"]).size())

# # # 75
# res = df.loc[(df["측정회원성별"] == "M") & (df["등급"] == "A")]["체지방율 : %"].mean()
# res1 = df.loc[(df["측정회원성별"] == "M") & (df["등급"] == "D")]["체지방율 : %"].mean()
# res = res1 - res
# print(res)
# # # 76
# res = df.loc[(df["측정회원성별"] == "F") & (df["등급"] == "A")]["체중 : kg"].mean()
# res1 = df.loc[(df["측정회원성별"] == "F") & (df["등급"] == "D")]["체중 : kg"].mean()
# res = res1 - res
# print(res)

# # # 77
# df["bmi"] = df["체중 : kg"]/(df["신장 : cm"]/100)**2
# res = df.loc[df["측정회원성별"] == "M"]["bmi"].mean()
# print(res)
# # # 78
# res = df.loc[df["bmi"] < df["체지방율 : %"]]["체중 : kg"].mean()
# print(res)

# # # 79
# res = df.loc[(df["측정회원성별"] == "M")]["악력D : kg"].mean()
# res1 = df.loc[(df["측정회원성별"] == "F")]["악력D : kg"].mean()
# res = res - res1
# print(res)

# # # 80
# res = df.loc[(df["측정회원성별"] == "M")]["교차윗몸일으키기 : 회"].mean()
# res1 = df.loc[(df["측정회원성별"] == "F")]["교차윗몸일으키기 : 회"].mean()
# res = res - res1
# print(res)

# # 81
df = pd.read_csv("../data/weather2.csv")
df.info()
df["time"] = pd.to_datetime(df["time"])
res = df.loc[df["time"].dt.month.isin([6, 7, 8])]
res = res.loc[res["이화동기온"] > res["수영동기온"]]
print(len(res))

# # 82
res = df.sort_values("이화동강수", ascending=False)
res = res.iloc[0, 0]
res1 = df.sort_values("수영동강수", ascending=False)
res1 = res1.iloc[0, 0]
print(res, res1)

# # 83
df = pd.read_csv("../data/customerInfo.csv")
df.info()
res = df.loc[df["Gender"] == "Male"].groupby(
    "Geography", as_index=False)["Exited"].sum().sort_values("Exited", ascending=False).iloc[0]
print(res)

# # 84
res = df.loc[(df["IsActiveMember"] == 1) & (
    df["HasCrCard"] == 1)]["Age"].mean()
print("%.4f" % res)

# # 85
res = df.loc[df["Balance"] >= df["Balance"].median()]["CreditScore"].std()
print("%.3f" % res)

# # 86
df = pd.read_csv("../data/adult_health_2018.csv")
df.info()
df["혈압차"] = df["수축기혈압"] - df["이완기혈압"]
res = df.groupby("연령대코드(5세단위)")["혈압차"].var().sort_values(ascending=False)
print(res.index[4])

# # 87
df["비만도"] = df["허리둘레"] / df["신장(5Cm단위)"]
res = df.loc[df["비만도"] >= 0.58].groupby("성별코드").size()
res = res.loc["M"]/res.loc["F"]
print(res)

# # 88
df = pd.read_csv("../data/carInsurance.csv")
df.info()
res = df.loc[df["Vehicle_Age"] == "> 2 Years"]
res = res.loc[res["Annual_Premium"] >=
              df["Annual_Premium"].median()]["Vintage"].mean()
print(res)

# # 89
# res = df.groupby(["Vehicle_Age", "Gender"])["Annual_Premium"].mean()
# res = res.unstack()
res = df.pivot_table(values="Annual_Premium",
                     index="Vehicle_Age", columns="Gender", aggfunc="mean")
print(res)

# # 90
df = pd.read_csv("../data/mobilePhone.csv")
df.info()
res = df.groupby(["price_range", "n_cores"], as_index=False).size()
res = res.sort_values(["price_range", "size"], ascending=[
                      False, False]).drop_duplicates("price_range")
print(res)

# # 91
res = df.loc[df["price_range"] == 3]
res = res.corr().unstack().reset_index(name="corr")
res = res.loc[(res["level_0"] != res["level_1"])
              & (res["level_0"] > res["level_1"])]
res = res.sort_values("corr", ascending=False)
print(res.iloc[1])

# # 92
df = pd.read_csv("../data/airlineSatisfaction.csv")
df.info()
res = df.loc[df["Arrival Delay in Minutes"].isna()]
res = res.groupby(["Class", "satisfaction"]).size().unstack()
res = res.loc[res["satisfied"] > res["neutral or dissatisfied"]]
print(res)

# # 93
df = pd.read_csv("../data/waterPotability.csv")
df.info()
res = df.loc[~df["ph"].isna()]
res = res.loc[res["ph"] <= res["ph"].quantile(0.25)].mean()
print(res["ph"])

# # 94
df = pd.read_csv("../data/medicalCost.csv")
df.info()
smoker = df.loc[df["smoker"] == "yes"]
non_smoker = df.loc[df["smoker"] == "no"]
smoker = smoker.loc[smoker["charges"] >=
                    smoker["charges"].quantile(0.9)]["charges"].mean()
non_smoker = non_smoker.loc[non_smoker["charges"]
                            >= non_smoker["charges"].quantile(0.9)]["charges"].mean()
res = smoker - non_smoker
print(res)

# # 95
df = pd.read_csv("../data/kingcountyPrice.csv")
df.info()
res = df.groupby("bedrooms").size().sort_values(ascending=False)
print(res)
res = df.loc[df["bedrooms"] == 3]
res2 = res["price"].quantile(0.9)
res1 = res["price"].quantile(0.1)
res = res2 - res1
print(res)

# # 96 unsolved
# df = pd.read_csv("../data/admission.csv")
# df.info()

# # 97 unsolved
# df = pd.read_csv("../data/redwine.csv")
# df.info()

# # 98
df = pd.read_csv("../data/drug.csv")
df.info()
df["Age2"] = df["Age"].apply(lambda x: x//10 * 10)
res = df.loc[df["Sex"] == "M"]
res = res.groupby("Age2")["Na_to_K"].mean()
print(res)

# # 99 ******
df = pd.read_csv("../data/audit.csv")
df.info()
res = df.groupby("Risk").mean(numeric_only=True)[["Score_A", "Score_B"]]
print(res)

# # 100 ******
df = pd.read_csv("../data/motion.csv")
df.info()
res = df.groupby("pose").median()
res = (res.iloc[0] - res.iloc[1]).abs()
res = res.sort_values(ascending=False)
print(res)

# # 101
df = pd.read_csv("../data/hyundai.csv")
df.info()
res = df.groupby("model").size().sort_values(ascending=False)
res = res.index[0:3].tolist()
ans = df.loc[df["model"].isin(res)].groupby("model")["price"].mean()
print(ans)

# # 102 *****
df = pd.read_csv("../data/diabetes.csv")
df.info()
res = df.groupby('Outcome').mean().diff().iloc[1, :]
print(res)

# # 103
df = pd.read_csv("../data/NFLX.csv")
df.info()
df["Date"] = pd.to_datetime(df["Date"])
res = df.loc[df["Date"].dt.month == 5]
res = res.groupby(df["Date"].dt.year)["Open"].mean()
print(res)

# # 104
df = pd.read_csv("../data/nba.csv", encoding='latin', sep=';')
df.info()
res = df.loc[df["Tm"] == "TOR"]["Age"].mean()
print("%.4f" % res)

# # 105
res = df.loc[df["Age"] == df["Age"].min()]
res = res.groupby("Pos").size().sort_values(ascending=False).index[0]
print(res)

# # 106
df.info()
df["FirstName"] = df["Player"].apply(lambda x: x.split(" ")[0])
res = df.groupby("FirstName").size().sort_values(ascending=False)
print(res.iloc[0])

# # 107
res = df.groupby("Pos")["PTS"].mean()
print(res)

# # 108 == 107 duplicated

# # 109
res = df.sort_values(["Tm", "G"], ascending=[
                     True, False]).drop_duplicates("Tm", keep="first")["G"].mean()
print(res)

# # 110
res = df.loc[(df["Tm"] == "MIA") & (df["Pos"].isin(["C", "PF"]))]["MP"].mean()
print(res)

# # 111
res = df.loc[df["G"] >= df["G"].mean() * 1.5]["3P"].mean()
print(res)

# # 112
res = df.loc[df["Age"] >= df["Age"].mean()]["G"].mean()
res1 = df.loc[df["Age"] < df["Age"].mean()]["G"].mean()
res = res - res1
print(res)
# # 113
res = df.groupby("Tm")["Age"].mean().sort_values().index[0]
print(res)

# # 114
res = df.groupby("Pos")["MP"].mean()
print(res)
