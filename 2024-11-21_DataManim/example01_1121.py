import datetime
import pandas as pd

# 1
df = pd.read_csv("../data/youtube.csv")
res = df.groupby("channelId").size()
# res = res.reset_index(name="size")
res = res.to_frame().rename(columns={0: "size"})
res = res.sort_values("size", ascending=False)
res = res.head(10)
res = df.loc[df["channelId"].isin(res.index), ["channelTitle"]]
res = res.drop_duplicates("channelTitle", keep="first").reset_index()
print(res["channelTitle"].tolist())

# 2
res = df.loc[df["dislikes"] > df["likes"], ["channelTitle"]
             ].drop_duplicates("channelTitle", keep="first")

print(res["channelTitle"].to_list())

# 3
res = df[["channelId", "channelTitle"]].drop_duplicates()
target = res.groupby("channelId", as_index=False)[
    "channelTitle"].count().sort_values("channelTitle", ascending=False)
target = target[target["channelTitle"] > 1]
print(len(target))

# 4
df["trending_date2"] = pd.to_datetime(df["trending_date2"])
df["week"] = df["trending_date2"].dt.day_name()
res = df.groupby(["week", "categoryId"], as_index=False).size()
res = res.loc[res["week"] == "Sunday"].sort_values("size", ascending=False)
res = res.reset_index(drop=True)
print(res.loc[0, "categoryId"])

# 5
df["trending_date2"] = pd.to_datetime(df["trending_date2"])
df["week"] = df["trending_date2"].dt.day_name()
res = df.groupby(["categoryId", "week"]).size().unstack()
print(res)

# 6
res = df.loc[df["view_count"] > 0, ["title", "comment_count", "view_count"]]
res["hype"] = df["comment_count"]/df["view_count"]
res = res[["title", "hype"]].sort_values("hype", ascending=False)
print(res.iloc[0])

# 7
res = df.loc[df["view_count"] > 0, ["title", "comment_count", "view_count"]]
res["hype"] = df["comment_count"]/df["view_count"]
res = res.loc[res["hype"] > 0]
res = res[["title", "hype"]].sort_values("hype", ascending=True)
print(res.iloc[0])

# 8
res = df.loc[(df["likes"] > 0) & (df["dislikes"] > 0),
             ["title", "likes", "dislikes"]]
res["hate"] = df["dislikes"]/df["likes"]
res = res[["title", "hate"]].sort_values("hate", ascending=True)
print(res.iloc[0, 0])

# 9
res = df.groupby(["channelId", "trending_date2"], as_index=False).size()
res = res.groupby("channelId", as_index=False)[
    "size"].sum().sort_values("size", ascending=False)
res = df.loc[df["channelId"] == res.iloc[0, 0], "channelTitle"].iloc[0]
print(res)

# 10
res = df.groupby(["title", "channelId"],
                 as_index=False).size()
res = res.loc[res["size"] >= 20, "title"]
print(len(res))

# 11
channel = pd.read_csv("../data/channelInfo.csv")
video = pd.read_csv("../data/videoInfo.csv")
print(channel.head())
print(video.head())

video["ct"] = pd.to_datetime(video["ct"])
res = video.groupby("videoname").size()
print(res)

# 12
res = video.sort_values(["videoname", "ct"])
res = res.drop_duplicates("videoname", keep="last")
res = res[["viewcnt", "videoname", "ct"]].reset_index(drop=True)
print(res)

# 13
channel["ct"] = pd.to_datetime(channel["ct"])
res = channel.loc[channel["ct"] >= "2021-10-03"]
res = res.sort_values(["ct", "channelname"])
res = res.drop_duplicates("channelname")
res = res[["channelname", "subcnt"]].reset_index(drop=True)
print(res)

# 14
end = channel.loc[channel.ct.dt.strftime('%Y-%m-%d %H') == '2021-11-01 15']
start = channel.loc[channel.ct.dt.strftime('%Y-%m-%d %H') == '2021-10-03 03']

end_df = end[['channelname', 'subcnt']].reset_index(drop=True)
start_df = start[['channelname', 'subcnt']].reset_index(drop=True)

end_df.columns = ['channelname', 'end_sub']
start_df.columns = ['channelname', 'start_sub']


tt = pd.merge(start_df, end_df)
tt['del'] = tt['end_sub'] - tt['start_sub']
result = tt[['channelname', 'del']]
print(result)

# 15 2024-11-22
res = video.loc[video["videoname"].str.contains(
    "1")].sort_values("ct").reset_index(drop=True)
res = res.loc[(res["ct"].diff() >= datetime.timedelta(minutes=20)) | (
    res["ct"].diff() <= datetime.timedelta(minutes=5))]

print(res)

# 16
video["date"] = video["ct"].dt.date
res = video[["date", "videoname"]].sort_values(
    ["date", "videoname"]).drop_duplicates("videoname")

print(res)

# 17
res = video.loc[video["ct"].dt.hour == 21]
res = res.sort_values(["ct", "videoname"])
res = res.drop_duplicates("videoname")
res = res[["viewcnt", "ct", "videoname"]
          ].sort_values("viewcnt", ascending=False).reset_index(drop=True)
