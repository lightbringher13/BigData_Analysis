import pandas as pd

# find min sal per job
# emp = pd.read_csv("data/emp.csv")
# result = emp.groupby("job", as_index=False)["sal"].min()
# result = result.rename(columns={"job": "직업", "sal": "직업별최소월급"})
# print(result)

# print job and min sal per job by ascending order
# emp = pd.read_csv("data/emp.csv")
# result = emp.groupby("job", as_index=False)["sal"].min()
# result = result.rename(columns={"job": "직업", "sal": "직업별최소금액"})
# result = result.sort_values(by="직업별최소금액", ascending=True)
# print(result)

# print job and min sal per job by ascending order if min >= 1200
# emp = pd.read_csv("data/emp.csv")
# result = emp.groupby("job", as_index=False)["sal"].min()
# result = result.rename(columns={"job": "직업", "sal": "직업별최소금액"})
# result = result.sort_values(by="직업별최소금액", ascending=True)
# result = result[result["직업별최소금액"] >= 1200]
# print(result)
