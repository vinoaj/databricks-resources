# Databricks Resources
My **personal** list of resources and samples related to working with Databricks. _Opinions are my own and not the views of my employer._

---

- By Cloud: [AWS](clouds/aws/README.md) | [Azure](clouds/azure/README.md) | [Google Cloud](clouds/google-cloud/README.md)
- By Industry: [FSI](by-industry/fsi/README.md) | [Healthcare](by-industry/healthcare/README.md) | [Media & Entertainment](by-industry/media-and-entertainment/README.md) | [Retail and CPG](by-industry/retail-and-cpg/README.md)

---

## Keep Current and Learning Resources
### News and Learning Content
[▶️ YouTube channel](https://www.youtube.com/channel/UC3q8O3Bh2Le8Rj1-Q-_UUbA) | [🎧 Data Brew Podcast](https://databricks.com/discover/data-brew) | [📖 Databricks Blog](https://databricks.com/blog)
- [Databricks Academy lab notebooks](https://github.com/databricks-academy)
- [APJ instructor led training (ILT)](https://databricks.com/learn/training/schedule-apj): Please note these are **paid** training courses.

### Community & Support
- Try the [Community Edition](https://community.cloud.databricks.com/login.html) for free (no Databricks or AWS costs are incurred by you)
- [Databricks Community](https://community.databricks.com/s/) Q&A
- Stack Overflow: [databricks](https://stackoverflow.com/questions/tagged/databricks), [apache-spark](https://stackoverflow.com/questions/tagged/apache-spark), [psypark](https://stackoverflow.com/questions/tagged/pyspark), [apache-spark-sql](https://stackoverflow.com/questions/tagged/apache-spark-sql)
- User Groups: 🇦🇺 [Sydney](https://www.meetup.com/Sydney-Databricks-User-Group/) | [Melbourne](https://www.meetup.com/melbourne-databricks-user-group/)

## Feedback / Feature Requests
- Submit feature requests (ideas) through the [Ideas Portal](https://docs.databricks.com/resources/ideas.html)

---

## Value Generation
- [Databricks 30 Index](https://databricks.com/blog/2021/03/17/winning-with-data-ai-meet-the-databricks-30-index.html): (March 2021) The Databricks 30 is an equal-weight price index composed of 5 marquee customers each across Retail/Consumer Products, Financial Services, Healthcare, Media/Entertainment, Manufacturing/Logistics, in addition to 5 strategic partners
![Databricks 30 Index performance](https://databricks.com/wp-content/uploads/2021/03/db-30-blog-image-1.png)

### OSS & No Lock-in
- Founding member of the [Data Cloud Alliance](https://cloud.google.com/solutions/data-cloud-alliance): "Commitment to accelerating adoption across industries through common industry data models, open standards, processes, and end-to-end integrated products and solutions"

---

## Lakehouse Paradigm
- [Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics](http://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf) Research paper from the 11th Annual Conference on Innovative Data Systems Research (CIDR ’21), January 11–15, 2021. My [annotated version](assets/cidr2021_paper17_vinoaj_annotated.pdf)

---

## Deployment Architecture & Management

### Administration
- [Functional Workspace Organization on Databricks](https://databricks.com/blog/2022/03/10/functional-workspace-organization-on-databricks.html) (Databricks Admin Essentials: Blog 1/5)
- [Monitoring Your Databricks Lakehouse Platform with Audit Logs](https://databricks.com/blog/2022/05/02/monitoring-your-databricks-lakehouse-platform-with-audit-logs.html) (Databricks Admin Essentials: Blog 2/5) ([Notebook](https://github.com/andyweaves/databricks-audit-logs))

### Disaster Recovery (DR) and High Availability (HA)
- [Disaster Recovery Overview, Strategies, and Assessment](https://databricks.com/blog/2022/04/25/disaster-recovery-overview-strategies-and-assessment.html) (Part 1 of DR series)
    - [Disaster Recovery Impact Assessment questionnaire doc](https://databricks.com/wp-content/uploads/2022/04/disaster-recovery-impact-assesment.pdf)
- [How illimity Bank Built a Disaster Recovery Strategy on the Lakehouse](https://databricks.com/blog/2022/05/09/how-illimity-bank-built-a-disaster-recovery-strategy-on-the-lakehouse.html) - DR strategy, Terraform management, data & metadata replication strategy

### Security 🔐
- [Security and Trust Center](https://databricks.com/trust)
- [Databricks Bug Bounty Program](https://hackerone.com/databricks?view_policy=true)
- [Audit Log schema](https://docs.databricks.com/administration-guide/account-settings/audit-logs.html#audit-log-schema)

### Unity Catalog
- [Terraform scripts](https://github.com/databricks/unity-catalog-setup)

### Customer Implementations
- [How Gemini Built a Cryptocurrency Analytics Platform Using Lakehouse for Financial Services](https://databricks.com/blog/2022/02/15/how-gemini-built-a-cryptocurrency-analytics-platform-using-lakehouse-for-financial-services.html): "The core lakehouse foundation and features resonated with the team as an efficient way to build the data platform"
![Gemini's Databricks architecture](https://databricks.com/wp-content/uploads/2022/02/gemini-order-book-newimage.png)

---

## Under the Hood: Apache Spark
### Apache Spark
- Apache Spark wins [2022 ACM SIGMOD Systems Award](https://sigmod.org/2022-sigmod-systems-award/)! _“Apache Spark is an innovative, widely-used, open-source, unified data processing system encompassing relational, streaming, and machine-learning workloads.”_
- [GitHub: Apache Spark](https://github.com/apache/spark)
- [Learning Spark (2nd Edition)](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/) (book)
- [Learning Spark](https://github.com/databricks/LearningSparkV2) code samples

### Photon Engine
- [Photon: A Fast Query Engine for Lakehouse Systems](https://www-cs.stanford.edu/~matei/papers/2022/sigmod_photon.pdf): SIGMOD 2022 Paper

---

## Under the Hood: Delta Lake
<img src="https://docs.delta.io/latest/_static/delta-lake-white.png" width="100" alt="Delta Lake Logo"></img>

### Delta Lake
- [Roadmap](https://github.com/delta-io/delta/issues/920)
- [Releases](https://github.com/delta-io/delta/releases)
- [Release Milestones](https://github.com/delta-io/delta/milestones)
- [Delta Transactional Log Protocol](https://github.com/delta-io/delta/blob/master/PROTOCOL.md)
- [Delta Lake paper](https://databricks.com/wp-content/uploads/2020/08/p975-armbrust.pdf) submitted to VLDB
- [TPC-DS Benchmarking guide](https://github.com/delta-io/delta/tree/master/benchmarks)

### Developing with Delta Lake
- [The Ubiquity of Delta Standalone](https://databricks.com/blog/2022/01/28/the-ubiquity-of-delta-standalone-java-scala-hive-presto-trino-power-bi-and-more.html): a JVM library that can be used to read and write Delta Lake tables. Unlike Delta Lake Core, this project does not use Spark to read or write tables and has only a few transitive dependencies. It can be used by any application (e.g. Power BI) that cannot use a Spark cluster. The project allows developers to build a Delta connector for an external processing engine following the Delta protocol without using a manifest file. 

### Delta Sharing
- [GitHub repository](https://github.com/delta-io/delta-sharing)
- [Release Milestones](https://github.com/delta-io/delta-sharing/milestones)
- [Arcuate](https://databricks.com/blog/2022/05/24/arcuate-machine-learning-model-exchange-with-delta-sharing-and-mlflow.html): Machine Learning Model Exchange With Delta Sharing and MLflow

---

## ETL / ELT Patterns
### Ingestion
- [Auto-Loader](https://docs.databricks.com/spark/latest/structured-streaming/auto-loader.html)
- [dbt](https://docs.databricks.com/dev-tools/dbt.html) ([GitHub](https://github.com/databricks/dbt-databricks))
- [Build Data and ML Pipelines More Easily With Databricks and Apache Airflow](https://databricks.com/blog/2022/04/29/build-data-and-ml-pipelines-more-easily-with-databricks-and-apache-airflow.html)

### Ingestion: Streaming
- [Speed Up Streaming Queries With Asynchronous State Checkpointing](https://databricks.com/blog/2022/05/02/speed-up-streaming-queries-with-asynchronous-state-checkpointing.html)
- [Confluent Streaming for Databricks: Build Scalable Real-time Applications on the Lakehouse (Part I)](https://databricks.com/blog/2022/01/13/confluent-streaming-for-databricks-build-scalable-real-time-applications-on-the-lakehouse.html) [(Part II)](https://databricks.com/blog/2022/05/17/build-scalable-real-time-applications-on-the-lakehouse-using-confluent-databricks-part-2.html)

### Delta Live Tables (DLT)
- [Delta Live Tables Cookbook](https://docs.databricks.com/data-engineering/delta-live-tables/delta-live-tables-cookbook.html)
- [Delta Live Tables Notebooks](https://github.com/databricks/delta-live-tables-notebooks)
- [Simplifying Change Data Capture With Databricks Delta Live Tables](https://databricks.com/blog/2022/04/25/simplifying-change-data-capture-with-databricks-delta-live-tables.html)
- [Delivering Real-Time Data to Retailers with Delta Live Tables](https://databricks.com/blog/2022/04/12/delivering-real-time-data-to-retailers-with-delta-live-tables.html) (fully documented [notebooks](https://d1r5llqwmkrl74.cloudfront.net/notebooks/RCG/POS_DLT/index.html#POS_DLT_1.html))
- [Building ETL pipelines for the cybersecurity lakehouse with Delta Live Tables](https://databricks.com/blog/2022/06/03/building-etl-pipelines-for-the-cybersecurity-lakehouse-with-delta-live-tables.html): ingest & evaluate AWS CloudTrail & VPC Flow logs (accompanying notebooks: [CloudTrail DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/cloudtrail-dlt-pipeline.html), [VPC Flow Logs DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/vpc-flow-logs-dlt-pipeline.html), [Zeek DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/zeek-dlt-pipeline.html))
- [How I Built A Streaming Analytics App With SQL and Delta Live Tables](https://databricks.com/blog/2022/05/19/how-i-built-a-streaming-analytics-app-with-sql-and-delta-live-tables.html): accompanying [repo](https://github.com/databricks/delta-live-tables-notebooks/tree/main/divvy-bike-demo)
- [How Uplift built CDC and Multiplexing data pipelines with Databricks Delta Live Tables](https://databricks.com/blog/2022/04/27/how-uplift-built-cdc-and-multiplexing-data-pipelines-with-databricks-delta-live-tables.html)
- [How Audantic Uses Databricks Delta Live Tables to Increase Productivity for Real Estate Market Segments](https://databricks.com/blog/2022/05/05/how-audantic-uses-databricks-delta-live-tables-to-increase-productivity-for-real-estate-market-segments.html)
![Audantic's Delta Live Tables Architecture](https://databricks.com/wp-content/uploads/2022/04/db-80-blog-img-2.png)

---

## Orchestration
### Databricks Workflows
- [Save Time and Money on Data and ML Workflows With “Repair and Rerun”](https://databricks.com/blog/2022/05/06/save-time-and-money-on-data-and-ml-workflows-with-repair-and-rerun.html)

---
## DataOps
- [GitHub Marketplace: Databricks](https://github.com/marketplace?query=databricks+publisher%3Adatabricks+)
- [GitHub Actions documentation](https://docs.databricks.com/dev-tools/ci-cd/ci-cd-github.html)

---

## Analysis


---

## Best Practices
- [7 best practices to modernize data architecture on Databricks with LeapLogic](https://www.leaplogic.io/modernization/blog/cloud-engineering-data-engineering-etl-and-analytics-migration-ml-analytics-ai/7-best-practices-modernizing-data-architecture-databricks-lakehouse)

### Performance tuning
- [Make Your Data Lakehouse Run, Faster With Delta Lake 1.1](https://databricks.com/blog/2022/01/31/make-your-data-lakehouse-run-faster-with-delta-lake-1-1.html)
- [Get to Know Your Queries With the New Databricks SQL Query Profile](https://databricks.com/blog/2022/02/23/get-to-know-your-queries-with-the-new-databricks-sql-query-profile.html)
- [Top 5 Performance Tips](https://databricks.com/blog/2022/03/10/top-5-databricks-performance-tips.html)
- [How to consistently get the best performance from star schema databases](https://databricks.com/blog/2022/05/20/five-simple-steps-for-implementing-a-star-schema-in-databricks-with-delta-lake.html)
- [Reduce Time to Decision With the Databricks Lakehouse Platform and Latest Intel 3rd Gen Xeon Scalable Processors](https://databricks.com/blog/2022/05/17/reduce-time-to-decision-with-the-databricks-lakehouse-platform-and-latest-intel-3rd-gen-xeon-scalable-processors.html): 
"By enabling Databricks Photon and using Intel’s 3rd Gen Xeon Scalable processors, without making any code modifications, we were able to save ⅔ of the costs on our TPC-DS benchmark at 10TB and run 6.7 times quicker"
![price performance](https://databricks.com/wp-content/uploads/2022/05/db-165-blog-img-2.png)

#### Z-Ordering
- Delta Lake orders the data in the Parquet files to make range selection on object storage more efficient
- Limit the number of columns in the Z-Order to the best 1-4

#### ANALYZE
`ANALYZE TABLE db_name.table_name COMPUTE STATISTICS FOR ALL COLUMNS`
- Utilised for [Adaptive Query Execution](https://docs.databricks.com/spark/latest/spark-sql/aqe.html) (AQE), re-optimisations that occur during query execution
- 3 major features of AQE
    - Coalescing post-shuffle partitions
    - Converting sort-merge joins to broadcast joins
    - Skew join optimisation
- `ANALYZE TABLE` collects table statistics that allows AQE to know which plan to choose for you

---

## Machine Learning (ML) & Artificial Intelligence (AI) 🧠
### MLflow
- [Cross-version Testing in MLflow](https://databricks.com/blog/2022/03/11/cross-version-testing-in-mlflow.html): MLflow integrates with several popular ML frameworks. See how the Databricks Engineering team proactively adapt MLflow and third-party libraries to prevent against breaking changes
- [Model Evaluation in MLflow](https://databricks.com/blog/2022/04/19/model-evaluation-in-mlflow.html)

### Feature Store
- [eBook: The Comprehensive Guide to Feature Stores](https://databricks.com/wp-content/uploads/2022/03/The-Comprehensive-Guide-to-Feature-Stores.pdf) (Mar 2022)

### Guides
- [Getting Started with Personalization through Propensity Scoring](https://databricks.com/blog/2022/06/03/getting-started-with-personalization-through-propensity-scoring.html) (accompanying [notebooks](https://d1r5llqwmkrl74.cloudfront.net/notebooks/nightly/RCG/Propensity/index.html#Propensity_1.html))
- [Quantifying uncertainty with Tensorflow Probability](https://databricks.com/blog/2022/04/28/how-wrong-is-your-model.html)


---

## Use Cases
### App Dev
- [Taming JavaScript Exceptions With Databricks](https://databricks.com/blog/2022/01/25/taming-javascript-exceptions-with-databricks.html)

### Cybersecurity 🔐
- [Hunting Anomalous Connections and Infrastructure With TLS Certificates: TLS hashes as a source for the cybersecurity threat hunting program](https://databricks.com/blog/2022/01/20/hunting-anomalous-connections-and-infrastructure-with-tls-certificates.html)
- [Building ETL pipelines for the cybersecurity lakehouse with Delta Live Tables](https://databricks.com/blog/2022/06/03/building-etl-pipelines-for-the-cybersecurity-lakehouse-with-delta-live-tables.html): ingest & evaluate AWS CloudTrail & VPC Flow logs (accompanying notebooks: [CloudTrail DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/cloudtrail-dlt-pipeline.html), [VPC Flow Logs DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/vpc-flow-logs-dlt-pipeline.html), [Zeek DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/zeek-dlt-pipeline.html))
- [Learn how to connect Databricks to Okta to ingest System Logs, retain, and analyze for complete visibility using your Databricks Lakehouse Platform](https://databricks.com/blog/2022/04/07/analyzing-okta-logs-with-databricks-lakehouse-platform-to-detect-unusual-activity.html) (accompanying [notebooks](https://databricks.com/wp-content/uploads/notebooks/db-134-okta-logs/index.html#1_okta_create_table.html))
- [Streaming Windows Event Logs into the Cybersecurity Lakehouse](https://databricks.com/blog/2022/05/05/streaming-windows-event-logs-into-the-cybersecurity-lakehouse.html) ([notebook](https://github.com/DerekKing001/databricks_cyber_notebooks/blob/master/winlogbeats-kafka-sysmon/winlogbeats-kafka-sysmon-example.py))

---

## Geospatial 🌏
- [Mosaic](https://databrickslabs.github.io/mosaic/): a Databricks Labs extension to the Apache Spark framework that allows easy and fast processing of very large geospatial datasets 
- [GitHub: Mosaic](https://github.com/databrickslabs/mosaic)
- [High Scale Geospatial Processing With Mosaic](https://databricks.com/blog/2022/05/02/high-scale-geospatial-processing-with-mosaic.html): writeup on the underlying philosophy behind Mosaic's design

## Tools
- [dbx](https://github.com/databrickslabs/dbx): DataBricks CLI eXtensions - aka `dbx` is a CLI tool for advanced Databricks jobs management

---

## End-to-end Guides
- [Exploration of Twitter sentiment impact on cryptocurrency price](https://databricks.com/blog/2022/05/02/introduction-to-analyzing-crypto-data-using-databricks.html)

---

## Case Studies
- [Australia's heavy vehicle regulator builds 'fatigue engine' to reduce truckie deaths](https://www.itnews.com.au/news/heavy-vehicle-regulator-builds-fatigue-engine-to-reduce-truckie-deaths-580113)

---

## TODO: By Roles
### ML/AI Roles
#### CTO
#### ML Engineer
#### Data Scientist
#### Software Engineer
#### ML Researcher
#### Data Engineer
#### Research Scientist
#### SRE
#### DevOps