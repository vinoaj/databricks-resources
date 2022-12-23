# Databricks notebook source
# MAGIC %md # ipywidgets examples
# MAGIC [Original source](https://learn.microsoft.com/en-us/azure/databricks/_static/notebooks/ipywidgets.html)
# MAGIC 
# MAGIC This notebook illustrates how you can use interactive ipywidgets in Databricks notebooks. The examples use one of the datasets that is built-in to Databricks.
# MAGIC 
# MAGIC For more information about ipywidgets, see [the ipywidgets documentation](https://ipywidgets.readthedocs.io/en/7.7.0/index.html).  
# MAGIC 
# MAGIC This notebook steps through how a data scientist might browse a new dataset. To skip directly to examples of ipywidgets, go to Cell 10.
# MAGIC 
# MAGIC ## Requirements
# MAGIC Databricks Runtime 11.0 or above.

# COMMAND ----------

# MAGIC %md The bike-sharing dataset contains two years of daily information about the date, weather, and number of bicycles rented by casual and registered users. 

# COMMAND ----------

sparkDF = spark.read.csv("/databricks-datasets/bikeSharing/data-001/day.csv", header="true", inferSchema="true")
display(sparkDF)

# COMMAND ----------

# MAGIC %md A common way to explore a new dataset is to plot the variables to look for relationships. The next cell creates a scatter plot of the total number of bicycles rented on a day versus the temperature recorded for that day.

# COMMAND ----------

pdf = sparkDF.toPandas()
pdf.plot.scatter(x='temp', y='cnt')

# COMMAND ----------

# MAGIC %md You can create a function to make it easier to browse the different predictors and outcomes.

# COMMAND ----------

def f(x ='temp', y = 'cnt'):
  pdf.plot.scatter(x=x, y=y)

# COMMAND ----------

# MAGIC %md Now you can pass in any two column names to plot the relationship.

# COMMAND ----------

f('hum', 'casual')

# COMMAND ----------

# MAGIC %md With ipywidgets, you can add interactive controls to your plots. The `@interact` [decorator](https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html) lets you define interactive widgets with a single line of code. 
# MAGIC 
# MAGIC After you run the cell below, the plot appears with `cnt` on the y-axis and the default value `temp` on the x-axis. Because the default value of `fit=True`, the plot includes a regression line.
# MAGIC 
# MAGIC You can use the widget selectors above the plot to select a different value for the x-axis and turn on or off the regression line. As you make selections using the widget, changes are reflected immediately in the plot.
# MAGIC 
# MAGIC For details about the different types of ipywidgets, see [the ipywidgets documentation](https://ipywidgets.readthedocs.io/en/7.7.0/index.html).

# COMMAND ----------

import ipywidgets as widgets
import seaborn as sns 
from ipywidgets import interact

# In this code, the list ['temp', 'atemp', 'hum', 'windspeed'] creates a drop-down menu widget. 
# Setting a variable to True or False (`fit=True`) creates a checkbox widget.
@interact(column=['temp', 'atemp', 'hum', 'windspeed'], fit=True)
def f(column='temp', fit=True):
  sns.lmplot(x=column, y='cnt', data=pdf, fit_reg=fit)


# COMMAND ----------

# MAGIC %md In the following cell, the drop-down menu enables you to plot any of the weather variables in a histogram.  
# MAGIC You can also use the bin slider to specify the number of bins in the histogram.

# COMMAND ----------

# In this code, `(bins=(2, 20, 2)` defines an integer slider widget that allows values between 2 and 20 with a step size of 2.
@interact(bins=(2, 20, 2), value=['temp', 'atemp', 'hum', 'windspeed'])
def plot_histogram(bins, value):
  pdf = sparkDF.toPandas()
  pdf.hist(column=value, bins=bins)
