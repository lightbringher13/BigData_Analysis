import pandas as pd

# let's join the dataframe like sql
# dept = pd.read_csv("../data/dept.csv")
# emp = pd.read_csv("../data/emp.csv")
# result = pd.merge(dept, emp, on="deptno")
# print(result)

# print ename, loc if job is salesman
# emp = pd.read_csv("../data/emp.csv")
# dept = pd.read_csv("../data/dept.csv")
# result = pd.merge(emp, dept, on="deptno")
# result = result[["ename", "loc"]][result["job"] == "SALESMAN"]
# print(result)

# print sal,ename,loc if sal is between (1000,3000)
# emp = pd.read_csv("../data/emp.csv")
# dept = pd.read_csv("../data/dept.csv")
# result = pd.merge(emp, dept, on="deptno")
# result = result[["ename", "loc", "sal"]][result["sal"].between(1000, 3000)]
# print(result)

# print sal,ename,loc if sal is between (1000,3000) and job is salesman
emp = pd.read_csv("../data/emp.csv")
dept = pd.read_csv("../data/dept.csv")
result = pd.merge(emp, dept, on="deptno")
result = result[["ename", "loc", "sal", "job"]][(
    result["sal"].between(1000, 3000)) & (result["job"] == "SALESMAN")]
print(result)
