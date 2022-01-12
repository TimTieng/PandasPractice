import pandas as pd

# Example - use a dictionary with existing data to create a DataFrame

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  # add Product Name and Color here
  'Product Name': ["t-shirt", "t-shirt", "skirt", "skirt"],
  'Color': ["blue","green","red", "black"]
})

print(df1)

# Example 2 - use a list with existing data to create a dataframe
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
  columns=[
    #add column names here
    'Store ID', 'Location', 'Number of Employees'
  ])

print(df2)

# Read a csv file syntax = <dfObject = pandas library.read_csv("<csvfilename>")

# Select specific coloumns in a df
#< dfObject  = df.<columnname> OR df['columnname']
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)
clinic_north = df.clinic_north
print(type(clinic_north))

# Selecting multiple columns -- Note the double Brackets!
clinic_north_south = df[["clinic_north", "clinic_south"]]

# Selecting Rows and Multiple Rows (slicing)
march = df.iloc[2]
print(march)

april_may_june = df.iloc[-3:]
print(april_may_june)

# Selecting Rows using Logic 
january = df[df.month == "January"]
print(january)

# Selecting rows with compound conditional statements
march_april = df[(df.month == "March") | (df.month == "April")]
print(march_april)

# Selecting rows using built-in methods in pandas
january_february_march = df[df.month.isin(["January","February","March"])]
print(january_february_march)

# Setting Indices -- Typically used for non-consecutive indices -- .reset_index()
# Use inplace = True to modify existing DF
# use drop = True to create new DF with new indices
df2 = df.loc[[1, 3, 5]]
# print(df2)

df2.reset_index(inplace = True,drop = True)
print(df2)
