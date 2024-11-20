import pandas as pd

# getting and knowing
df = pd.read_csv("../data/emp.csv")
# 1. print top 5 rows
print(df.head(5))

# 2. print rows and columns
print(df.shape)
print(f"rows: {df.shape[0]}")
print(f"columns: {df.shape[1]}")

# 3. print all columns
print(f"all columns: {df.columns}")

# 4. print third column
print(df.columns[2])

# 5. print third column type iloc[rows,columns]
print(df.iloc[:, 2].dtype)

# 6. print index
print(df.index)

# 7. print third value of the sixth column
print(df.iloc[2, 5])

# 8. load data data is korean
df = pd.read_csv("../data/emp20.csv", encoding="euckr")

# 9. print last 3 rows
print(df.tail(3))

# 10. select only numeric data type
print(df.select_dtypes(exclude="object").columns)

# 11. select only categorical data type
print(df.select_dtypes(include="category").columns)

# 12. print null numbers
print(df.isnull().sum())

# 13. print data num, and dtype
df.info()

# 14. print quartiles, mean, stadard deviation, maximum, minimum
print(df.describe())

# 15. print empno
print(df["empno"])

# 16. print IQR(Q3 - Q1) and used for outlier Q1-1.5IQR,Q3+1.5IQR
df = pd.read_csv("../data/Jeju.csv", encoding="euckr")
IQR = df["평균 속도"].quantile(0.75) - df["평균 속도"].quantile(0.25)
print(IQR)

# 17. print 읍면동명 columns unique val count
print(df["읍면동명"].nunique())

# 18. print 읍면동명 coumns unique val
print(df["읍면동명"].unique())

# -----------------------------------------------------------------------------
# filtering and sorting

# 19. load data
df = pd.read_csv("../data/chipo.csv")

# 20. print first 5 rows if quantitiy is 3
result = df.loc[df["quantity"] == 3]
print(result.head())

# 21. print first 5 rows if quantitiy is 3 start from index 0
result = df.loc[df["quantity"] == 3]
result = result.reset_index(drop=True)
print(result.head())

# 22 print new_df column quantity, item_price
result = df.loc[:, ["quantity", "item_price"]]

# 23 item_price no dollar mark and float type new_price
df["new_price"] = df["item_price"].str.replace("$", "").astype(float)


# 24 count new_price val <= 5
result = len(df.loc[df["new_price"] <= 5])

# 25 print item_name is Chicken Salad Bowl and reset index
result = df.loc[df["item_name"] == "Chicken Salad Bowl"]
result = result.reset_index(drop=True)

# 26 print item_name is Chicken Salad Bowl and new_price <= 9
result = df.loc[(df["item_name"] == "Chicken Salad Bowl")
                & (df["new_price"] <= 9)]

# 27 sort by new_price and reset index
result = df.sort_values(by="new_price", ascending=True).reset_index(drop=True)
print(df)

# 28 print df if item_name includes chips
result = df.loc[df["item_name"].str.contains("Chips")]

# 29 print only the even num column
result = df.iloc[:, 0::2]
print(result)

# 30 new_price sort descending order and reset index
result = df.sort_values(
    by="new_price", ascending=False).reset_index(drop=True)
print(result)

# 31 print item_name isin Steak Salad or Bowl
result = df.loc[df["item_name"].isin(["Steak Salad", "Bowl"])]

# 32 print item_name isin Steak Salad or Bowl drop_duplicates keep first
result = df.loc[df["item_name"].isin(["Steak Salad", "Bowl"])]
result = result.drop_duplicates(subset="item_name", keep="first")

# 33 print item_name isin Steak Salad or Bowl drop_duplicates keep last
result = df[df["item_name"].isin(["Steak Salad", "Bowl"])]
result = result.drop_duplicates(subset="item_name", keep="last")
print(result)

# 34 print df if new_price > new_price avg
result = df.loc[df["new_price"] >= df["new_price"].mean()]

# 35 replace item_name Izze to Fizzy Lizzy
result = df.loc[df["item_name"] == "Izze", "item_name"] = "Fizzy Lizzy"

# 36 count choice_description is NaN
result = df["choice_description"].isnull().sum()

# 37 fill NaN in choide_description use loc
result = df.loc[df["choice_description"].isnull(),
                "choice_description"] = "NoData"

# 38 print df if choice_description contains Black
result = df.loc[df["choice_description"].str.contains("Blakc")]

# 39 print df if choice_description does not contain Vegetables
result = len(df.loc[~df["choice_description"].str.contains("Vegetables")])

# 40 print df if item_name starts with N
result = df.loc[df["item_name"].str.startswith("N")]

# 41 print df if len of item_name is over 15
result = df.loc[df["item_name"].str.len() >= 15]

