# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC # Delta Lake: Turn your Data Lake into a Lakehouse
# MAGIC &nbsp;
# MAGIC &nbsp;
# MAGIC <div style="background:#110336">
# MAGIC   <img src="https://dataengconf.com.au//images/dataEngLogos/DataEng.MeetUp600x450.option1.v1.jpg?w=320&q=75" style="height:200px"/>
# MAGIC   <img src="https://delta.io/static/delta-lake-logo-a1c0d80d23c17de5f5d7224cb40f15dc.svg" style="height:100px; padding:50px 0;"/>
# MAGIC </div>
# MAGIC &nbsp;
# MAGIC 
# MAGIC This notebook was prepared for [my talk](https://dataengconf.com.au/conference/schedule) at the [**DataEngBytes** conference](https://dataengconf.com.au/conference/sydney) held on 2022-09-29 in Sydney, Australia.    
# MAGIC 
# MAGIC - Author: Vinoaj (Vinny) Vijeyakumaar (vinoaj@gmail.com, vinny.vijeyakumaar@databricks.com)
# MAGIC - _Opinions are my own and not necessarily the views of my employer_
# MAGIC 
# MAGIC 
# MAGIC ## Demo Objectives
# MAGIC 
# MAGIC Delta Lake provides ACID transactions, scalable metadata handling, and unifies streaming and batch data processing on top of existing data lakes. 
# MAGIC 
# MAGIC In this demo, we will touch upon Delta Lake's more powerful features:
# MAGIC * ACID transactions
# MAGIC * DML support
# MAGIC * Unify batch & streaming
# MAGIC * Time Travel
# MAGIC * Change data feeds
# MAGIC * ... and more!
# MAGIC 
# MAGIC 
# MAGIC ### The Data
# MAGIC 
# MAGIC The data used in this demo is from the Kaggle competition [`predict-closed-questions-on-stack-overflow`](https://www.kaggle.com/competitions/predict-closed-questions-on-stack-overflow/overview).
# MAGIC 
# MAGIC 
# MAGIC ### The Environment
# MAGIC This notebooks is setup to run in a Databricks Workspace. Databricks clusters are already set up with Spark, Delta Lake, and their respective SDKs (e.g. PySpark). This notebook was developed using **DBR 11.2** (_Spark 3.3.0_)
# MAGIC 
# MAGIC To set up Delta Lake in a non-Databricks environment, please [follow these instructions](https://docs.delta.io/latest/quick-start.html)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Environment setup

# COMMAND ----------

!pip install kaggle

# COMMAND ----------

import json
import os

# COMMAND ----------

# MAGIC %md
# MAGIC We assume API credentials have already been stored in [Databricks Secrets](https://docs.databricks.com/security/secrets/index.html). 

# COMMAND ----------

USERNAME = "vinny.vijeyakumaar@databricks.com"
SECRETS_SCOPE = "vinnyvijeyakumaar"

KAGGLE_USERNAME = dbutils.secrets.get(scope=SECRETS_SCOPE, key="KAGGLE_USERNAME")
KAGGLE_KEY = dbutils.secrets.get(scope=SECRETS_SCOPE, key="KAGGLE_KEY")
KAGGLE_COMPETITION = "predict-closed-questions-on-stack-overflow"

TABLE_NAME = "stackoverflow_train01"

os.environ['USERNAME'] = USERNAME
os.environ['KAGGLE_USERNAME'] = KAGGLE_USERNAME
os.environ['KAGGLE_KEY'] = KAGGLE_KEY
os.environ['KAGGLE_COMPETITION'] = KAGGLE_COMPETITION

# COMMAND ----------

import kaggle

# COMMAND ----------

# DBTITLE 1,Create DBFS directories to hold our input & Delta Lake files
dbutils.fs.mkdirs(f"/Users/{USERNAME}/custom_demos/input_files/")
dbutils.fs.mkdirs(f"/Users/{USERNAME}/custom_demos/lakehouse/{KAGGLE_COMPETITION}")

# Start with a clean slate by cleaning up artifacts from previous demo runs
dbutils.fs.rm(f"/Users/{USERNAME}/custom_demos/lakehouse/{KAGGLE_COMPETITION}/{TABLE_NAME}", True)

display(dbutils.fs.ls(f"/Users/{USERNAME}/custom_demos/"))

# COMMAND ----------

print(f"/Users/{USERNAME}/custom_demos/lakehouse/{KAGGLE_COMPETITION}/{TABLE_NAME}")
dbutils.fs.rm(f"/Users/{USERNAME}/custom_demos/lakehouse/{KAGGLE_COMPETITION}/{TABLE_NAME}", True)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Download and prepare data files from Kaggle
# MAGIC [Kaggle API documentation](https://github.com/Kaggle/kaggle-api)

