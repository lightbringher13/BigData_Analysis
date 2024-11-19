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
result = df.groupby("host_name").size().sort_index(ascending=False)
print(result)
