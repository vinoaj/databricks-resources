# Delta Lake: From Data Lake to Lakehouse

This notebook was prepared for [my talk](https://dataengconf.com.au/conference/schedule) at the [**DataEngBytes** conference](https://dataengconf.com.au/conference/sydney) held on 2022-09-29 in Sydney, Australia.

- Author: Vinoaj (Vinny) Vijeyakumaar (vinoaj@gmail.com, vinny.vijeyakumaar@databricks.com)
- _Opinions are my own and not the views of my employer_


## Demo Objectives

Delta Lake provides ACID transactions, scalable metadata handling, and unifies streaming and batch data processing on top of existing data lakes. 

In this demo, we will touch upon Delta Lake's more powerful features:
* ACID transactions
* DML support
* Unify batch & streaming
* Time Travel
* Zero copy clones
* Change data feeds
* ... and more!


### The Data

The data used in this demo is from the Kaggle competition [`predict-closed-questions-on-stack-overflow`](https://www.kaggle.com/competitions/predict-closed-questions-on-stack-overflow/overview).


### The Environment
This notebooks is setup to run in a Databricks Workspace. Databricks clusters are already set up with Spark, Delta Lake, and their respective SDKs (e.g. PySpark). This notebook was developed using **DBR 11.2** (_Spark 3.3.0_)

To set up Delta Lake in a non-Databricks environment, please [follow these instructions](https://docs.delta.io/latest/quick-start.html)