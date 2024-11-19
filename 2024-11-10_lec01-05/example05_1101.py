import pandas as pd

# sort the collumn values in sal ascending order
# emp = pd.read_csv("data/emp.csv")
# print(emp[["ename", "sal"]].sort_values(by="sal", ascending=True))

# print ename and sal if job is salesman and ascending sal order
# emp = pd.read_csv("data/emp.csv")
# print(emp[["ename", "sal", "job"]][emp["job"] ==
#       "SALESMAN"].sort_values(by="sal", ascending=True))

# print telecom and age and name if not kt in age descending order
emp20 = pd.read_csv("data/emp20.csv", encoding="euckr")
print(emp20[["ename", "age", "telecom"]]
      [emp20["telecom"] != "kt"].sort_values(by="age", ascending=True))

result = emp20[["ename", 'age', 'telecom']][emp20['telecom'] != "kt"]
result.sort_values(by="age", ascending=True)
print(result)
