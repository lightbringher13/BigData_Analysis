import pandas as pd

# pivot sal_sum of each deptno
# emp = pd.read_csv("../data/emp.csv")
# result = emp.pivot_table(values="sal",
#                          columns="deptno", aggfunc="sum")
# print(result)

# pivot sum of sal per job
# emp = pd.read_csv("../data/emp.csv")
# result = emp.pivot_table(values="sal", columns="job", aggfunc="sum")
# print(result)

# pivot job,deptno and sal_sum per job,deptno
# emp = pd.read_csv("../data/emp.csv")
# result = emp.pivot_table(values="sal", index="job",
#                          columns="deptno", aggfunc="sum")
# print(result)

# add "addree_front_3" series
# emp20 = pd.read_csv("../data/emp20.csv", encoding="euckr")
# emp20["address_front_3"] = emp20["address"].str.slice(start=0, stop=3)
# emp20["address_front_3"] = emp20["address"].apply(lambda x: x[0:3])
# print(emp20["address_front_3"])

# add "addree_front_3" series and pivot table address_front_3 man count
emp20 = pd.read_csv("../data/emp20.csv", encoding="euckr")
emp20["address_front_3"] = emp20["address"].str.slice(start=0, stop=3)
result = emp20.pivot_table(
    values="empno", columns="address_front_3", aggfunc="count")
print(result)
