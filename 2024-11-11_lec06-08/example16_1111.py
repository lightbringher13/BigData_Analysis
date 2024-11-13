import pandas as pd

# find max age
# emp20 = pd.read_csv("data/emp20.csv", encoding="euckr")
# print(emp20["age"].max())

# find max sal with deptno is 20
# emp = pd.read_csv("data/emp.csv")
# emp.info()
# result = emp[emp["deptno"] == 20]
# print(result)
# print(result["sal"].max())

# find max sal with job is salesman
# emp = pd.read_csv("data/emp.csv")
# print(emp[emp["job"] == "SALESMAN"]['sal'].max())

# find max sal for each job
# emp = pd.read_csv("data/emp.csv")
# print(emp.groupby("job")['sal'].max().reset_index())

# find max fare for each Pclass
# tit = pd.read_csv("data/train.csv")
# print(tit.groupby("Pclass", as_index=False)["Fare"].max())
# print(tit.groupby("Pclass")["Fare"].max().reset_index())

# find max age per telecom and descending order
# emp20 = pd.read_csv("data/emp20.csv", encoding="euckr")
# print(emp20.groupby("telecom", as_index=False)[
#       "age"].max().sort_values(by="age", ascending=False))

# change the column name
# emp20 = pd.read_csv("data/emp20.csv", encoding="euckr")
# result = emp20.groupby("telecom", as_index=False)["age"].max()
# result = result.sort_values(by="age", ascending=False)
# result.columns = ["통신사", "최대나이"]
# result = result.rename(columns={'통신사': "telecom", '최대나이': 'max_age'})
# print(result)
