# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC # Locating farmers markets
# MAGIC [Original source](https://learn.microsoft.com/en-us/azure/databricks/_static/notebooks/ipywidgets-adv.html)
# MAGIC 
# MAGIC This notebook uses Jupyter widgets to explore the farmers markets dataset. Jupyter widgets can make exploring data and working with notebooks easier and more interactive.

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC First, install the [ipyleaflet](https://ipyleaflet.readthedocs.io/en/latest/) Python package. We'll use this later to display geographic data on maps.

# COMMAND ----------

# MAGIC %pip install ipyleaflet==0.17.0

# COMMAND ----------

# MAGIC %md
# MAGIC Read the farmers market data from `databricks-datasets` as a pandas DataFrame.

# COMMAND ----------

import pandas as pd
market_data = pd.read_csv("/dbfs/databricks-datasets/data.gov/farmers_markets_geographic_data/data-001/market_data.csv")
market_data

# COMMAND ----------

# MAGIC %md
# MAGIC The dataset is over 8000 rows and nearly 60 columns, so viewing it all at once is not practical, but you can use ipywidgets to display subsets of the data. 

# COMMAND ----------

import ipywidgets as w
column_widget = w.SelectMultiple(options=market_data.columns, value=["MarketName", "city", "County", "State", "Fruits", "Coffee", "x", "y"])

@w.interact(first_row=(0, len(market_data), 25), columns=column_widget)
def display_data(first_row=0, columns=["MarketName", "city", "County", "State", "Fruits", "Coffee", "x", "y"]):
  return market_data.loc[first_row:first_row+25, columns]

# COMMAND ----------

# MAGIC %md
# MAGIC Now you have a better idea of what kind of data is in the table. Suppose you want to know what markets are available in San Francisco and where they are. You can use a map widget from ipyleaflet to display the location of all the San Francisco farmers markets on an interactive map. You can then zoom in and see the exact location of each market.

# COMMAND ----------

from ipyleaflet import Map, Marker, MarkerCluster

city_map = Map(center=(37.76, -122.45), zoom=12)
local_markets = market_data[market_data.city == "San Francisco"]
locations = [Marker(location=(y, x), draggable=False) for (x, y) in zip(local_markets.x, local_markets.y)]
cluster = MarkerCluster(markers=locations)
city_map.add(cluster)
city_map

# COMMAND ----------

# MAGIC %md
# MAGIC This map is nice, but it's a bit hard to know which market you're looking at on the map. You can redo the markers on the map so that an information popup appears when you click on them. To do this, use the HTML widget to display the name and time for each market. The code below changes the map above, so after you evaluate the cell below, scroll back up to the map to see the changes.

# COMMAND ----------

market_desc = """<div style="white-space: pre">Name: {name}
Season: {season}
Time: {time}</div>
"""

def createMarker(row):
  "Create a marker with an appropriate description from a row in our dataset"
  description = market_desc.format(name=row.MarketName, season=row.Season1Date, time=row.Season1Time)
  return Marker(location=(row.y, row.x), popup=w.HTML(description), draggable=False)

cluster.markers = [createMarker(row) for idx, row in local_markets.iterrows()]

# COMMAND ----------

# MAGIC %md 
# MAGIC To identify markets that sell your favorite foods, add a multiple-select widget to the map to filter the markets based on what you want to buy.

# COMMAND ----------

import operator
import functools
from ipyleaflet import WidgetControl

# The "" option represents no filter
item_list = ["Any product", "Bakedgoods", "Cheese", "Crafts", "Flowers", "Eggs", "Seafood", "Herbs", 
             "Vegetables", "Honey", "Jams", "Meat", "Nuts", "Plants", "Poultry", "Prepared",
             "Soap", "Wine", "Coffee", "Beans", "Fruits"]
item_filter = w.SelectMultiple(options=item_list, rows=len(item_list))

def update_markers(*args):
    selected_items = item_filter.value
    if len(selected_items) == 0 or "Any product" in selected_items:
        filtered_markets = local_markets
    else:
        filter = functools.reduce(operator.and_, (local_markets[item] == "Y" for item in selected_items))
        filtered_markets = local_markets[filter]
    cluster.markers = [createMarker(row) for idx, row in filtered_markets.iterrows()]

item_filter.observe(update_markers, names="value")
city_map.add(WidgetControl(widget=item_filter, position="bottomright"))

# COMMAND ----------

# MAGIC %md
# MAGIC At this point, you've found a market for this weekend, and in the process, you've built a small data application. You can make the application a little more general so you can use it for other areas as well. In the following cell, you add a refresh button to update the markets displayed to match the visible area of the map.

# COMMAND ----------

import numpy as np

max_markers = 200

refresh = w.Button(description="Refresh")
current_bounds = (city_map.north, city_map.south, city_map.east, city_map.west)

def update_local_markets(*args):
    global local_markets
    global current_bounds
    bounds = (city_map.north, city_map.south, city_map.east, city_map.west)
    if bounds == current_bounds:
        return
    else:
        current_bounds = bounds
    local_markets = market_data[market_data.x.between(city_map.west, city_map.east) & market_data.y.between(city_map.south, city_map.north)]
    # If there are a lot of locations, just get the ones closest to the map center
    if len(local_markets) > max_markers:
        dist = np.linalg.norm(local_markets[["y", "x"]] - city_map.center, axis=1)
        closest = dist.argpartition(max_markers)[:max_markers]
        local_markets = local_markets.iloc[closest]
        # make the button have a red border to indicate there are markets that are not shown
        refresh.layout.border = "1px solid red"
    else:
        refresh.layout.border = ""
    update_markers()
  
refresh.on_click(update_local_markets)
city_map.add(WidgetControl(widget=refresh, position="bottomleft"))
