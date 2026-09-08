import pandas as pd

data = {
    "Name": ["Amit", "Ravi", "Neha", "Sara"],
    "Age": [21, 22, 20, 23],
    "Marks": [78, 85, 92, 66]
}

df = pd.DataFrame(data)

# # insert one column inside exisiting table
# df["Grade"] = ["A", "A+", "B", "A+"]
# print(df)

# # To calculate average, max, min from marks
# avg = df["Marks"].mean()
# max = df["Marks"].max()
# min = df["Marks"].min()
# print(f"\nAverage Marks: {avg} \nMaximum Marks: {max} \nMinimum Marks: {min}")

# # To sort based on grater/lesser than numbers
# gt = df[df["Marks"] > 80]
# print(f"\n{gt}")

# 
sort = df.sort_values("Marks", ascending=False)
print(sort)

# # Select one column
# print(df["Name"])

# # Select multiple columns
# print(df[["Name", "Marks"]])

# # Select rows using label-based indexing
# print(df.loc[0])

# # Select rows using integer position
# print(df.iloc[0:2])
