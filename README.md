# databricks-resources
My **personal** list of resources and samples related to working with Databricks. 

## News & Learning Content
- [YouTube channel](https://www.youtube.com/channel/UC3q8O3Bh2Le8Rj1-Q-_UUbA)
- [🎧 Data Brew Podcast](https://databricks.com/discover/data-brew)

## Value Generation
- [Databricks 30 Index](https://databricks.com/blog/2021/03/17/winning-with-data-ai-meet-the-databricks-30-index.html): (March 2021) The Databricks 30 is an equal-weight price index composed of 5 marquee customers each across Retail/Consumer Products, Financial Services, Healthcare, Media/Entertainment, Manufacturing/Logistics, in addition to 5 strategic partners
![Databricks 30 Index performance](https://databricks.com/wp-content/uploads/2021/03/db-30-blog-image-1.png)

## Using Databricks
- Try the [Community Edition](https://community.cloud.databricks.com/login.html) for free (no Databricks or AWS costs are incurred)

## Lakehouse
- [Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics](http://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf) Research paper from the 11th Annual Conference on Innovative Data Systems Research (CIDR ’21), January 11–15, 2021. My [annotated version](assets/cidr2021_paper17_vinoaj_annotated.pdf)

## Administration
- [Functional Workspace Organization on Databricks](https://databricks.com/blog/2022/03/10/functional-workspace-organization-on-databricks.html) (Databricks Admin Essentials: Blog 1/5)

## Apache Spark
- [GitHub: Apache Spark](https://github.com/apache/spark)

## Delta Lake
- [Roadmap](https://github.com/delta-io/delta/issues/920)
- [Releases](https://github.com/delta-io/delta/releases)
- [Release Milestones](https://github.com/delta-io/delta/milestones)
- [Delta Transactional Log Protocol](https://github.com/delta-io/delta/blob/master/PROTOCOL.md)
- [Delta Lake paper](https://databricks.com/wp-content/uploads/2020/08/p975-armbrust.pdf) submitted to VLDB
- [TPC-DS Benchmarking guide](https://github.com/delta-io/delta/tree/master/benchmarks)


### Ingestion
- [Auto-Loader](https://docs.databricks.com/spark/latest/structured-streaming/auto-loader.html)
- [dbt](https://docs.databricks.com/dev-tools/dbt.html) ([GitHub](https://github.com/databricks/dbt-databricks))
- [Build Data and ML Pipelines More Easily With Databricks and Apache Airflow](https://databricks.com/blog/2022/04/29/build-data-and-ml-pipelines-more-easily-with-databricks-and-apache-airflow.html)


### Developing with Delta Lake
- [The Ubiquity of Delta Standalone](https://databricks.com/blog/2022/01/28/the-ubiquity-of-delta-standalone-java-scala-hive-presto-trino-power-bi-and-more.html): a JVM library that can be used to read and write Delta Lake tables. Unlike Delta Lake Core, this project does not use Spark to read or write tables and has only a few transitive dependencies. It can be used by any application (e.g. Power BI) that cannot use a Spark cluster. The project allows developers to build a Delta connector for an external processing engine following the Delta protocol without using a manifest file. 


## Delta Sharing
- [GitHub repository](https://github.com/delta-io/delta-sharing)
- [Release Milestones](https://github.com/delta-io/delta-sharing/milestones)


## Delta Live Tables (DLT)
- [Simplifying Change Data Capture With Databricks Delta Live Tables](https://databricks.com/blog/2022/04/25/simplifying-change-data-capture-with-databricks-delta-live-tables.html)
- [Delivering Real-Time Data to Retailers with Delta Live Tables](https://databricks.com/blog/2022/04/12/delivering-real-time-data-to-retailers-with-delta-live-tables.html) (fully documented [notebooks](https://d1r5llqwmkrl74.cloudfront.net/notebooks/RCG/POS_DLT/index.html#POS_DLT_1.html))
- [How Uplift built CDC and Multiplexing data pipelines with Databricks Delta Live Tables](https://databricks.com/blog/2022/04/27/how-uplift-built-cdc-and-multiplexing-data-pipelines-with-databricks-delta-live-tables.html)

## Analysis
- [PipelineDP](https://github.com/OpenMined/PipelineDP): PipelineDP is a Python framework for applying differentially private aggregations to large datasets using batch processing systems such as Apache Spark, Apache Beam, and more. Developed by [OpenMined](https://www.openmined.org/) and Google

## Performance tuning
- [Make Your Data Lakehouse Run, Faster With Delta Lake 1.1](https://databricks.com/blog/2022/01/31/make-your-data-lakehouse-run-faster-with-delta-lake-1-1.html)
- [Get to Know Your Queries With the New Databricks SQL Query Profile](https://databricks.com/blog/2022/02/23/get-to-know-your-queries-with-the-new-databricks-sql-query-profile.html)
- [Top 5 Performance Tips](https://databricks.com/blog/2022/03/10/top-5-databricks-performance-tips.html)

## Best Practices
- [7 best practices to modernize data architecture on Databricks with LeapLogic](https://www.leaplogic.io/modernization/blog/cloud-engineering-data-engineering-etl-and-analytics-migration-ml-analytics-ai/7-best-practices-modernizing-data-architecture-databricks-lakehouse)

## OSS & No Lock-in
- Founding member of the [Data Cloud Alliance](https://cloud.google.com/solutions/data-cloud-alliance): "Commitment to accelerating adoption across industries through common industry data models, open standards, processes, and end-to-end integrated products and solutions"
- 

## BI
### Power BI
- [Architecting Aggregations in PowerBI with Databricks SQL](https://medium.com/@kyle.hale/architecting-aggregations-in-powerbi-with-databricks-sql-675899014ce3)

## Security
- [Security and Trust Center](https://databricks.com/trust)
- [Databricks Bug Bounty Program](https://hackerone.com/databricks?view_policy=true)


## Machine Learning (ML) & Artificial Intelligence (AI)
### Feature Store
- [eBook: The Comprehensive Guide to Feature Stores](https://databricks.com/wp-content/uploads/2022/03/The-Comprehensive-Guide-to-Feature-Stores.pdf) (Mar 2022)

## MLflow
- [Cross-version Testing in MLflow](https://databricks.com/blog/2022/03/11/cross-version-testing-in-mlflow.html): MLflow integrates with several popular ML frameworks. See how the Databricks Engineering team proactively adapt MLflow and third-party libraries to prevent against breaking changes
- [Model Evaluation in MLflow](https://databricks.com/blog/2022/04/19/model-evaluation-in-mlflow.html)

## Customer Implementations
- [How Gemini Built a Cryptocurrency Analytics Platform Using Lakehouse for Financial Services](https://databricks.com/blog/2022/02/15/how-gemini-built-a-cryptocurrency-analytics-platform-using-lakehouse-for-financial-services.html): "The core lakehouse foundation and features resonated with the team as an efficient way to build the data platform"
![Gemini's Databricks architecture](https://databricks.com/wp-content/uploads/2022/02/gemini-order-book-newimage.png)

## Use Cases
### App Dev
- [Taming JavaScript Exceptions With Databricks](https://databricks.com/blog/2022/01/25/taming-javascript-exceptions-with-databricks.html)

### Cybersecurity
- [Hunting Anomalous Connections and Infrastructure With TLS Certificates: TLS hashes as a source for the cybersecurity threat hunting program](https://databricks.com/blog/2022/01/20/hunting-anomalous-connections-and-infrastructure-with-tls-certificates.html)
- [Learn how to connect Databricks to Okta to ingest System Logs, retain, and analyze for complete visibility using your Databricks Lakehouse Platform](https://databricks.com/blog/2022/04/07/analyzing-okta-logs-with-databricks-lakehouse-platform-to-detect-unusual-activity.html) (accompanying [notebooks](https://databricks.com/wp-content/uploads/notebooks/db-134-okta-logs/index.html#1_okta_create_table.html))

## Deployment
- [AWS Quickstart](https://aws.amazon.com/quickstart/architecture/databricks/)


## ML/AI Roles
### ML Engineer
### Data Scientist
### Software Engineer
### CTO
### ML Researcher
### Data Engineer
### Research Scientist
### SRE
### DevOps

## Community & Support
- [Databricks Community](https://community.databricks.com/s/)
- [Sydney Databricks User Group](https://www.meetup.com/Sydney-Databricks-User-Group/)

# Spark
- [Learning Spark (2nd Edition)](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/) (book)
- [Learning Spark](https://github.com/databricks/LearningSparkV2) code samples

## AWS
- [Build an MLOps sentiment analysis pipeline using Amazon SageMaker Ground Truth and Databricks MLflow](https://aws.amazon.com/blogs/machine-learning/build-an-mlops-sentiment-analysis-pipeline-using-amazon-sagemaker-ground-truth-and-databricks-mlflow/)

## Azure
- [Azure Databricks Best Practices](https://github.com/Azure/AzureDatabricksBestPractices/blob/master/toc.md)

## Geospatial
- [Mosaic](https://github.com/databrickslabs/mosaic): a Databricks Labs extension to the Apache Spark framework that allows easy and fast processing of very large geospatial datasets

## Tools
- [dbx](https://github.com/databrickslabs/dbx): DataBricks CLI eXtensions - aka `dbx` is a CLI tool for advanced Databricks jobs management

## Disaster Recovery (DR) and High Availability (HA)
- [Disaster Recovery Overview, Strategies, and Assessment](https://databricks.com/blog/2022/04/25/disaster-recovery-overview-strategies-and-assessment.html) (Part 1 of DR series)
    - [Disaster Recovery Impact Assessment questionnaire doc](https://databricks.com/wp-content/uploads/2022/04/disaster-recovery-impact-assesment.pdf)

## Feedback / Feature Requests
- Submit feature requests (ideas) through the [Ideas Portal](https://docs.databricks.com/resources/ideas.html)