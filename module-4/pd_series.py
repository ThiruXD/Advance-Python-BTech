import pandas as pd

marks = pd.Series([78, 85, 92, 66], index=["Amit", "Ravi", "Neha", "Sara"])
print(marks)
print(marks["Neha"])