# COMMAND ----------

!kaggle competitions download -c $KAGGLE_COMPETITION -p /tmp/$USERNAME/

# COMMAND ----------

# MAGIC %sh
# MAGIC # Create output directory
# MAGIC mkdir -p /tmp/$USERNAME/files/$KAGGLE_COMPETITION/
# MAGIC 
# MAGIC # Extract files
# MAGIC unzip /tmp/$USERNAME/$KAGGLE_COMPETITION.zip -d /tmp/$USERNAME/files/$KAGGLE_COMPETITION/

# COMMAND ----------

#cleanup
!rm /tmp/$USERNAME/$KAGGLE_COMPETITION.zip

# COMMAND ----------

!ls -la /tmp/$USERNAME/files/$KAGGLE_COMPETITION/

# COMMAND ----------

!head /tmp/$USERNAME/files/$KAGGLE_COMPETITION/train.csv

# COMMAND ----------

# MAGIC %md
# MAGIC The downloaded and unzipped files are stored on the driver's local disk. 
# MAGIC We now move the relevant files to `DBFS` so that they're persisted on cloud storage.
# MAGIC 
# MAGIC For the purposes of this demo, we'll only move `train.csv`

# COMMAND ----------

file_pattern = "train.csv"

dbutils.fs.cp(f"file:/tmp/{USERNAME}/files/{KAGGLE_COMPETITION}/{file_pattern}", 
              f"/Users/{USERNAME}/custom_demos/input_files/{KAGGLE_COMPETITION}/", 
              True)

# COMMAND ----------

display(dbutils.fs.ls(f"/Users/{USERNAME}/custom_demos/input_files/{KAGGLE_COMPETITION}/"))

# COMMAND ----------

#cleanup
!rm -rf /tmp/$USERNAME/files/$KAGGLE_COMPETITION/

# COMMAND ----------

# MAGIC %md ## ![](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Delta introduction

# COMMAND ----------

# MAGIC %md ### ![](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Import Data and create a Delta Lake Table
# MAGIC 
# MAGIC &nbsp;
# MAGIC 
# MAGIC <img src="https://databricks.com/wp-content/uploads/2020/12/simplysaydelta.png" width=600/>

# COMMAND ----------

# MAGIC %md
# MAGIC ### Delta Table creation with PySpark

# COMMAND ----------

filename = "train.csv"
filepath = f"/Users/{USERNAME}/custom_demos/input_files/{KAGGLE_COMPETITION}/{filename}"
print(f"Loading contents of: {filepath}")

data_csv = (spark.read
                 .option("header", "true")
                 .option("multiLine", "true")
                 .option("escape", '"') # Handle double quotes in multiline entries
                 .csv(filepath))

(data_csv.write
   .format("delta")
   .mode("overwrite")
   # All Delta Lake files (i.e. data and log files) for this table will be stored here
   .save(f"/Users/{USERNAME}/custom_demos/lakehouse/stackoverflow_train00"))

# COMMAND ----------

# DBTITLE 1,View contents of the Delta table
(spark.read.format("delta")
   .load(f"/Users/{USERNAME}/custom_demos/lakehouse/stackoverflow_train00")
   .display())

# COMMAND ----------

# MAGIC %md
# MAGIC ### Delta Table creation using SQL
# MAGIC 
# MAGIC Let's do the same with SQL instead
# MAGIC 
# MAGIC 
# MAGIC - First use Databricks' native handling of CSVs to create a temporary view with the CSV data
# MAGIC - Then create a Delta Table, specifying
# MAGIC   - Partition columns
# MAGIC   - Table properties (note: `autoOptimize` features are prioritised in Delta Lake's [current roadmap](https://github.com/delta-io/delta/issues/1307))
# MAGIC   - Location to host the Delta data and log files

# COMMAND ----------

