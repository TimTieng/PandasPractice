import pandas as pd

df = pd.DataFrame([
    [1, "3 inch screw", 0.5, 0.75],
    [2, "2 inch nail", 0.10, 0.25],
    [3, "hammer", 3.00, 5.50],
    [4, "screwdriver", 2.50, 3.00]
],
    columns=["Product ID", "Description", "Cost To Manufacture", "Price"]
)
# print(df)

# Add a column to an existing df -> df["<newColumnName>"] = [Column Values....]
df["Sold In Bulk?"] = ["Yes", "Yes", "No", "No"]

# Add a column and set all the values to be the same
df["Is taxed?"] = "Yes"

# Add a column and perform a function to set the values of the new  column
df["Margin"] = df['Price'] - df["Cost To Manufacture"]

# Formatting column values - Lower/Upper Case
df["Uppercase Descrption"] = df.Description.apply(str.upper)

# Apply lambda functions to modify a column
df1 = pd.read_csv('employees.csv')
get_last_name = lambda name: name.split(" ")[-1]
df["last_name"] = df.name.apply(get_last_name)
print(df)

