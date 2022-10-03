# Delta Lake: From Data Lake to Lakehouse

## Follow Along
- [🌟 **Recommended**: View pre-executed notebook and outputs](https://vinoaj.github.io/databricks-resources/presentations/dataengconf_syd_20220929/DataEngBytes-Delta-Lake-Demo.html)
- [Notebook](DataEngBytes-Delta-Lake-Demo.py)

## Recording
[▶️ Watch here](https://youtu.be/k6IEaMF7U7A?t=22131) 

[![Watch recording](https://img.youtube.com/vi/k6IEaMF7U7A/mqdefault.jpg)](https://youtu.be/k6IEaMF7U7A?t=22131)

## About

These assets are prepared for [my talk](https://dataengconf.com.au/conference/schedule) at the [**DataEngBytes** conference](https://dataengconf.com.au/conference/sydney) held on 2022-09-29 in Sydney, Australia.

- Author: [Vinoaj (Vinny) Vijeyakumaar](https://github.com/vinoaj) ([LinkedIn](https://www.linkedin.com/in/vinoaj))
- _Opinions are my own and not necessarily the views of my employer_


### The Data

The data used in this demo is from the Kaggle competition [`predict-closed-questions-on-stack-overflow`](https://www.kaggle.com/competitions/predict-closed-questions-on-stack-overflow/overview).


### The Environment
This notebook is setup to run in a Databricks Workspace. Databricks clusters are already set up with Spark, Delta Lake, their respective SDKs (e.g. `PySpark`), and configured to interoperate with each other. This notebook was developed using **DBR 11.2** (_Spark 3.3.0_)

To set up Delta Lake in a non-Databricks environment, please [follow these instructions](https://docs.delta.io/latest/quick-start.html)

---

# Upcoming Databricks Events ... Join Us!
## (Free & in-person!) Data+AI World Tour Sydney
![Data+AI World Tour Sydney](../../assets/img/data_ai_world_tour_sydney.png)

[🔗 Registration link](https://www.databricks.com/dataaisummit/worldtour/sydney)

Our lineup of data and AI experts, leaders and visionaries includes [Matei Zaharia](https://www.linkedin.com/in/mateizaharia), co-founder Apache Spark and Databricks. 

Come spend the day with Lakehouse experts and practitioners from across Australia and New Zealand. Learn howlocal entrprises and startups are pushing the Lakehouse boundaries!

## (Free & in-person!) Databricks Bootcamps
[🔗 Registration link](https://pages.databricks.com/00-202202-APJ-FE-Databricks-Bootcamp-2022-q4-Router_LP---Registration-page.html?utm_source=databricks&utm_medium=vinny&utm_campaign=7013f000000LkDCAA0)

We're holding **free** Databricks Bootcamps across Brisbane, Sydney, Melbourne, Adelaide, Perth, and Auckland over Oct - Dec.

Led by Databricks instructors, these sessions will use real-world data sets as we go under the hood to demonstrate how to use robust technologies such as Delta Lake, Databricks SQL and MLflow

---

<img src="https://docs.delta.io/latest/_static/delta-lake-white.png" width="100" alt="Delta Lake Logo"></img>
# Further Reading & Resources

## Understand the fundamentals
- [Delta Lake VLDB paper](https://databricks.com/wp-content/uploads/2020/08/p975-armbrust.pdf) (my [annotated version](../../assets/p975-armbrust_vinoaj_annotated.pdf))
- 📘 Delta Lake: The Definitive Guide (O'Reilly) ([access free preview](https://www.databricks.com/p/ebook/delta-lake-the-definitive-guide-by-oreilly) | [PDF direct link](https://www.databricks.com/wp-content/uploads/2021/05/9781098104528-1.pdf))

## Further reading 
- [Roadmap](https://github.com/delta-io/delta/issues/1307)
- [Releases](https://github.com/delta-io/delta/releases)
- [Release Milestones](https://github.com/delta-io/delta/milestones)
- [Delta Transactional Log Protocol](https://github.com/delta-io/delta/blob/master/PROTOCOL.md)
- [Diving Into Delta Lake: Unpacking The Transaction Log](https://www.databricks.com/blog/2019/08/21/diving-into-delta-lake-unpacking-the-transaction-log.html)
- [Diving Into Delta Lake: Schema Enforcement & Evolution](https://www.databricks.com/blog/2019/09/24/diving-into-delta-lake-schema-enforcement-evolution.html)
- [Diving Into Delta Lake: DML Internals (Update, Delete, Merge)](https://www.databricks.com/blog/2020/09/29/diving-into-delta-lake-dml-internals-update-delete-merge.html)
- [Processing Petabytes of Data in Seconds with Databricks Delta](https://www.databricks.com/blog/2018/07/31/processing-petabytes-of-data-in-seconds-with-databricks-delta.html)
- [Top 5 Reasons to Convert Your Cloud Data Lake to a Delta Lake](https://databricks.com/blog/2020/08/21/top-5-reasons-to-convert-your-cloud-data-lake-to-a-delta-lake.html)
- [TPC-DS Benchmarking guide](https://github.com/delta-io/delta/tree/master/benchmarks)
- [The Ubiquity of Delta Standalone](https://databricks.com/blog/2022/01/28/the-ubiquity-of-delta-standalone-java-scala-hive-presto-trino-power-bi-and-more.html): a JVM library that can be used to read and write Delta Lake tables. Unlike Delta Lake Core, this project does not use Spark to read or write tables and has only a few transitive dependencies. It can be used by any application (e.g. Power BI) that cannot use a Spark cluster. The project allows developers to build a Delta connector for an external processing engine following the Delta protocol without using a manifest file. 