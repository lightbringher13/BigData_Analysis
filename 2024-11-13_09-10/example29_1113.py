import pandas as pd

# union all ename,deptno,sal deptno 10 or 20 + dept 10
# emp = pd.read_csv("../data/emp.csv")
# x1 = emp[["ename", "sal", "deptno"]][emp["deptno"].isin([10, 20])]
# x2 = emp[["ename", "sal", "deptno"]][emp["deptno"] == 10]
# result = pd.concat([x1, x2], axis=1)
# print(result)

# union all ename,age,telecom telecom kt or lg + telecom sk or lg
# emp20 = pd.read_csv("../data/emp20.csv", encoding="euckr")
# x1 = emp20[["ename", "age", "telecom"]][emp20["telecom"].isin(["kt", "lg"])]
# x2 = emp20[["ename", "age", "telecom"]][emp20["telecom"].isin(["sk", "lg"])]
# result = pd.concat([x1, x2], axis=0)
# print(result)

# union drop duplicates ename,age,telecom telecom kt or lg + telecom sk or lg
# emp20 = pd.read_csv("../data/emp20.csv", encoding="euckr")
# x1 = emp20[["ename", "age", "telecom"]][emp20["telecom"].isin(["kt", "lg"])]
# x2 = emp20[["ename", "age", "telecom"]][emp20["telecom"].isin(["sk", "lg"])]
# result = pd.concat([x1, x2], axis=0)
# result = result.drop_duplicates()
# print(result)

# minus emp - emp_old_backup ename,sal,deptno
# emp = pd.read_csv("../data/emp.csv")
# emp_old_backup = pd.read_csv("../data/emp_old_backup.csv")
# result = emp[["ename", "sal", "deptno"]
#              ][~emp["ename"].isin(emp_old_backup["ename"])]
# print(result)

# minus emp20 kt or lg - emp20 lg or sk ename,age,telecom
# emp20 = pd.read_csv("../data/emp20.csv", encoding="euckr")
# x1 = emp20[["ename", "age", "telecom"]][emp20["telecom"].isin(["kt", "lg"])]
# x2 = emp20[["ename", "age", "telecom"]][emp20["telecom"].isin(["lg", "sk"])]
# result = x1[~x1["telecom"].isin(x2["telecom"])]
# print(result)

# intersect emp and emp_old_backup
# emp = pd.read_csv("../data/emp.csv")
# emp_old_backup = pd.read_csv("../data/emp_old_backup.csv")
# x1 = emp[["ename", "sal", "deptno"]]
# x2 = emp_old_backup[["ename", "sal", "deptno"]]
# result = x1[x1["ename"].isin(x2["ename"])]
# print(result)
