import pandas as pd
import re

# print ename,sal and sal should be str replace "0" to "*"
# emp = pd.read_csv("data/emp.csv")
# emp["sal"] = emp["sal"].astype(str)
# emp["sal_replace"] = emp["sal"].str.replace("0", "*")
# print(emp[["ename", "sal_replace"]])

# print ename, sal replce 0~3 -> "*"
# emp = pd.read_csv("data/emp.csv")
# emp["sal"] = emp["sal"].astype(str)
# emp["sal_star"] = emp["sal"].apply(lambda x: re.sub("[0-3]", "x", x))
# print(emp[["ename", "sal_star"]])