# DBTITLE 1,Delta table creation using SQL instead
# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMPORARY VIEW tvw_train
# MAGIC USING CSV -- Databricks-specific operator
# MAGIC OPTIONS(
# MAGIC   path "/Users/vinny.vijeyakumaar@databricks.com/custom_demos/input_files/predict-closed-questions-on-stack-overflow/train.csv",
# MAGIC   header "true", multiLine "true", escape '"'
# MAGIC );
# MAGIC 
# MAGIC -- DROP TABLE IF EXISTS vinny_vijeyakumaar.stackoverflow_train01;
# MAGIC 
# MAGIC -- Create the Delta table
# MAGIC CREATE OR REPLACE TABLE vinny_vijeyakumaar.stackoverflow_train01
# MAGIC USING DELTA
# MAGIC PARTITIONED BY (PostCreationDate)
# MAGIC TBLPROPERTIES(
# MAGIC   delta.enableChangeDataFeed = true, 
# MAGIC   -- autoOptimize.* currently available in Databricks; P1 priority on current Delta Lake OSS roadmap
# MAGIC   delta.autoOptimize.optimizeWrite = true, 
# MAGIC   delta.autoOptimize.autoCompact = true
# MAGIC )
# MAGIC -- (Optional) All Delta Lake files (i.e. data and log files) for this table will be stored here
# MAGIC -- If not specified, location will be managed by your active metastore
# MAGIC LOCATION "/Users/vinny.vijeyakumaar@databricks.com/custom_demos/lakehouse/predict-closed-questions-on-stack-overflow/stackoverflow_train01"
# MAGIC AS
# MAGIC   SELECT 
# MAGIC     PostId
# MAGIC     , DATE(TO_TIMESTAMP(PostCreationDate, "MM/dd/yyyy HH:mm:ss")) AS PostCreationDate
# MAGIC     , * EXCEPT (PostId, PostCreationDate)
# MAGIC   FROM tvw_train;
# MAGIC 
# MAGIC -- Cleanup
# MAGIC DROP VIEW IF EXISTS tvw_train;
# MAGIC 
# MAGIC -- Show data
# MAGIC SELECT *
# MAGIC FROM vinny_vijeyakumaar.stackoverflow_train01;

# COMMAND ----------

# MAGIC %md ## ![](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Exploring Delta Lake's file structure

# COMMAND ----------

# MAGIC %sql 
# MAGIC DESCRIBE DETAIL vinny_vijeyakumaar.stackoverflow_train01;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY vinny_vijeyakumaar.stackoverflow_train01
# MAGIC LIMIT 10;

# COMMAND ----------

# Move paths to variables for easier readability
delta_lake_dbfs_path = f"/Users/{USERNAME}/custom_demos/lakehouse/{KAGGLE_COMPETITION}/stackoverflow_train01/"
delta_lake_dir = f"/dbfs{delta_lake_dbfs_path}"
os.environ['DL_DIR'] = delta_lake_dir

print(f"DBFS path: {delta_lake_dbfs_path}")
print(f"File IO path: {delta_lake_dir}")

def display_log_files(path=None):
  if path is None:
    path = f"{delta_lake_dbfs_path}/_delta_log/"
  
  print(f"Displaying contents of {path}")
  display(dbutils.fs.ls(path))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Data Files
# MAGIC - Data is stored in standard `.parquet` files in the top level directory for the data
# MAGIC - As expected, partitions sit in their own subdirectories

# COMMAND ----------

path = f"{delta_lake_dbfs_path}PostCreationDate=2008-07-31/"
print(f"Displaying contents of {path}")
display(dbutils.fs.ls(path))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Log files
# MAGIC - Transaction log files are stored at the top level `_delta_log/` directory 
# MAGIC - A `.json` log file is created at the end of every successful transaction
# MAGIC - A checkpoint log is created every `n` transactions, and is stored in the `_last_checkpoint` directory
# MAGIC 
# MAGIC _Note_: even 

# COMMAND ----------

path = f"{delta_lake_dbfs_path}_delta_log/"
print(f"Displaying contents of {path}")
display(dbutils.fs.ls(path))

# COMMAND ----------

# DBTITLE 1,Each log contains parquet files stats for efficient data skipping
!head $DL_DIR/_delta_log/00000000000000000000.json

# COMMAND ----------

# DBTITLE 1,Let's get a clean view of the content logs
# Since it's a JSONL file, we'll parse it line-by-line
def pretty_print_log(filename:str):
  if filename.startswith("/dbfs/") is False:
    filename = "/dbfs" + filename
  
  with open(filename, "r") as logfile:
    for line in logfile:
      print(json.dumps(json.loads(line), indent=4))


log_path = f"{delta_lake_dir}/_delta_log/00000000000000000000.json"
pretty_print_log(log_path)

# COMMAND ----------

# Let's get a clean view of some of the stats
with open(log_path, "r") as logfile:
  for line in logfile: 
    try:
      # Look for the first "add" entry with stats
      json_obj = json.loads(line)
      stats = json_obj["add"]["stats"]
      print(f"File: {json_obj['add']['path']}")
      json_stats = json.loads(stats)
      print(json.dumps(json_stats, indent=4))
      break
    except (KeyError, IndexError):
      pass
      

# COMMAND ----------

# MAGIC %md ## ![](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Unified Batch and Streaming Source and Sink
# MAGIC 
# MAGIC Delta Lake can simultaneously support streaming & batch reads & writes on the same table. These cells showcase streaming and batch concurrent queries (inserts and reads)
# MAGIC 
# MAGIC * We will run a streaming query on this data
# MAGIC * This notebook will run an `INSERT` against our `stackoverflow_train01` table

