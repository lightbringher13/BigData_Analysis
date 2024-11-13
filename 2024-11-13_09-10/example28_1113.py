import pandas as pd

# right join print all deptno
# emp = pd.read_csv("../data/emp.csv")
# dept = pd.read_csv("../data/dept.csv")
# result = pd.merge(emp, dept, on="deptno", how="right")
# print(result[["ename", "loc"]])

# left join print all deptno
# emp = pd.read_csv("../data/emp.csv")
# dept = pd.read_csv("../data/dept.csv")
# result = pd.merge(emp, dept, on="deptno", how="lef")
# print(result[["ename", "loc"]])

# outer join print all deptno
# emp = pd.read_csv("../data/emp.csv")
# dept = pd.read_csv("../data/dept.csv")
# result = pd.merge(emp, dept, on="deptno", how="outer")
# print(result[["ename", "loc"]])

# print dept_loc_sum grouped by loc
# emp = pd.read_csv("../data/emp.csv")
# dept = pd.read_csv('../data/dept.csv')
# result = pd.merge(emp, dept, on="deptno")
# result = result.groupby("loc", as_index=False)["sal"].sum()
# print(result)
# result = result.pivot_table(values="sal", columns="loc", aggfunc="sum")
# print(result)

# print dept_dname_mean grouped by dname
# emp = pd.read_csv("../data/emp.csv")
# dept = pd.read_csv('../data/dept.csv')
# result = pd.merge(emp, dept, on="deptno")
# result = result.groupby("dname", as_index=False)["sal"].mean()
# print(result)
# result = result.pivot_table(values="sal", columns="dname", aggfunc="mean")
# print(result)