# 42 print df if new_price is in the lst value
lst = [1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
result = df.loc[df["new_price"].isin(lst)]

# ----------------------------------------------------------------------------------------------------------------
# Grouping

# 43 load the data and print df top 5 rows
df = pd.read_csv("../data/AB_NYC_2019.csv")
print(df.head())

# 44 pirnt host_name frequency and sort by host_name
result = df.groupby("host_name").size().sort_index()
print(result)

# 45 print host_name frequency and sort by descending order and name the column counts
result = df.groupby("host_name").size().reset_index(name="count")
result = result.sort_values("count", ascending=False)
print(result)

# 46 groupby neighborhood_group and neighborhood
result = df.groupby(["neighbourhood_group", "neighbourhood"]
                    ).size().to_frame().rename(columns={0: "size"})
print(result)

# 47 groupby neighborhood_group and neighborhood find max
result = df.groupby(
    ["neighbourhood_group", "neighbourhood"], as_index=False).size()
result = result.groupby("neighbourhood_group").max()
print(result)

# 48 groupby neighbourhood_group and price avg,deviation,max,min
result = df[['neighbourhood_group', 'price']].groupby(
    'neighbourhood_group').agg(['mean', 'var', 'max', 'min'])
print(result)

# 49 groupby neighbourhood_group, reviews_per_month mean,var,min,max
res = df[["neighbourhood_group", "reviews_per_month"]
         ].groupby("neighbourhood_group").agg(["mean", 'var', 'min', 'max'])
print(res)

# 50 groupby neighbourhood, neibourhood_group and price_mean
res = df.groupby(["neighbourhood_group", "neighbourhood"])["price"].mean()
print(res)

# 51 groupby neighbourhood, neibourhood_group and price_mean without hierarchical indexing
res = df.groupby(["neighbourhood", "neighbourhood_group"])[
    "price"].mean().unstack()
print(res)

# 52 groupby neighbourhood, neibourhood_group and price_mean without hierarchical indexing and fill na -999
res = df.groupby(["neighbourhood", "neighbourhood_group"])[
    "price"].mean().unstack()
res = res.fillna(-999)
print(res)

# 53 neighbourhood_group is Queens and groupby neighbourhood and price mean, var,min,max
res = df.loc[df["neighbourhood_group"] == "Queens"]
res = res.groupby("neighbourhood")["price"].agg(["mean", "var", "min", "max"])
print(res)

# 54 very hard
Ans = df[['neighbourhood_group', 'room_type']].groupby(
    ['neighbourhood_group', 'room_type']).size().unstack()
Ans.loc[:, :] = (Ans.values / Ans.sum(axis=1).values.reshape(-1, 1))

# 56 load the data and rows and columns
df = pd.read_csv("../data/BankChurnersUp.csv")
print(df.shape)

# 58 use Income_catergory to make newIncome use map
dic = {
    'Unknown': 'N',
    'Less than $40K': 'a',
    '$40K - $60K': 'b',
    '$60K - $80K': 'c',
    '$80K - $120K': 'd',
    '$120K +': 'e'
}
df["newIncome"] = df["Income_Category"].map(lambda x: dic[x])

# 59 use Income_catergory to make newIncome use apply
df["newIncome"] = df["Income_Category"].apply(lambda x: dic[x])

# 60 make AgeState customer_Age frequency
df["AgeState"] = df["Customer_Age"].apply(lambda x: x//10 * 10)
res = df.groupby("AgeState").size().sort_index()
print(res)

# 61 Education_Level contains Graduate 1 or 0 newEduLevel and frequency
df["newEduLevel"] = df["Education_Level"].apply(
    lambda x: 1 if "Graduate" in x else 0)
res = df.groupby("newEduLevel").size()
print(res)

# 62 Credit_Limit over 4500 1 or 0 -> newLimit and frequency
df["newLimit"] = df["Credit_Limit"].apply(lambda x: 1 if x >= 4500 else 0)
res = df.groupby("newLimit").size()
print(res)

# 63
df["newState"] = df[["Marital_Status", "Card_Category"]].apply(
    lambda x: 1 if x.iloc[0] == "Married" and x.iloc[1] == "Platinum" else 0, axis=1)
res = df.groupby("newState").size()
print(res)

# 64
df["Gender"] = df["Gender"].apply(lambda x: "male" if x == "M" else "female")
res = df.groupby("Gender").size()
print(res)


# -----------------------------------------------------------------------------
# Time Series

# 65
df = pd.read_csv("../data/timeTest.csv")
df.info()

# 66
df["Yr_Mo_Dy"] = pd.to_datetime(df["Yr_Mo_Dy"])
print(df["Yr_Mo_Dy"])
df.info()

# 67
res = df['Yr_Mo_Dy'].dt.year
res = res.unique()
print(res)

# 68
df["Yr_Mo_Dy"] = df["Yr_Mo_Dy"].apply(
    lambda x: x.replace(year=x.year - 100) if x.year >= 2061 else x)
print(df["Yr_Mo_Dy"])

# 69
res = df.groupby(df["Yr_Mo_Dy"].dt.year).agg("mean")
print(res)

# 70
df["weekday"] = df["Yr_Mo_Dy"].dt.weekday
print(df["weekday"])

# 71
df["WeekCheck"] = df["weekday"].apply(lambda x: 1 if x > 4 else 0)
print(df["WeekCheck"])

# 72
res = df.groupby(df.Yr_Mo_Dy.dt.month).mean()
print(res)

# 73
df = df.fillna(method="ffill").fillna(method="bfill")
print(df.isnull().sum())

# 74
res = df.groupby(df["Yr_Mo_Dy"].dt.to_period("M")).mean()
print(res)

# 75
res = df["RPT"].diff()
result = pd.concat([res, df["RPT"]], axis=1)
print(result)

# 76
res = df[["RPT", "VAL"]].rolling(7).mean()
print(res.head(10))

# 76
# def change_date(x):
#     import datetime
#     hour = x.split(':')[1]
#     date = x.split(":")[0]

#     if hour == '24':
#         hour = '00:00:00'

#         FinalDate = pd.to_datetime(date + " "+hour) + \
#             datetime.timedelta(days=1)

#     else:
#         hour = hour + ':00:00'
#         FinalDate = pd.to_datetime(date + " "+hour)

#     return FinalDate


# df['(년-월-일:시)'] = df['(년-월-일:시)'].apply(change_date)

# res = df

# 77
# df['dayName'] = df['(년-월-일:시)'].dt.day_name()
# res = df['dayName']

# 78
# Ans1 = df.groupby(['dayName', 'PM10등급'], as_index=False).size()
# Ans2 = Ans1.pivot(index='dayName', columns='PM10등급', values='size').fillna(0)

# 79
# 시간을 차분했을 경우 첫 값은 nan, 이후 모든 차분값이 동일하면 연속이라 판단한다.
# check = len(df['(년-월-일:시)'].diff().unique())
# if check == 2:
#     Ans = True
# else:
#     Ans = False

# 80
# res = df.groupby(df['(년-월-일:시)'].dt.hour)['PM10'].mean().loc[[10, 22]]

# 81
# df.set_index('(년-월-일:시)', inplace=True, drop=True)

# 82
# df['week'] = df.index.to_period('W')
# Ans = df.groupby('week').agg(['min', 'max', 'mean', 'std'])

# -----------------------------------------------------------------------------
# pivot

# 83
df = pd.read_csv("../data/under5MortalityRate.csv")
df = df.drop("Indicator", axis=1)
df["First Tooltip"] = df["First Tooltip"].apply(
    lambda x: float(x.split("[")[0]))
print(df.head(5))
df.info()

# 84
df = df.loc[(df["Period"] >= 2015) & (df["Dim1"] == "Both sexes")]
print(df)

# 85
res = df.pivot(index="Location", columns="Period", values="First Tooltip")
print(res)

# 86
res = df.pivot_table(values="First Tooltip", index="Dim1",
                     columns="Period", aggfunc="mean")
print(res.head(5))

# 87
df = pd.read_csv("../data/winter.csv")
res = df.loc[df["Country"] == "KOR"]
print(res)

# 88
res = df.pivot_table(index="Year",
                     columns="Medal", aggfunc="size").fillna(0)
print(res)

# 89
res = df.pivot_table(index="Sport", columns="Gender", aggfunc="size").fillna(0)
print(res)

# 90
res = df.pivot_table(index="Discipline", columns="Medal",
                     aggfunc="size").fillna(0)
print(res)

# -----------------------------------------------------------------------------
# Merge, Concat

# 91
df = pd.read_csv("../data/mergeTest.csv")

df1 = df.iloc[:4, :]
df2 = df.iloc[4:, :]
total = pd.concat([df1, df2])
print(total)

# 92
df3 = df.iloc[:2, :4]
df4 = df.iloc[:5, 3:]
res = pd.concat([df3, df4], join="inner")
print(res)

# 93
df3 = df.iloc[:2, :4]
df4 = df.iloc[5:, 3:]
res = pd.concat([df3, df4], join="outer").fillna(0)
print(res)

# 94
df5 = df.T.iloc[:7, :3]
df6 = df.T.iloc[6:, 2:5]
Ans = pd.merge(df5, df6, on='Algeria', how='inner')

# 95
Ans = pd.merge(df5, df6, on='Algeria', how='outer')