# COMMAND ----------

# Read the insertion of data
(spark.readStream
   .table("vinny_vijeyakumaar.stackoverflow_train01")
   .createOrReplaceTempView("vv_so_train_readStream"))

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Let's look up a post that shouldn't yet exist
# MAGIC SELECT *
# MAGIC FROM vv_so_train_readStream
# MAGIC WHERE PostId = 999999999

# COMMAND ----------

# MAGIC %md **Wait** until the stream is up and running before executing the code below

# COMMAND ----------

# DBTITLE 1,Let's add this user, it'll appear in our map as blue as the stream picks up the update
# MAGIC %sql 
# MAGIC INSERT INTO vinny_vijeyakumaar.stackoverflow_train01
# MAGIC     VALUES (999999999, DATE("2007-08-01"), "", 999999999, "", "", "", "", "", "", "", "", "", "", "")

# COMMAND ----------

# MAGIC %md
# MAGIC ##![](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Full DML Support
# MAGIC 
# MAGIC Delta Lake supports standard DML including UPDATE, DELETE and MERGE INTO providing developers more controls to manage their big datasets.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Delete rows

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Remove "off topic" posts
# MAGIC DELETE FROM vinny_vijeyakumaar.stackoverflow_train01 
# MAGIC WHERE OpenStatus = 'off topic'

# COMMAND ----------

# MAGIC %md
# MAGIC ### Update rows

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Capitalise "open" values
# MAGIC UPDATE vinny_vijeyakumaar.stackoverflow_train01 
# MAGIC SET OpenStatus = "OPEN" 
# MAGIC WHERE OpenStatus = "open"

# COMMAND ----------

# DBTITLE 1,Each of the above transactions will have generated new log files
display_log_files()

# COMMAND ----------

# MAGIC %md
# MAGIC ### MERGE INTO
# MAGIC Upsert into tables using the [`MERGE` SQL Operation](https://docs.delta.io/latest/delta-update.html#upsert-into-a-table-using-merge). 
# MAGIC 
# MAGIC In non-Databricks environments, see [Configure SparkSession](https://docs.delta.io/latest/delta-batch.html#-sql-support) for steps to enable support for SQL commands.

# COMMAND ----------

# MAGIC %md
# MAGIC Let's create a table `load_updates` that contains new data from a source data store

# COMMAND ----------

# MAGIC %sql
# MAGIC -- DROP TABLE vinny_vijeyakumaar.load_updates;
# MAGIC 
# MAGIC CREATE TABLE IF NOT EXISTS vinny_vijeyakumaar.load_updates (
# MAGIC   PostId string, PostCreationDate string, OwnerUserId string,
# MAGIC   OwnerCreationDate string, ReputationAtPostCreation string,
# MAGIC   OwnerUndeletedAnswerCountAtPostTime string, Title string, BodyMarkdown string,
# MAGIC   Tag1 string, Tag2 string, Tag3 string, Tag4 string, Tag5 string, PostClosedDate string,
# MAGIC   OpenStatus string
# MAGIC );
# MAGIC 
# MAGIC TRUNCATE TABLE vinny_vijeyakumaar.load_updates;
# MAGIC 
# MAGIC INSERT INTO vinny_vijeyakumaar.load_updates VALUES
# MAGIC   (999999, DATE("2007-08-01"), "", 999999, "", "", "", "", "", "", "", "", "", "", ""),
# MAGIC   (888888, DATE("2007-08-01"), "", 888888, "", "", "", "", "", "", "", "", "", "", ""),
# MAGIC   (1167904, DATE("2007-08-01"), "", 1167904, "", "", "", "", "", "", "", "", "", "", ""),
# MAGIC   (1078360, DATE("2007-08-01"), "", 1078360, "", "", "", "", "", "", "", "", "", "", "");
# MAGIC 
# MAGIC SELECT * FROM vinny_vijeyakumaar.load_updates;

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO vinny_vijeyakumaar.stackoverflow_train01 AS target
# MAGIC USING vinny_vijeyakumaar.load_updates AS source
# MAGIC ON target.PostId = source.PostId
# MAGIC WHEN MATCHED THEN 
# MAGIC   UPDATE SET * -- Update all columns
# MAGIC WHEN NOT MATCHED 
# MAGIC   THEN INSERT *;
# MAGIC   
# MAGIC SELECT * FROM vinny_vijeyakumaar.stackoverflow_train01 WHERE PostId IN (999999, 888888, 1167904, 1078360);

# COMMAND ----------

display_log_files()

# COMMAND ----------

log_path = f"{delta_lake_dir}/_delta_log/00000000000000000006.json"
pretty_print_log(log_path)

# COMMAND ----------

