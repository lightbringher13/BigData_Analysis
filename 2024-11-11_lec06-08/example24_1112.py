import pandas as pd

# print grouped data in list
# emp = pd.read_csv("../data/emp.csv")
# result = emp.groupby("deptno", as_index=False)['ename'].apply(list)
# print(result)

# print telecom grouped ename in list
emp20 = pd.read_csv("../data/emp20.csv", encoding="euckr")
result = emp20.groupby("telecom", as_index=False)["ename"].apply(list)
print(result)

# print telecom single series into list
emp20 = pd.read_csv("../data/emp20.csv", encoding="euckr")
print(emp20["ename"].to_list())
