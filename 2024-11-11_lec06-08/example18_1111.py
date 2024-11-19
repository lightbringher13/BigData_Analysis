import pandas as pd

# print deptno  and sal_sum per deptno
# emp = pd.read_csv("../data/emp.csv")
# emp = emp.groupby("deptno", as_index=False)["sal"].sum()
# emp = emp.rename(columns={"sal": "sal_sum"})
# print(emp)

# print job and sal sum per job
# emp = pd.read_csv("../data/emp.csv")
# emp = emp.groupby("job", as_index=False)["sal"].sum()
# emp = emp.rename(columns={"sal": "sal_sum"})
# emp = emp.sort_values(by="sal_sum", ascending=False)
# print(emp)

# print job and sal_sum per job ascending order
# emp = pd.read_csv("../data/emp.csv")
# emp = emp.groupby("job", as_index=False)["sal"].sum()
# emp = emp.rename(columns={"sal": "sal_sum"})
# emp = emp.sort_values(by="sal_sum", ascending=False)
# emp = emp[(emp["job"] != "SALESMAN") & (emp["sal_sum"] >= 5000)]
# print(emp)
