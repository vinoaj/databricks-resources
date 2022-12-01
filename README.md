# Databricks Resources
My **personal** list of resources and samples related to working with Databricks. _Opinions are my own and not the views of my employer._

---

- By Cloud: [AWS](clouds/aws/README.md) | [Azure](clouds/azure/README.md) | [Google Cloud](clouds/google-cloud/README.md)
- By Industry: [FSI](by-industry/fsi/README.md) | [Healthcare](by-industry/healthcare/README.md) | [Media & Entertainment](by-industry/media-and-entertainment/README.md) | [Retail and CPG](by-industry/retail-and-cpg/README.md)

---

## Keep Current and Learning Resources
### News and Learning Content
[▶️ YouTube channel](https://www.youtube.com/channel/UC3q8O3Bh2Le8Rj1-Q-_UUbA) | [🎧 Data Brew Podcast](https://databricks.com/discover/data-brew) | [📖 Databricks Blog](https://databricks.com/blog)
- [📄 Databricks Academy lab notebooks](https://github.com/databricks-academy)
- [📄 Databricks Industry Solutions notebooks](https://github.com/databricks-industry-solutions)
- [▶️ Data + AI Summit (DAIS) 2022 recordings](https://www.youtube.com/playlist?list=PLTPXxbhUt-YVWi_cf2UUDc9VZFLoRgu0l)
- [APJ instructor led training (ILT)](https://databricks.com/learn/training/schedule-apj): Please note these are **paid** training courses.

### Release Notes
- Azure Databricks: [Platform release notes](https://docs.microsoft.com/en-us/azure/databricks/release-notes/product/) | [Runtime release notes](https://docs.microsoft.com/en-us/azure/databricks/release-notes/runtime/) | [Databricks SQL release notes](https://docs.microsoft.com/en-us/azure/databricks/sql/release-notes/)

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
- [Don’t Let a Cloud Data Warehouse Bottleneck your Machine Learning](https://www.linkedin.com/pulse/dont-let-cloud-data-warehouse-bottleneck-your-machine-jason-pohl/)

---

## Deployment Architecture & Management

### Architecture Design
- [6 Guiding Principles to Build an Effective Data Lakehouse](https://databricks.com/blog/2022/07/14/6-guiding-principles-to-build-an-effective-data-lakehouse.html)
- [Data Warehousing Modeling Techniques and Their Implementation on the Databricks Lakehouse Platform](https://databricks.com/blog/2022/06/24/data-warehousing-modeling-techniques-and-their-implementation-on-the-databricks-lakehouse-platform.html)
- [Five Simple Steps for Implementing a Star Schema in Databricks With Delta Lake](https://databricks.com/blog/2022/05/20/five-simple-steps-for-implementing-a-star-schema-in-databricks-with-delta-lake.html)
- [Databricks Lakehouse and Data Mesh, (Part 1)](https://www.databricks.com/blog/2022/10/10/databricks-lakehouse-and-data-mesh-part-1.html) [(Part 2)](https://www.databricks.com/blog/2022/10/19/building-data-mesh-based-databricks-lakehouse-part-2.html)
![Data Mesh architecture](https://cms.databricks.com/sites/default/files/inline-images/db-363-blog-image-3.png)
- [Dimensional modeling implementation on the modern lakehouse using Delta Live Tables](https://www.databricks.com/blog/2022/11/07/load-edw-dimensional-model-real-time-databricks-lakehouse.html)
- [Prescriptive Guidance for Implementing a Data Vault Model on the Databricks Lakehouse Platform](https://databricks.com/blog/2022/06/24/prescriptive-guidance-for-implementing-a-data-vault-model-on-the-databricks-lakehouse-platform.html)
- [Architecting MLOps on the Lakehouse](https://databricks.com/blog/2022/06/22/architecting-mlops-on-the-lakehouse.html)
- [Leveraging Delta Across Teams at McGraw Hill](https://www.databricks.com/blog/2022/09/14/leveraging-delta-across-teams-mcgraw-hill.html) ([source code](https://github.com/MHEducation/databricks-athena-blog-code) to automate the Databricks to Athena manifest based integration)
![McGraw Hill architecture](https://cms.databricks.com/sites/default/files/inline-images/db-302-blog-img-4.png)

### Administration
- [Databricks Workspace Administration – Best Practices for Account, Workspace and Metastore Admins](https://www.databricks.com/blog/2022/08/26/databricks-workspace-administration-best-practices-for-account-workspace-and-metastore-admins.html)
- [Functional Workspace Organization on Databricks](https://databricks.com/blog/2022/03/10/functional-workspace-organization-on-databricks.html) (Databricks Admin Essentials: Blog 1/5)
- [Monitoring Your Databricks Lakehouse Platform with Audit Logs](https://databricks.com/blog/2022/05/02/monitoring-your-databricks-lakehouse-platform-with-audit-logs.html) (Databricks Admin Essentials: Blog 2/5) ([Notebook](https://github.com/andyweaves/databricks-audit-logs))
- [Best Practices for Cost Management on Databricks](https://www.databricks.com/blog/2022/10/18/best-practices-cost-management-databricks.html)

### Disaster Recovery (DR) and High Availability (HA)
- [Disaster Recovery Overview, Strategies, and Assessment](https://databricks.com/blog/2022/04/25/disaster-recovery-overview-strategies-and-assessment.html) (Part 1 of DR series) ([Part 2](https://databricks.com/blog/2022/07/18/disaster-recovery-automation-and-tooling-for-a-databricks-workspace.html))
    - [Disaster Recovery Impact Assessment questionnaire doc](https://databricks.com/wp-content/uploads/2022/04/disaster-recovery-impact-assesment.pdf)
- [How illimity Bank Built a Disaster Recovery Strategy on the Lakehouse](https://databricks.com/blog/2022/05/09/how-illimity-bank-built-a-disaster-recovery-strategy-on-the-lakehouse.html) - DR strategy, Terraform management, data & metadata replication strategy

### Security 🔐
- [Security and Trust Center](https://databricks.com/trust)
- [Databricks Bug Bounty Program](https://hackerone.com/databricks?view_policy=true) (example of bug bounty response: [Admin Isolation on Shared Clusters](https://www.databricks.com/blog/2022/10/10/admin-isolation-shared-clusters.html))
- [Security Analysis Tool (SAT)](https://www.databricks.com/blog/2022/11/02/announcing-security-analysis-tool-sat.html): [📄 GitHub repo](https://github.com/databricks-industry-solutions/security-analysis-tool), [▶️ Setup instructions](https://www.youtube.com/watch?v=kLSc3UHKL40)
- [Audit Log schema](https://docs.databricks.com/administration-guide/account-settings/audit-logs.html#audit-log-schema)
- [Admin Isolation on Shared Clusters](https://www.databricks.com/blog/2022/10/10/admin-isolation-shared-clusters.html)
- [Scanning for Arbitrary Code in Databricks Workspace With Improved Search and Audit Logs](https://databricks.com/blog/2022/07/19/scanning-for-arbitrary-code-in-databricks-workspace-with-improved-search-and-audit-logs.html)
- [Monitoring Notebook Command Logs With Static Analysis Tools](https://www.databricks.com/blog/2022/11/02/monitoring-notebook-command-logs-static-analysis-tools.html) ([📄 Notebooks](https://github.com/granturing/notebook-monitoring))
- [How Databricks restricts third party libraries in JVM compute platforms](https://www.databricks.com/blog/2022/08/23/restricting-libraries-in-jvm-compute-platforms.html)

### Unity Catalog 🔐
- [Terraform scripts](https://github.com/databricks/unity-catalog-setup)
- [Export lineage via API](https://github.com/databricks/unity-catalog-setup/blob/main/lineage/lineage_export.py) example

#### Migrating to Unity Catalog
- [How to Seamlessly Upgrade Your Hive Metastore Objects to the Unity Catalog Metastore Using SYNC](https://www.databricks.com/blog/2022/11/03/how-seamlessly-upgrade-your-hive-metastore-objects-unity-catalog-metastore-using) ([📄 notebook](https://www.databricks.com/wp-content/uploads/notebooks/db-382-unity-table-hive.dbc))
- [Simplify Access Policy Management With Privilege Inheritance in Unity Catalog](https://www.databricks.com/blog/2022/10/21/simplify-access-policy-management-privilege-inheritance-unity-catalog.html)

### Customer Implementations
- [How Gemini Built a Cryptocurrency Analytics Platform Using Lakehouse for Financial Services](https://databricks.com/blog/2022/02/15/how-gemini-built-a-cryptocurrency-analytics-platform-using-lakehouse-for-financial-services.html): "The core lakehouse foundation and features resonated with the team as an efficient way to build the data platform"
![Gemini's Databricks architecture](https://databricks.com/wp-content/uploads/2022/02/gemini-order-book-newimage.png)

---

## Under the Hood: Apache Spark
### Apache Spark
- [Apache Spark and Photon Receive SIGMOD Awards](https://databricks.com/blog/2022/06/15/apache-spark-and-photon-receive-sigmod-awards.html)
- Apache Spark wins [2022 ACM SIGMOD Systems Award](https://sigmod.org/2022-sigmod-systems-award/)! _“Apache Spark is an innovative, widely-used, open-source, unified data processing system encompassing relational, streaming, and machine-learning workloads.”_
- [GitHub: Apache Spark](https://github.com/apache/spark)
- [Learning Spark (2nd Edition)](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/) (book)
- [Learning Spark](https://github.com/databricks/LearningSparkV2) code samples

---

## Under the Hood: Photon Engine
- [Photon: A Fast Query Engine for Lakehouse Systems](https://www-cs.stanford.edu/~matei/papers/2022/sigmod_photon.pdf): SIGMOD 2022 Paper
- [Apache Spark and Photon Receive SIGMOD Awards](https://databricks.com/blog/2022/06/15/apache-spark-and-photon-receive-sigmod-awards.html)
- [▶️ Advancing Spark - The Photon Whitepaper](https://www.youtube.com/watch?v=hxvQxI4FksY)
- [How DuPont achieved 11x latency reduction and 4x cost reduction with Photon](https://www.databricks.com/blog/2022/10/04/how-dupont-achieved-11x-latency-reduction-and-4x-cost-reduction-photon.html)

---

## Under the Hood: Delta Lake
<img src="https://docs.delta.io/latest/_static/delta-lake-white.png" width="100" alt="Delta Lake Logo"></img>
- [Roadmap](https://github.com/delta-io/delta/issues/1307)
- [Releases](https://github.com/delta-io/delta/releases)
- [Release Milestones](https://github.com/delta-io/delta/milestones)
- [Delta Transactional Log Protocol](https://github.com/delta-io/delta/blob/master/PROTOCOL.md)
- [📄 Delta Lake VLDB paper](https://databricks.com/wp-content/uploads/2020/08/p975-armbrust.pdf) (my [annotated version](../../assets/p975-armbrust_vinoaj_annotated.pdf))
- 📘 Delta Lake: The Definitive Guide (O'Reilly) ([access free preview](https://www.databricks.com/p/ebook/delta-lake-the-definitive-guide-by-oreilly) | [PDF direct link](https://www.databricks.com/wp-content/uploads/2021/05/9781098104528-1.pdf))
- [Diving Into Delta Lake: Unpacking The Transaction Log](https://www.databricks.com/blog/2019/08/21/diving-into-delta-lake-unpacking-the-transaction-log.html)
- [Diving Into Delta Lake: Schema Enforcement & Evolution](https://www.databricks.com/blog/2019/09/24/diving-into-delta-lake-schema-enforcement-evolution.html)
- [Diving Into Delta Lake: DML Internals (Update, Delete, Merge)](https://www.databricks.com/blog/2020/09/29/diving-into-delta-lake-dml-internals-update-delete-merge.html)
- [Processing Petabytes of Data in Seconds with Databricks Delta](https://www.databricks.com/blog/2018/07/31/processing-petabytes-of-data-in-seconds-with-databricks-delta.html)
- [Top 5 Reasons to Convert Your Cloud Data Lake to a Delta Lake](https://databricks.com/blog/2020/08/21/top-5-reasons-to-convert-your-cloud-data-lake-to-a-delta-lake.html)
- [How to Rollback a Delta Lake Table to a Previous Version with Restore](https://delta.io/blog/2022-10-03-rollback-delta-lake-restore/)
- [TPC-DS Benchmarking guide](https://github.com/delta-io/delta/tree/master/benchmarks)

### Developing with Delta Lake
- [The Ubiquity of Delta Standalone](https://databricks.com/blog/2022/01/28/the-ubiquity-of-delta-standalone-java-scala-hive-presto-trino-power-bi-and-more.html): a JVM library that can be used to read and write Delta Lake tables. Unlike Delta Lake Core, this project does not use Spark to read or write tables and has only a few transitive dependencies. It can be used by any application (e.g. Power BI) that cannot use a Spark cluster. The project allows developers to build a Delta connector for an external processing engine following the Delta protocol without using a manifest file. 

### Delta Sharing
- [GitHub repository](https://github.com/delta-io/delta-sharing)
- [Release Milestones](https://github.com/delta-io/delta-sharing/milestones)
- [▶️ Databricks Delta Sharing demo](https://www.youtube.com/watch?v=wRT1Vpbyy88)
- [Arcuate](https://databricks.com/blog/2022/05/24/arcuate-machine-learning-model-exchange-with-delta-sharing-and-mlflow.html): Machine Learning Model Exchange With Delta Sharing and MLflow
- [Java connector](https://github.com/databrickslabs/delta-sharing-java-connector)(supporting [blog post](https://databricks.com/blog/2022/06/29/designing-a-java-connector-for-delta-sharing-recipient.html))
- [Security Best Practices for Delta Sharing](https://www.databricks.com/blog/2022/08/01/security-best-practices-for-delta-sharing.html)
- [How Delta Sharing Helped Rearc Simplify Data Sharing and Maximize the Business Value of Its Data](https://www.databricks.com/blog/2022/09/13/how-delta-sharing-helped-rearc-simplify-data-sharing-and-maximize-business-value): With over 450+ open curated data products available across different sectors, Rearc's cross-industry catalog of datasets is one of the largest available today ([Rearc data library](https://www.rearc.io/data/delta-sharing/))

---

## ETL / ELT Patterns
### Design
- [Identity Columns to Generate Surrogate Keys](https://www.databricks.com/blog/2022/08/08/identity-columns-to-generate-surrogate-keys-are-now-available-in-a-lakehouse-near-you.html)

### Ingestion
- [Auto-Loader](https://docs.databricks.com/spark/latest/structured-streaming/auto-loader.html)
- [dbt](https://docs.databricks.com/dev-tools/dbt.html) ([GitHub](https://github.com/databricks/dbt-databricks))
- [Build Data and ML Pipelines More Easily With Databricks and Apache Airflow](https://databricks.com/blog/2022/04/29/build-data-and-ml-pipelines-more-easily-with-databricks-and-apache-airflow.html)

### Ingestion: Streaming
- [Simplifying Streaming Data Ingestion into Delta Lake](https://www.databricks.com/blog/2022/09/12/simplifying-streaming-data-ingestion-delta-lake.html)
- [Speed Up Streaming Queries With Asynchronous State Checkpointing](https://databricks.com/blog/2022/05/02/speed-up-streaming-queries-with-asynchronous-state-checkpointing.html)
- [Feature Deep Dive: Watermarking in Apache Spark Structured Streaming](https://www.databricks.com/blog/2022/08/22/feature-deep-dive-watermarking-in-apache-spark-structured-streaming.html)
- [Python Arbitrary Stateful Processing in Structured Streaming](https://www.databricks.com/blog/2022/10/18/python-arbitrary-stateful-processing-structured-streaming.html)
- Monitoring streaming queries ([PySpark](https://www.databricks.com/blog/2022/05/27/how-to-monitor-streaming-queries-in-pyspark.html) | [Scala](https://docs.databricks.com/structured-streaming/stream-monitoring.html#language-scala))
- [Using Spark Structured Streaming to Scale Your Analytics](https://www.databricks.com/blog/2022/07/14/using-spark-structured-streaming-to-scale-your-analytics.html)
- [State Rebalancing in Structured Streaming](https://www.databricks.com/blog/2022/10/04/state-rebalancing-structured-streaming.html)
- [▶️ Streaming data into the Lakehouse](https://www.youtube.com/watch?v=FFVH7G9iN68)
- [Simplifying Streaming Data Ingestion into Delta Lake](https://www.databricks.com/blog/2022/09/12/simplifying-streaming-data-ingestion-delta-lake.html)
![High level view of streaming data ingestion into delta lake](https://cms.databricks.com/sites/default/files/inline-images/db-265-blog-img-1.png)
- Roadmap: [Project Lightspeed: Faster and Simpler Stream Processing With Apache Spark](https://www.databricks.com/blog/2022/06/28/project-lightspeed-faster-and-simpler-stream-processing-with-apache-spark.html)
- [Debugging using the Structured Streaming UI](https://www.databricks.com/blog/2020/07/29/a-look-at-the-new-structured-streaming-ui-in-apache-spark-3-0.html) ([Spark docs](https://spark.apache.org/docs/latest/web-ui.html#structured-streaming-tab))
- [Confluent Streaming for Databricks: Build Scalable Real-time Applications on the Lakehouse (Part I)](https://databricks.com/blog/2022/01/13/confluent-streaming-for-databricks-build-scalable-real-time-applications-on-the-lakehouse.html) [(Part II)](https://databricks.com/blog/2022/05/17/build-scalable-real-time-applications-on-the-lakehouse-using-confluent-databricks-part-2.html)

### Delta Live Tables (DLT)
- [Delta Live Tables Cookbook](https://docs.databricks.com/data-engineering/delta-live-tables/delta-live-tables-cookbook.html)
- [Delta Live Tables Notebooks](https://github.com/databricks/delta-live-tables-notebooks)
- [Dimensional modeling implementation on the modern lakehouse using Delta Live Tables](https://www.databricks.com/blog/2022/11/07/load-edw-dimensional-model-real-time-databricks-lakehouse.html)
- [Deloitte’s Guide to Declarative Data Pipelines With Delta Live Tables](https://www.databricks.com/blog/2022/10/19/deloittes-guide-declarative-data-pipelines-delta-live-tables.html) ([Whitepaper](https://www.databricks.com/wp-content/uploads/2022/10/deloitte-delta-live-tables-databricks-white-paper.pdf))
![Deloitte's view on Delta Live Tables](https://cms.databricks.com/sites/default/files/inline-images/db-355-blog-img-1.png)
- [Build a Customer 360 Solution with Fivetran and Delta Live Tables](https://www.databricks.com/blog/2022/11/09/build-customer-360-solution-fivetran-and-delta-live-tables.html) - includes SCD2 example
- [Simplifying Change Data Capture With Databricks Delta Live Tables](https://databricks.com/blog/2022/04/25/simplifying-change-data-capture-with-databricks-delta-live-tables.html)
- [Delivering Real-Time Data to Retailers with Delta Live Tables](https://databricks.com/blog/2022/04/12/delivering-real-time-data-to-retailers-with-delta-live-tables.html) (fully documented [notebooks](https://d1r5llqwmkrl74.cloudfront.net/notebooks/RCG/POS_DLT/index.html#POS_DLT_1.html))
- [Building ETL pipelines for the cybersecurity lakehouse with Delta Live Tables](https://databricks.com/blog/2022/06/03/building-etl-pipelines-for-the-cybersecurity-lakehouse-with-delta-live-tables.html): ingest & evaluate AWS CloudTrail & VPC Flow logs (accompanying notebooks: [CloudTrail DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/cloudtrail-dlt-pipeline.html), [VPC Flow Logs DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/vpc-flow-logs-dlt-pipeline.html), [Zeek DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/zeek-dlt-pipeline.html))
- [Low-latency Streaming Data Pipelines with Delta Live Tables and Apache Kafka](https://www.databricks.com/blog/2022/08/09/low-latency-streaming-data-pipelines-with-delta-live-tables-and-apache-kafka.html)
- [▶️ Apache Kafka and Delta Live Tables](https://www.youtube.com/watch?v=ntbs0uwPvxY)
- [How I Built A Streaming Analytics App With SQL and Delta Live Tables](https://databricks.com/blog/2022/05/19/how-i-built-a-streaming-analytics-app-with-sql-and-delta-live-tables.html): accompanying [repo](https://github.com/databricks/delta-live-tables-notebooks/tree/main/divvy-bike-demo)
- [How Uplift built CDC and Multiplexing data pipelines with Databricks Delta Live Tables](https://databricks.com/blog/2022/04/27/how-uplift-built-cdc-and-multiplexing-data-pipelines-with-databricks-delta-live-tables.html)
- [Near Real-Time Anomaly Detection with Delta Live Tables and Databricks Machine Learning](https://www.databricks.com/blog/2022/08/08/near-real-time-anomaly-detection-with-delta-live-tables-and-databricks-machine-learning.html)
- [How Audantic Uses Databricks Delta Live Tables to Increase Productivity for Real Estate Market Segments](https://databricks.com/blog/2022/05/05/how-audantic-uses-databricks-delta-live-tables-to-increase-productivity-for-real-estate-market-segments.html)
![Audantic's Delta Live Tables Architecture](https://databricks.com/wp-content/uploads/2022/04/db-80-blog-img-2.png)

### Transformation
- [`dbt-databricks`](https://github.com/databricks/dbt-databricks)
- [Faster MERGE Performance With Low-Shuffle MERGE and Photon](https://www.databricks.com/blog/2022/10/17/faster-merge-performance-low-shuffle-merge-and-photon.html)

---
## Development
- [SQL CLI](https://docs.databricks.com/dev-tools/databricks-sql-cli.html): run SQL queries on your SQL endpoints from your terminal. From the command line, you get productivity features such as suggestions and syntax highlighting
- [sqlparse](https://github.com/andialbrecht/sqlparse): open source library for formatting and analysing SQL strings

---

## Orchestration
### Databricks Workflows
- [Save Time and Money on Data and ML Workflows With “Repair and Rerun”](https://databricks.com/blog/2022/05/06/save-time-and-money-on-data-and-ml-workflows-with-repair-and-rerun.html)

---
## DataOps
- [Use an IDE with Databricks](https://docs.databricks.com/dev-tools/ide-how-to.html#set-up-the-code-sample)
- [Software engineering best practices for notebooks](https://docs.databricks.com/notebooks/best-practices.html) ([accompanying notebooks](https://github.com/databricks/notebook-best-practices)) ([accompanying notebooks](https://github.com/databricks/ide-best-practices))
- [Build Reliable Production Data and ML Pipelines With Git Support for Databricks Workflows](https://databricks.com/blog/2022/06/21/build-reliable-production-data-and-ml-pipelines-with-git-support-for-databricks-workflows.html) ([📄 notebooks](https://github.com/RafiKurlansik/e2e-cuj))


### GitHub
- [GitHub Marketplace: Databricks](https://github.com/marketplace?query=databricks+publisher%3Adatabricks+)
- [GitHub Actions documentation](https://docs.databricks.com/dev-tools/ci-cd/ci-cd-github.html)

---

## Analysis

### Analyst Experience
- [▶️ Low-Code Exploratory Data Analysis with Bamboolib](https://www.youtube.com/watch?v=VC9LxBwaPFw)

---

## Best Practices
- [7 best practices to modernize data architecture on Databricks with LeapLogic](https://www.leaplogic.io/modernization/blog/cloud-engineering-data-engineering-etl-and-analytics-migration-ml-analytics-ai/7-best-practices-modernizing-data-architecture-databricks-lakehouse)

### Performance tuning
- [Delta Lake best practices](https://docs.databricks.com/delta/best-practices.html)
- [Optimize performance with file management](https://docs.databricks.com/delta/optimizations/file-mgmt.html)
- [Make Your Data Lakehouse Run, Faster With Delta Lake 1.1](https://databricks.com/blog/2022/01/31/make-your-data-lakehouse-run-faster-with-delta-lake-1-1.html)
- [Get to Know Your Queries With the New Databricks SQL Query Profile](https://databricks.com/blog/2022/02/23/get-to-know-your-queries-with-the-new-databricks-sql-query-profile.html)
- [Top 5 Performance Tips](https://databricks.com/blog/2022/03/10/top-5-databricks-performance-tips.html)
- [How to consistently get the best performance from star schema databases](https://databricks.com/blog/2022/05/20/five-simple-steps-for-implementing-a-star-schema-in-databricks-with-delta-lake.html)
- [Faster insights With Databricks Photon Using AWS i4i Instances With the Latest Intel Ice Lake Scalable Processors](https://www.databricks.com/blog/2022/09/13/faster-insights-databricks-photon-using-aws-i4i-instances-latest-intel-ice-lake): Up to 2.5x price/performance benefits and 5.3x speed up!
![2.5x relative price-performance improvement of i4i Photon](https://cms.databricks.com/sites/default/files/inline-images/db-325-blog-img-3.png)
- [Improved Performance and Value With Databricks Photon and Azure Lasv3 Instances Using AMD 3rd Gen EPYC™ 7763v Processors](https://www.databricks.com/blog/2022/10/11/improved-performance-and-value-databricks-photon-and-azure-lasv3-instances-using): Up to 2.5x price/performance benefits and 5.3x speed up!
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
    - Coalescing post-shuffle partitions (combine small partitions into reasonably sized partitions)
    - Converting sort-merge joins to broadcast hash joins
    - Skew join optimisation by splitting (and replicating if needed) skewed tasks into roughly evenly sized tasks
    - Dynamically detects and propagates empty relations
- `ANALYZE TABLE` collects table statistics that allows AQE to know which plan to choose for you

---

## Machine Learning (ML) & Artificial Intelligence (AI) 🧠
- [Selecting an Effective & Productive Machine Learning Platform](https://alexanderkwok17.medium.com/selecting-an-effective-productive-machine-learning-platform-8b7d7efa3d4f)

### MLOps
- [Architecting MLOps on the Lakehouse](https://databricks.com/blog/2022/06/22/architecting-mlops-on-the-lakehouse.html)

### MLflow
- [▶️ MLflow YouTube channel](https://www.youtube.com/channel/UC5d6sLKbZahYMaAHgeYmoAg)
- [Cross-version Testing in MLflow](https://databricks.com/blog/2022/03/11/cross-version-testing-in-mlflow.html): MLflow integrates with several popular ML frameworks. See how the Databricks Engineering team proactively adapt MLflow and third-party libraries to prevent against breaking changes
- [Model Evaluation in MLflow](https://databricks.com/blog/2022/04/19/model-evaluation-in-mlflow.html)

### Feature Store
- [eBook: The Comprehensive Guide to Feature Stores](https://databricks.com/wp-content/uploads/2022/03/The-Comprehensive-Guide-to-Feature-Stores.pdf) (Mar 2022)

### Distributed Training
- [How (Not) To Scale Deep Learning in 6 Easy Steps](https://www.databricks.com/blog/2019/08/15/how-not-to-scale-deep-learning-in-6-easy-steps.html)
- [Accelerating Your Deep Learning with PyTorch Lightning on Databricks](https://www.databricks.com/blog/2022/09/07/accelerating-your-deep-learning-pytorch-lightning-databricks.html)
- [▶️ Scaling Deep Learning on Databricks](https://www.youtube.com/watch?v=A95_q24nA1o)
- [Rapid NLP Development With Databricks, Delta, and Transformers](https://www.databricks.com/blog/2022/09/09/rapid-nlp-development-databricks-delta-and-transformers.html)
- [Mitigating Bias in Machine Learning With SHAP and Fairlearn](https://www.databricks.com/blog/2022/09/16/mitigating-bias-machine-learning-shap-and-fairlearn.html)([accompanying 📄 notebook](https://www.databricks.com/wp-content/uploads/notebooks/db-336-mitigating_bias_with_shap_fairlearn-blog.html))
- [Parallel ML: How Compass Built a Framework for Training Many Machine Learning Models](https://www.databricks.com/blog/2022/07/20/parallel-ml-how-compass-built-a-framework-for-training-many-machine-learning-models-on-databricks.html)

### Predictions
- [Near Real-Time Anomaly Detection with Delta Live Tables and Databricks Machine Learning](https://www.databricks.com/blog/2022/08/08/near-real-time-anomaly-detection-with-delta-live-tables-and-databricks-machine-learning.html)

### Guides
- [Getting Started with Personalization through Propensity Scoring](https://databricks.com/blog/2022/06/03/getting-started-with-personalization-through-propensity-scoring.html) (accompanying [notebooks](https://d1r5llqwmkrl74.cloudfront.net/notebooks/nightly/RCG/Propensity/index.html#Propensity_1.html))
- [Using MLflow to deploy Graph Neural Networks for Monitoring Supply Chain Risk](https://medium.com/@ajmal.t.aziz/using-mlflow-to-deploy-graph-neural-networks-for-monitoring-supply-chain-risk-644c87e5259e)
- [Quantifying uncertainty with Tensorflow Probability](https://databricks.com/blog/2022/04/28/how-wrong-is-your-model.html)

---

## Geospatial 🌏
- [Mosaic](https://databrickslabs.github.io/mosaic/): a Databricks Labs extension to the Apache Spark framework that allows easy and fast processing of very large geospatial datasets 
- [GitHub: Mosaic](https://github.com/databrickslabs/mosaic)
- [Building a Geospatial Lakehouse, Part 1](https://databricks.com/blog/2021/12/17/building-a-geospatial-lakehouse-part-1.html)
- [Building a Geospatial Lakehouse, Part 2](https://databricks.com/blog/2022/03/28/building-a-geospatial-lakehouse-part-2.html): includes downloadable notebooks
- [High Scale Geospatial Processing With Mosaic](https://databricks.com/blog/2022/05/02/high-scale-geospatial-processing-with-mosaic.html): writeup on the underlying philosophy behind Mosaic's design
- [Built-in H3 Expressions for Geospatial Processing and Analytics](https://www.databricks.com/blog/2022/09/14/announcing-built-h3-expressions-geospatial-processing-and-analytics.html)
- [How Thasos Optimized and Scaled Geospatial Workloads with Mosaic on Databricks](https://www.databricks.com/blog/2022/10/12/how-thasos-optimized-and-scaled-geospatial-workloads-mosaic-databricks.html): Thasos is an alternative data intelligence firm that transforms real-time location data from mobile phones into actionable business performance insights. To derive actionable insights from mobile phone ping data (a time series of points defined by a latitude and longitude pair), Thasos created, maintains and manages a vast collection of verified geofences
![Geofence polygons from Figure 1 showing contained H3 cells (in red) and the derived boundary chips (in blue)](https://cms.databricks.com/sites/default/files/inline-images/db-328-blog-img-2.jpg)

---

## Use Cases
### App Dev
- [Taming JavaScript Exceptions With Databricks](https://databricks.com/blog/2022/01/25/taming-javascript-exceptions-with-databricks.html)

### Customer Data
- [Customer Entity Resolution](https://www.databricks.com/blog/2022/08/04/new-solution-accelerator-customer-entity-resolution.html) ([Solution Accelerator page](https://www.databricks.com/solutions/accelerators/customer-entity-resolution) | [Notebooks](https://d1r5llqwmkrl74.cloudfront.net/notebooks/nightly/RCG/Customer_ER/index.html))
- [The Emergence of the Composable Customer Data Platform](https://databricks.com/blog/2022/06/24/the-emergence-of-the-composable-customer-data-platform.html)

### Cybersecurity 🔐
- [Hunting for IOCs Without Knowing Table Names or Field Labels](https://databricks.com/blog/2022/07/15/hunting-for-iocs-without-knowing-table-names-or-field-labels.html)
- [Hunting Anomalous Connections and Infrastructure With TLS Certificates: TLS hashes as a source for the cybersecurity threat hunting program](https://databricks.com/blog/2022/01/20/hunting-anomalous-connections-and-infrastructure-with-tls-certificates.html)
- [Cybersecurity in the Era of Multiple Clouds and Regions](https://www.databricks.com/blog/2022/08/30/cybersecurity-era-multiple-clouds-and-regions.html)
- [Building ETL pipelines for the cybersecurity lakehouse with Delta Live Tables](https://databricks.com/blog/2022/06/03/building-etl-pipelines-for-the-cybersecurity-lakehouse-with-delta-live-tables.html): ingest & evaluate AWS CloudTrail & VPC Flow logs (accompanying notebooks: [CloudTrail DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/cloudtrail-dlt-pipeline.html), [VPC Flow Logs DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/vpc-flow-logs-dlt-pipeline.html), [Zeek DLT pipeline](https://databricks.com/wp-content/uploads/notebooks/db-172-dlt/zeek-dlt-pipeline.html))
- [Learn how to connect Databricks to Okta to ingest System Logs, retain, and analyze for complete visibility using your Databricks Lakehouse Platform](https://databricks.com/blog/2022/04/07/analyzing-okta-logs-with-databricks-lakehouse-platform-to-detect-unusual-activity.html) (accompanying [notebooks](https://databricks.com/wp-content/uploads/notebooks/db-134-okta-logs/index.html#1_okta_create_table.html))
- [Streaming Windows Event Logs into the Cybersecurity Lakehouse](https://databricks.com/blog/2022/05/05/streaming-windows-event-logs-into-the-cybersecurity-lakehouse.html) ([notebook](https://github.com/DerekKing001/databricks_cyber_notebooks/blob/master/winlogbeats-kafka-sysmon/winlogbeats-kafka-sysmon-example.py))
- [Building a Cybersecurity Lakehouse for CrowdStrike Falcon Events Part I](https://databricks.com/blog/2021/05/20/building-a-cybersecurity-lakehouse-for-crowdstrike-falcon-events.html), [Part II](https://databricks.com/blog/2022/07/19/building-a-cybersecurity-lakehouse-for-crowdstrike-falcon-events-part-ii.html)

### ERP
- [How Organizations Can Extract the Full Potential of SAP Data with a Lakehouse](https://www.databricks.com/blog/2022/09/20/how-organizations-can-extract-full-potential-sap-data-lakehouse.html)

### Marketing Analytics
- [How to Build a Marketing Analytics Solution Using Fivetran and dbt on the Databricks Lakehouse](https://www.databricks.com/blog/2022/08/03/how-to-build-a-marketing-analytics-solution-using-fivetran-and-dbt-on-the-databricks-lakehouse.html)

---

## Tools 🛠
- [dbx](https://github.com/databrickslabs/dbx): DataBricks CLI eXtensions - aka `dbx` is a CLI tool for advanced Databricks jobs management

---

## End-to-end Guides
- [Exploration of Twitter sentiment impact on cryptocurrency price](https://databricks.com/blog/2022/05/02/introduction-to-analyzing-crypto-data-using-databricks.html)

---

## Case Studies
- [Monash University stands up 'lakehouse' in Databricks, Azure](https://www.itnews.com.au/news/monash-university-stands-up-lakehouse-in-databricks-azure-585801)
- [Australia's heavy vehicle regulator builds 'fatigue engine' to reduce truckie deaths](https://www.itnews.com.au/news/heavy-vehicle-regulator-builds-fatigue-engine-to-reduce-truckie-deaths-580113)
- [Why we migrated to a Data Lakehouse on Delta Lake for T-Mobile Data Science and Analytics Team](https://delta.io/blog/2022-09-14-why-migrate-lakehouse-delta-lake-tmo-dsna/)

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