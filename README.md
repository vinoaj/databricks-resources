# Databricks Resources
My **personal** list of resources and samples related to working with Databricks. _Opinions are my own and not the views of my employer._

---

## Keep Current and Learning Resources
### News and Learning Content
[▶️ YouTube channel](https://www.youtube.com/channel/UC3q8O3Bh2Le8Rj1-Q-_UUbA) | [🎧 Data Brew Podcast](https://databricks.com/discover/data-brew) | [📖 Databricks Blog](https://databricks.com/blog)
- [Databricks Academy lab notebooks](https://github.com/databricks-academy)

### Community & Support
- Try the [Community Edition](https://community.cloud.databricks.com/login.html) for free (no Databricks or AWS costs are incurred by you)
- [Databricks Community](https://community.databricks.com/s/) Q&A
- Stack Overflow: [databricks](https://stackoverflow.com/questions/tagged/databricks), [apache-spark](https://stackoverflow.com/questions/tagged/apache-spark), [psypark](https://stackoverflow.com/questions/tagged/pyspark), [apache-spark-sql](https://stackoverflow.com/questions/tagged/apache-spark-sql)
- User Groups: 🇦🇺 [Sydney](https://www.meetup.com/Sydney-Databricks-User-Group/) | [Melbourne](https://www.meetup.com/melbourne-databricks-user-group/)

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

### Security
- [Security and Trust Center](https://databricks.com/trust)
- [Databricks Bug Bounty Program](https://hackerone.com/databricks?view_policy=true)
- [Audit Log schema](https://docs.databricks.com/administration-guide/account-settings/audit-logs.html#audit-log-schema)

### Customer Implementations
- [How Gemini Built a Cryptocurrency Analytics Platform Using Lakehouse for Financial Services](https://databricks.com/blog/2022/02/15/how-gemini-built-a-cryptocurrency-analytics-platform-using-lakehouse-for-financial-services.html): "The core lakehouse foundation and features resonated with the team as an efficient way to build the data platform"
![Gemini's Databricks architecture](https://databricks.com/wp-content/uploads/2022/02/gemini-order-book-newimage.png)

---

## Under the Hood: Apache Spark
### Apache Spark
- [GitHub: Apache Spark](https://github.com/apache/spark)
- [Learning Spark (2nd Edition)](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/) (book)
- [Learning Spark](https://github.com/databricks/LearningSparkV2) code samples

### Photon Engine
- [Photon: A Fast Query Engine for Lakehouse Systems](https://www-cs.stanford.edu/~matei/papers/2022/sigmod_photon.pdf): SIGMOD 2022 Paper

---

## Under the Hood: Delta Lake
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

---

## ETL / ELT Patterns
### Ingestion
- [Auto-Loader](https://docs.databricks.com/spark/latest/structured-streaming/auto-loader.html)
- [dbt](https://docs.databricks.com/dev-tools/dbt.html) ([GitHub](https://github.com/databricks/dbt-databricks))
- [Build Data and ML Pipelines More Easily With Databricks and Apache Airflow](https://databricks.com/blog/2022/04/29/build-data-and-ml-pipelines-more-easily-with-databricks-and-apache-airflow.html)

### Delta Live Tables (DLT)
- [Simplifying Change Data Capture With Databricks Delta Live Tables](https://databricks.com/blog/2022/04/25/simplifying-change-data-capture-with-databricks-delta-live-tables.html)
- [Delivering Real-Time Data to Retailers with Delta Live Tables](https://databricks.com/blog/2022/04/12/delivering-real-time-data-to-retailers-with-delta-live-tables.html) (fully documented [notebooks](https://d1r5llqwmkrl74.cloudfront.net/notebooks/RCG/POS_DLT/index.html#POS_DLT_1.html))
- [How Uplift built CDC and Multiplexing data pipelines with Databricks Delta Live Tables](https://databricks.com/blog/2022/04/27/how-uplift-built-cdc-and-multiplexing-data-pipelines-with-databricks-delta-live-tables.html)

---

## Analysis
- [PipelineDP](https://github.com/OpenMined/PipelineDP): PipelineDP is a Python framework for applying differentially private aggregations to large datasets using batch processing systems such as Apache Spark, Apache Beam, and more. Developed by [OpenMined](https://www.openmined.org/) and Google

---

## Best Practices
- [7 best practices to modernize data architecture on Databricks with LeapLogic](https://www.leaplogic.io/modernization/blog/cloud-engineering-data-engineering-etl-and-analytics-migration-ml-analytics-ai/7-best-practices-modernizing-data-architecture-databricks-lakehouse)

### Performance tuning
- [Make Your Data Lakehouse Run, Faster With Delta Lake 1.1](https://databricks.com/blog/2022/01/31/make-your-data-lakehouse-run-faster-with-delta-lake-1-1.html)
- [Get to Know Your Queries With the New Databricks SQL Query Profile](https://databricks.com/blog/2022/02/23/get-to-know-your-queries-with-the-new-databricks-sql-query-profile.html)
- [Top 5 Performance Tips](https://databricks.com/blog/2022/03/10/top-5-databricks-performance-tips.html)

---

## Machine Learning (ML) & Artificial Intelligence (AI)
### MLflow
- [Cross-version Testing in MLflow](https://databricks.com/blog/2022/03/11/cross-version-testing-in-mlflow.html): MLflow integrates with several popular ML frameworks. See how the Databricks Engineering team proactively adapt MLflow and third-party libraries to prevent against breaking changes
- [Model Evaluation in MLflow](https://databricks.com/blog/2022/04/19/model-evaluation-in-mlflow.html)

### Feature Store
- [eBook: The Comprehensive Guide to Feature Stores](https://databricks.com/wp-content/uploads/2022/03/The-Comprehensive-Guide-to-Feature-Stores.pdf) (Mar 2022)

---

## Use Cases
### App Dev
- [Taming JavaScript Exceptions With Databricks](https://databricks.com/blog/2022/01/25/taming-javascript-exceptions-with-databricks.html)

### Cybersecurity
- [Hunting Anomalous Connections and Infrastructure With TLS Certificates: TLS hashes as a source for the cybersecurity threat hunting program](https://databricks.com/blog/2022/01/20/hunting-anomalous-connections-and-infrastructure-with-tls-certificates.html)
- [Learn how to connect Databricks to Okta to ingest System Logs, retain, and analyze for complete visibility using your Databricks Lakehouse Platform](https://databricks.com/blog/2022/04/07/analyzing-okta-logs-with-databricks-lakehouse-platform-to-detect-unusual-activity.html) (accompanying [notebooks](https://databricks.com/wp-content/uploads/notebooks/db-134-okta-logs/index.html#1_okta_create_table.html))

---

## Geospatial
- [Mosaic](https://databrickslabs.github.io/mosaic/): a Databricks Labs extension to the Apache Spark framework that allows easy and fast processing of very large geospatial datasets 
- [GitHub: Mosaic](https://github.com/databrickslabs/mosaic)
- [High Scale Geospatial Processing With Mosaic](https://databricks.com/blog/2022/05/02/high-scale-geospatial-processing-with-mosaic.html): writeup on the underlying philosophy behind Mosaic's design

## Tools
- [dbx](https://github.com/databrickslabs/dbx): DataBricks CLI eXtensions - aka `dbx` is a CLI tool for advanced Databricks jobs management



## Feedback / Feature Requests
- Submit feature requests (ideas) through the [Ideas Portal](https://docs.databricks.com/resources/ideas.html)

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