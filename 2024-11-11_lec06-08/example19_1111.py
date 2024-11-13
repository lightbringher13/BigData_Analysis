import pandas as pd

# print mean
# emp = pd.read_csv("../data/emp.csv")
# print(emp["sal"].mean())

# pirnt year from date
# emp = pd.read_csv("../data/emp.csv")
# emp["hiredate"] = pd.to_datetime(emp["hiredate"])
# emp["hiredate"] = emp["hiredate"].dt.year
# print(emp['hiredate'])

# add year series from date
# emp = pd.read_csv("../data/emp.csv")
# emp["hiredate"] = pd.to_datetime(emp["hiredate"])
# emp["hire_year"] = emp["hiredate"].dt.year
# print(emp)

# add 'hire_year" series and mean_sal per year
# emp = pd.read_csv("../data/emp.csv")
# emp["hiredate"] = pd.to_datetime(emp["hiredate"])
# emp['hire_year'] = emp["hiredate"].dt.year
# emp = emp.groupby("hire_year", as_index=False)["sal"].mean()
# emp = emp.rename(columns={"sal": "sal_mean"})
# print(emp)

# add 'hire_year" series and mean_sal per year ascending order
# emp = pd.read_csv("../data/emp.csv")
# emp["hiredate"] = pd.to_datetime(emp["hiredate"])
# emp['hire_year'] = emp["hiredate"].dt.year
# emp = emp.groupby("hire_year", as_index=False)["sal"].mean()
# emp = emp.rename(columns={"sal": "sal_mean"})
# emp = emp.sort_values(by="sal_mean", ascending=False)
# print(emp)