# MAGIC %md
# MAGIC ## ![](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Checkpoint files

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC <img src="https://github.com/QuentinAmbard/databricks-demo/raw/main/retail/resources/images/delta-lake-perf-bench.png" width="500" style="float: right; margin-left: 50px"/>
# MAGIC 
# MAGIC ### Blazing fast query at scale
# MAGIC 
# MAGIC Log files are compacted in a parquet checkpoint every `n` commits. The checkpoint file contains the entire table structure.
# MAGIC 
# MAGIC Table is self suficient, the metastore doesn't store additional information removing bottleneck and scaling metadata
# MAGIC 
# MAGIC This result in **fast read query**, even with a growing number of files/partitions!

# COMMAND ----------

# MAGIC %md
# MAGIC ### Let's generate more transaction logs

# COMMAND ----------

import random

def generate_transactions(n_transactions:int=1):
  for _ in range(n_transactions):
    scenario = random.randrange(0,2,1)
    
    if scenario == 0:
      # print(f"Scenario {scenario}")
      [x, y] = random.sample(range(100000,999999), 2)
      spark.sql(f"""
        INSERT INTO vinny_vijeyakumaar.stackoverflow_train01 VALUES
          ({x}, DATE("2007-08-01"), "", {x}, "", "", "", "", "", "", "", "", "", "", ""),
          ({y}, DATE("2007-08-01"), "", {y}, "", "", "", "", "", "", "", "", "", "", "")
      """)
    elif scenario == 1:
      # print(f"Scenario {scenario}")
      spark.sql("""
        UPDATE vinny_vijeyakumaar.stackoverflow_train01 VALUES
        SET tag5 = NULL
        WHERE PostId IN (
          SELECT PostId 
          FROM vinny_vijeyakumaar.stackoverflow_train01 
          TABLESAMPLE (2 ROWS)
        )
      """)
    elif scenario == 2:
      # print(f"Scenario {scenario}")
      spark.sql("""
        DELETE FROM vinny_vijeyakumaar.stackoverflow_train01
        WHERE PostId IN (
          SELECT PostId 
          FROM vinny_vijeyakumaar.stackoverflow_train01 
          TABLESAMPLE (2 ROWS)
        )
      """)
      

generate_transactions(250)

# COMMAND ----------

# MAGIC %md
# MAGIC ### ![](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Checkpoint files
# MAGIC [Protocol reference](https://github.com/delta-io/delta/blob/master/PROTOCOL.md#checkpoints)
# MAGIC 
# MAGIC Checkpoint files are stored as `parquet` files in the `_delta_log` directory

# COMMAND ----------

