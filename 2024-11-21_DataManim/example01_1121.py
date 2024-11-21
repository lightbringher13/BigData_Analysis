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

end_df = end[["channelname", "subcnt"]]
start_df = start[["channelname", "subcnt"]]

end_df = end_df.rename(columns={"subcnt": "end_sub"})
start_df = start_df.rename(columns={"subcnt": "start_sub"})

total = pd.merge(start_df, end_df, on="channelname", how="inner")

total["del"] = total["end_sub"] - total["start_sub"]
total = total[["channelname", "del"]]
print(total)

# 15
