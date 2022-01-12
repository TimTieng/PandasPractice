import pandas as pd
import numpy as np

orders = pd.read_csv('orders.csv')
print(orders.head(10))

most_expensive = orders.price.max()
print(f"The most expensive shoe is: ${most_expensive}")

num_colors = orders.shoe_color.nunique()
print(f"There are {num_colors} differnt colors")

# GroupBy -- Syntax == df.groupby('column1').column2.measurement()
pricey_shoes = orders.groupby("shoe_type").price.max()
print(pricey_shoes)
print(type(pricey_shoes)) # Series

# Cleaning up . reset_index() syntax == df.groupby('column1').column2.measurement().reset_index()
pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
print(pricey_shoes)
print(type(pricey_shoes)) # DF

# Lambda Functions 
cheap_shoes = orders.groupby("shoe_color").price.apply(lambda x: np.percentile(x,25)).reset_index()
print(cheap_shoes)

# GroupBy multiple columns - groupby([col1, col2])
shoe_counts = orders.groupby(["shoe_type", "shoe_color"])["id"].count().reset_index()
print(shoe_counts)

# pivot tables Syntax 
#  df.pivot(columns='ColumnToPivot',
        #  index='ColumnToBeRows',
        #  values='ColumnToBeValues')

shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()

shoe_counts_pivot = shoe_counts.pivot(
  columns = "shoe_color",
  index = "shoe_type",
  values = "id"
).reset_index()

print(shoe_counts_pivot)

# Review
user_visits = pd.read_csv('page_visits.csv')
print(user_visits.head())

# new DF that shoes how many clicks per advertisement source
click_source = user_visits.groupby("utm_source").id.count().reset_index()
print(click_source)

click_source_by_month = user_visits.groupby(["utm_source", "month"]).id.count().reset_index()
print(click_source_by_month)

click_source_by_month_pivot = click_source_by_month.pivot(
  columns = 'month',
  index = 'utm_source',
  values = 'id'
).reset_index()
print(click_source_by_month_pivot)