!ls /dbfs/Users/vinny.vijeyakumaar@databricks.com/custom_demos/lakehouse/predict-closed-questions-on-stack-overflow/stackoverflow_train01/_delta_log/*.checkpoint.*

# COMMAND ----------

# MAGIC %md
# MAGIC Rather than listing an entire directory to determine the last available checkpoint file, readers can locate the most recent checkpoint by looking at the `_delta_log/_last_checkpoint` file (which is a `JSON` file)
# MAGIC 
# MAGIC [Protocol reference](https://github.com/delta-io/delta/blob/master/PROTOCOL.md#last-checkpoint-file)
# MAGIC 
# MAGIC The checkpoint file points the reader to the latest available checkpoint log. In the below example it is `202`

# COMMAND ----------

filename = f"/dbfs/Users/{USERNAME}/custom_demos/lakehouse/{KAGGLE_COMPETITION}/stackoverflow_train01/_delta_log/_last_checkpoint"
with open(filename, "r") as checkpoint_file:
    for line in checkpoint_file:
      print(json.dumps(json.loads(line), indent=4))

# COMMAND ----------

# MAGIC %md
# MAGIC A checkpoint file summarises the current state of the table's underlying files up to that checkpoint's version.
# MAGIC A reader would reconstitute the current state of the table by
# MAGIC - Reading the checkpoint file
# MAGIC - Reading all **subsequent** log files (in this example it would be log files `0...203.json` and above)

# COMMAND ----------

display(spark.read.parquet(f"/Users/{USERNAME}/custom_demos/lakehouse/{KAGGLE_COMPETITION}/stackoverflow_train01/_delta_log/00000000000000000202.checkpoint.parquet"))

# COMMAND ----------

# MAGIC %md
# MAGIC ##![](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Schema enforcement & constraints

# COMMAND ----------

# DBTITLE 1,Attempting to write bad data will throw an error
# MAGIC %sql
# MAGIC INSERT INTO vinny_vijeyakumaar.stackoverflow_train01 VALUES
# MAGIC   ("abc", "2007-08-01", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "extraColumn"),
# MAGIC   ("xyz", DATE("2007-08-01"), "", 999999, "", "", "", "", "", "", "", "", "", "", "", "")

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO vinny_vijeyakumaar.stackoverflow_train01 VALUES
# MAGIC   ("abc", "2007-08-01", "", "", "", "", "", "", "", "", "", "", "", "", "", ""),
# MAGIC   ("xyz", DATE("2007-08-01"), "", 999999, "", "", "", "", "", "", "", "", "", "", "", "")

# COMMAND ----------

# DBTITLE 1,Let's add constraints
# MAGIC %sql
# MAGIC ALTER TABLE vinny_vijeyakumaar.stackoverflow_train01 
# MAGIC   ADD CONSTRAINT post_id_not_null CHECK (PostId IS NOT NULL);
# MAGIC 
# MAGIC ALTER TABLE vinny_vijeyakumaar.stackoverflow_train01 
# MAGIC   ADD CONSTRAINT post_creation_date_valid CHECK (
# MAGIC     PostCreationDate BETWEEN "2007-08-01" AND "2012-09-01");

# COMMAND ----------

# DBTITLE 1,An exception is thrown if existing rows violate a constraint. Let's try again.
# MAGIC %sql
# MAGIC DELETE FROM vinny_vijeyakumaar.stackoverflow_train01 
# MAGIC WHERE
# MAGIC   PostCreationDate < "2007-08-01"
# MAGIC   OR PostCreationDate > "2012-09-01"
# MAGIC   OR PostCreationDate IS NULL;
# MAGIC   
# MAGIC ALTER TABLE vinny_vijeyakumaar.stackoverflow_train01 
# MAGIC   ADD CONSTRAINT post_creation_date_valid CHECK (
# MAGIC     PostCreationDate BETWEEN "2007-08-01" AND "2012-09-01");

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO vinny_vijeyakumaar.stackoverflow_train01 VALUES
# MAGIC   ("xyz", DATE("2022-09-29"), "", 999999, "", "", "", "", "", "", "", "", "", "", "")

# COMMAND ----------

# MAGIC %md
# MAGIC ##![](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Schema Evolution
# MAGIC With the `mergeSchema` option, you can evolve your Delta Lake table schema
# MAGIC 
# MAGIC Let's merge into a table, simultaneously:
# MAGIC - Introducing 2 new columns `newCol1`, `newCol2`
# MAGIC - Updating some existing records

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS vinny_vijeyakumaar.load_updates_02 (
# MAGIC   PostId string, PostCreationDate string, OwnerUserId string,
# MAGIC   OwnerCreationDate string, ReputationAtPostCreation string,
# MAGIC   OwnerUndeletedAnswerCountAtPostTime string, Title string, BodyMarkdown string,
# MAGIC   Tag1 string, Tag2 string, Tag3 string, Tag4 string, Tag5 string, PostClosedDate string,
# MAGIC   OpenStatus string, newCol1 string, newCol2 string
# MAGIC );
# MAGIC 
# MAGIC TRUNCATE TABLE vinny_vijeyakumaar.load_updates_02;
# MAGIC 
# MAGIC INSERT INTO vinny_vijeyakumaar.load_updates_02 VALUES
# MAGIC   (999999, DATE("2007-08-01"), "", 999999, "", "", "", "", "", "", "", "", "", "", "", "A", "B"),
# MAGIC   (888888, DATE("2007-08-01"), "", 888888, "", "", "", "", "", "", "", "", "", "", "", "1", "2"),
# MAGIC   (1167904, DATE("2007-08-01"), "", 1167904, "", "", "", "", "", "", "", "", "", "", "", "X", "Y"),
# MAGIC   (1078360, DATE("2007-08-01"), "", 1078360, "", "", "", "", "", "", "", "", "", "", "", "99", "99");
# MAGIC 
# MAGIC SELECT * FROM vinny_vijeyakumaar.load_updates_02

# COMMAND ----------

# MAGIC %md
# MAGIC At this point `MERGE INTO` will do two things:
# MAGIC - Add the two new columns to the schema
# MAGIC - Update relevant records

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO vinny_vijeyakumaar.stackoverflow_train01 AS target
# MAGIC USING vinny_vijeyakumaar.load_updates_02 AS source
# MAGIC ON target.PostId = source.PostId
# MAGIC WHEN MATCHED THEN 
# MAGIC   UPDATE SET * -- Update all columns
# MAGIC WHEN NOT MATCHED 
# MAGIC   THEN INSERT *;
# MAGIC   
# MAGIC SELECT * FROM vinny_vijeyakumaar.stackoverflow_train01 WHERE PostId IN (999999, 888888, 1167904, 1078360);

# COMMAND ----------

# MAGIC %md ## ![](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Let's Travel back in Time!
# MAGIC Databricks Delta’s time travel capabilities simplify building data pipelines for the following use cases. 
# MAGIC 
# MAGIC * Audit Data Changes
# MAGIC * Reproduce experiments & reports
# MAGIC * Rollbacks
# MAGIC 
# MAGIC As you write into a Delta table or directory, every operation is automatically versioned.
# MAGIC 
# MAGIC You can query by:
# MAGIC 1. Using a timestamp
# MAGIC 1. Using a version number
# MAGIC 
# MAGIC using Python, Scala, and/or Scala syntax; for these examples we will use the SQL syntax.  
# MAGIC 
# MAGIC For more information, refer to [Introducing Delta Time Travel for Large Scale Data Lakes](https://databricks.com/blog/2019/02/04/introducing-delta-time-travel-for-large-scale-data-lakes.html)

# COMMAND ----------

# MAGIC %md ### ![](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Review Delta Lake Table History
# MAGIC All the transactions for this table are stored within this table including the initial set of insertions, update, delete, merge, and inserts with schema modification

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY vinny_vijeyakumaar.stackoverflow_train01
# MAGIC LIMIT 20 -- get the last 20 operations

# COMMAND ----------

# MAGIC %md ### ![](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Time Travel via Version Number or Timestamp
# MAGIC Below are SQL syntax examples of Delta Time Travel by using a **version number** or **timestamp**

# COMMAND ----------

# MAGIC %sql
# MAGIC WITH rec_count_00 AS (
# MAGIC   SELECT COUNT(*) AS n FROM vinny_vijeyakumaar.stackoverflow_train01 
# MAGIC   VERSION AS OF 1
# MAGIC )
# MAGIC , rec_count_01 AS (
# MAGIC   SELECT COUNT(*) AS n FROM vinny_vijeyakumaar.stackoverflow_train01
# MAGIC   TIMESTAMP AS OF (CURRENT_TIMESTAMP() - INTERVAL 240 MINUTES)
# MAGIC )
# MAGIC , rec_count_now AS (
# MAGIC   SELECT COUNT(*) AS n FROM vinny_vijeyakumaar.stackoverflow_train01
# MAGIC )
# MAGIC SELECT r0.n AS start, r1.n AS 240minsAgo, rn.n AS now
# MAGIC FROM rec_count_00 r0, rec_count_01 r1, rec_count_now rn

# COMMAND ----------

# MAGIC %md ### ![](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Restoring previous versions of a Delta Table
# MAGIC 
# MAGIC [Documentation](https://docs.delta.io/latest/delta-utility.html#restore-a-delta-table-to-an-earlier-state)

# COMMAND ----------

# DBTITLE 1,Using Time Travel, we can restore a table to a previous state
# MAGIC %sql
# MAGIC -- Restore table to previous state
# MAGIC RESTORE TABLE vinny_vijeyakumaar.stackoverflow_train01 
# MAGIC TO VERSION AS OF 12 -- by version
# MAGIC -- TO TIMESTAMP AS OF "2022-09-28 10:00:00" -- or by point in time

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ## ![](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Delta Lake CDF (Change Data Feed) to support data sharing and Datamesh organization
# MAGIC <img src="https://github.com/QuentinAmbard/databricks-demo/raw/main/retail/resources/images/delta-cdf-datamesh.png" style="float:right; margin-right: 50px" width="300px" />
# MAGIC &nbsp;
# MAGIC 
# MAGIC Enable [Change Data Feed](https://docs.delta.io/2.0.0/delta-change-data-feed.html) on your Delta table. With CDF, you can track all the changes (INSERT/UPDATE/DELETE) from your table.
# MAGIC 
# MAGIC It's then easy to subscribe to modifications stream on one of your table to propagate changes downsteram (e.g. GDPR DELETEs downstream)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Enable Change Data Feed on an existing table
# MAGIC If you wish to enable Change Data Feed on an existing table, simply alter the table's `TBLPROPERTIES`

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE vinny_vijeyakumaar.stackoverflow_train01
# MAGIC SET TBLPROPERTIES (delta.enableChangeDataFeed = true)

# COMMAND ----------

# MAGIC %md
# MAGIC ### View changes to the table
# MAGIC Query the metatable `TABLE_CHANGES` to view change data history. 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM TABLE_CHANGES("vinny_vijeyakumaar.stackoverflow_train01", 0)
# MAGIC WHERE PostId = "1167904"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Propagate changes downstream
# MAGIC This is just an example. Attempting to run it won't work unless you have the relevant target table already created.

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO target_schema.target_table 
# MAGIC SELECT * EXCEPT (_change_type, _commit_version, _commit_timestamp)
# MAGIC -- Let's assume our orchestration tool knows that the last update happened at 2022-09-29 00:00:00
# MAGIC FROM TABLE_CHANGES("vinny_vijeyakumaar.stackoverflow_train01", "2022-09-29 00:00:00")
# MAGIC WHERE _change_type IN ("insert", "update_postimage");
# MAGIC 
# MAGIC 
# MAGIC DELETE FROM target_schema.target_table 
# MAGIC WHERE PostId IN (
# MAGIC   SELECT PostId
# MAGIC   -- Let's assume our orchestration tool knows that the last update happened at 2022-09-29 00:00:00
# MAGIC   FROM TABLE_CHANGES("vinny_vijeyakumaar.stackoverflow_train01", "2022-09-29 00:00:00")
# MAGIC   WHERE _change_type IN ("delete")
# MAGIC );

# COMMAND ----------

# MAGIC %md
# MAGIC ## ![](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Keeping a clean file system

# COMMAND ----------

# MAGIC %md
# MAGIC ### `OPTIMIZE`
# MAGIC Coalesce many small files into larger files

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE vinny_vijeyakumaar.stackoverflow_train01

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY vinny_vijeyakumaar.stackoverflow_train01 LIMIT 1;
# MAGIC 
# MAGIC -- Looking at operationMetrics, we can see that 43 files were coalesced into a single file

# COMMAND ----------

# MAGIC %md
# MAGIC ### `VACUUM`
# MAGIC You can remove files no longer referenced by a Delta table and are older than the retention threshold by running the vacuum command on the table. `VACUUM` is not triggered automatically. The default retention threshold for the files is 7 days. 
# MAGIC 
# MAGIC **Note**: Vacuuming will prevent the ability to time travel back to a version where that version's files have been removed

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM vinny_vijeyakumaar.stackoverflow_train01 RETAIN 12 HOURS DRY RUN

# COMMAND ----------

# MAGIC %sql
# MAGIC SET spark.databricks.delta.retentionDurationCheck.enabled = false;
# MAGIC 
# MAGIC -- Use `DRY RUN` to verify which files will be deleted
# MAGIC VACUUM vinny_vijeyakumaar.stackoverflow_train01 RETAIN 12 HOURS DRY RUN;

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM vinny_vijeyakumaar.stackoverflow_train01 RETAIN 12 HOURS

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM vinny_vijeyakumaar.stackoverflow_train01;

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC 
# MAGIC # Thank you for following along!
# MAGIC &nbsp;
# MAGIC &nbsp;
# MAGIC <div style="background:#110336">
# MAGIC   <img src="https://dataengconf.com.au//images/dataEngLogos/DataEng.MeetUp600x450.option1.v1.jpg?w=320&q=75" style="height:200px"/>
# MAGIC   <img src="https://delta.io/static/delta-lake-logo-a1c0d80d23c17de5f5d7224cb40f15dc.svg" style="height:100px; padding:50px 0;"/>
# MAGIC </div>
# MAGIC &nbsp;
# MAGIC 
# MAGIC Find [**more resources here**](https://github.com/vinoaj/databricks-resources/tree/main/presentations/dataengconf_syd_20220929)

# COMMAND ----------

# MAGIC %md
# MAGIC # Upcoming Databricks Events ... Join Us!
# MAGIC ## (Free & in-person!) Data+AI World Tour Sydney
# MAGIC ![Data+AI World Tour Sydney](https://github.com/vinoaj/databricks-resources/raw/main/assets/img/data_ai_world_tour_sydney.png)
# MAGIC 
# MAGIC [🔗 Registration link](https://www.databricks.com/dataaisummit/worldtour/sydney)
# MAGIC 
# MAGIC Our lineup of data and AI experts, leaders and visionaries includes [Matei Zaharia](https://www.linkedin.com/in/mateizaharia), co-founder Apache Spark and Databricks. 
# MAGIC 
# MAGIC Come spend the day with Lakehouse experts and practitioners from across Australia and New Zealand. Learn howlocal entrprises and startups are pushing the Lakehouse boundaries!
# MAGIC 
# MAGIC ## (Free & in-person!) Databricks Bootcamps
# MAGIC [🔗 Registration link](https://pages.databricks.com/00-202202-APJ-FE-Databricks-Bootcamp-2022-q4-Router_LP---Registration-page.html?utm_source=databricks&utm_medium=vinny&utm_campaign=7013f000000LkDCAA0)
# MAGIC 
# MAGIC We're holding **free** Databricks Bootcamps across Brisbane, Sydney, Melbourne, Adelaide, Perth, and Auckland over Oct - Dec.
# MAGIC 
# MAGIC Led by Databricks instructors, these sessions will use real-world data sets as we go under the hood to demonstrate how to use robust technologies such as Delta Lake, Databricks SQL and MLflow
