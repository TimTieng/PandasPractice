import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
# print(ad_clicks.head())

adPlatformCount = ad_clicks.groupby("utm_source").user_id.count().reset_index()
print(adPlatformCount)


ad_clicks["is_click"] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks)

clicks_by_source = ad_clicks.groupby(["utm_source", "is_click"]).user_id.count().reset_index()
print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(
  columns = "is_click",
  index = "utm_source",
  values = "user_id"
).reset_index()

clicks_pivot["percent_clicked"] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot)

ABCount = ad_clicks.groupby("experimental_group").user_id.count().reset_index()
print(ABCount)

# ~ symbol is NOT
ABCount["is_clicked"] = ~ad_clicks.ad_click_timestamp.isnull()
print(ABCount)
clicks_by_group = ad_clicks.groupby(["experimental_group", "is_click"]).user_id.count().reset_index()
print(clicks_by_group)

clickByGroupPivot = clicks_by_group.pivot(
  columns = "is_click",
  index = "experimental_group",
  values = "user_id"
).reset_index()

clickByGroupPivot["% Clicked"] = clickByGroupPivot[True] / (clickByGroupPivot[True] + clickByGroupPivot[False])
print(clickByGroupPivot)

# Create Dataframes for each experimental groups
a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]
print(a_clicks)
print(b_clicks)