print(res)

# 18
res = video.sort_values("ct").drop_duplicates("videoname", keep="last")
res["ratio"] = res["dislikecnt"]/res["likecnt"]
res = res[["videoname", "ratio"]].sort_values("ratio")
res = res.reset_index(drop=True)
print(res)

# 18
res = video.loc[(video["ct"] >= "2021-11-01 00:00:00") &
                (video["ct"] <= "2021-11-01 15:00:00"), ["videoname", "viewcnt", "ct"]]

res = res.groupby("videoname")["viewcnt"].agg(["min", "max"]).reset_index()
res["increse"] = res["max"] - res["min"]
res = res[["videoname", "increse"]]
print(res)

# 20
res = video.loc[video.duplicated()]
res = res[["videoname", "ct"]]
print(res)

# 21
wcg = pd.read_csv("../data/worldcupgoals.csv")
res = wcg.groupby("Country")["Goals"].sum(
).reset_index().sort_values("Goals", ascending=False)
res = res.head()
print(res)

# 22
res = wcg.groupby("Country", as_index=False)["Player"].count(
).sort_values("Player", ascending=False).head()
print(res)

# 23


def check(x):
    for val in x:
        if len(val) != 4:
            return False
    return True


wcg["yearlst"] = wcg["Years"].str.split("-")
wcg["check"] = wcg["yearlst"].apply(check)
res = wcg.loc[wcg["check"] == False]
print(len(res))

# 24
df2 = wcg.loc[wcg["check"] == True]
print(len(df2))

# 25


def lencup(x):
    val = x.split("-")
    return (len(val))


df2["lencup"] = df2["Years"].apply(lencup)
res = df2.loc[df2["lencup"] == 4, "Player"]
print(len(res))

# 26
res = df2.loc[(df2["Country"] == "Yugoslavia") & (df2["lencup"] == 2)]
print(len(res))

# 27
res = len(df2.loc[df2["Years"].str.contains("2002")])
print(res)

# 28
res = len(df2.loc[df2["Player"].str.lower().str.contains("carlos")])
print(res)

# 29
res = df2.loc[df2["lencup"] == 1, ["Player", "Goals"]]
res = res.sort_values("Goals", ascending=False).iloc[0, 0]
print(res)

# 30
res = df2.loc[df2["lencup"] == 1]
res = res.groupby("Country", as_index=False).size(
).sort_values("size", ascending=False)
print(res.iloc[0, 0])

# 31
df = pd.read_csv("../data/seoul_bi.csv")
res = df.groupby("대여일자", as_index=False).size()
res = res.sort_values("size", ascending=False)
print(res.iloc[0, 0])

# 32
df["대여일자"] = pd.to_datetime(df["대여일자"])
df["day_name"] = df["대여일자"].dt.day_name()
res = df.groupby("day_name", as_index=False).size(
).sort_values("day_name", ascending=False)
print(res)

# 33
res = df.groupby(["day_name", "대여소번호"], as_index=False).size(
).sort_values(["day_name", "size"], ascending=[False, False])
res = res.drop_duplicates("day_name")
print(res)

# 34
res = df.loc[df["대여구분코드"].str.contains("일일권")].groupby(
    "연령대코드", as_index=False).size()
res1 = df.groupby("연령대코드", as_index=False)["대여구분코드"].size()
res["del"] = res["size"]/res1["size"]
print(res.sort_values("del", ascending=False))

# 35
res = df.groupby("연령대코드")["이동거리"].mean()
print(res)

# 36
res = df.loc[df["연령대코드"] == "20대"]
res = res.loc[res["이동거리"] >= res["이동거리"].mean()]
res = res.sort_values(["대여일자", "대여소번호"], ascending=[False, False]).head(200)
res["탄소량"] = res["탄소량"].astype(float)
answer = res["탄소량"].mean()
print("% .3f" % answer)

# 37
res = df.loc[(df.연령대코드 == '~10대') & (
    df.대여일자 == pd.to_datetime('2021-06-07'))]["이용건수"].median()
print(res)

# 38
res = df.loc[(~df["day_name"].isin(["Sunday", "Saturday"]))
             & (df["대여시간"].isin([6, 7, 8]))]

res = res.groupby(["대여시간", "대여소번호"]).size().reset_index(
    name="이용횟수")
res = res.sort_values(["대여시간", "이용횟수"], ascending=False)
res = res.groupby("대여시간").head(3).reset_index(drop=True)
print(res)

# 39
res = df.loc[df["이동거리"] >= df["이동거리"].mean()]
res = res["이동거리"].std()
print(res)

# 40
df["sex"] = df["성별"].str.lower().apply(lambda x: "남"if x == "m" else "여")
res = df.groupby("sex")["이동거리"].mean()
print(res)

# 41
df = pd.read_csv("../data/happiness.csv")
df.info()
res = df.loc[(df["년도"].isin([2019, 2018])) & (df["행복랭킹"] == 10)]["점수"].mean()
print(res)

# 42
res = df.loc[df["행복랭킹"] <= 50]
res = res.groupby("년도")["점수"].mean()
print(res)

# 43
