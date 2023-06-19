# YYYY-MM-DD

Hi team! I just wanted to share some of the interesting resources/articles that have come from Databricks in the last couple of weeks:

## 🎓 Events, Training & Education

- The [Databricks Data+AI Summit](https://dbricks.co/45EV2yI) is just around the corner! Kicking off on Wed 28th (AEST), it promises a lot of exciting announcements around LLMs, ML- and LLM-Ops, data engineering, and SQL goodness. If you haven't already, you can [register for free here](https://dbricks.co/45EV2yI). Recordings will be available shortly after on-demand.

- For those of you who missed our Roadmap session earlier this week, I'm happy to go over the highlights with you, or you can [watch a recording in the Databricks Academy](https://customer-academy.databricks.com/learn/course/internal/view/elearning/861/databricks-product-roadmap-webinars) (select _FY24Q2 Product Roadmap Webinar - All Clouds_)

- [Now Available: **New Generative AI Learning** Offerings](https://www.databricks.com/blog/now-available-new-generative-ai-learning-offerings) in Databricks Academy! This is similar content to the [Databricks LLM courses on edX](https://www.edx.org/professional-certificate/databricks-large-language-models), but also giving you the ability to download the teaching slides and notebooks. Sign up to the [first course here](https://customer-academy.databricks.com/learn/course/internal/view/elearning/1749/large-language-models-llms-application-through-production)
  - If you don't already have access to the Databricks Academy, sign up with your work e-mail address to gain immediate free access

## 🧠 ML & AI

- [Announcing MLflow 2.4: LLMOps Tools for Robust Model Evaluation](https://www.databricks.com/blog/announcing-mlflow-24-llmops-tools-robust-model-evaluation)
  - the new **Artifact View** in MLflow Tracking simplifies comparing the performance of LLMs across different runs. This data can be downloaded for further analysis, data labeling, etc.
  ![The MLflow Artifact View provides a side-by-side comparison of inputs, outputs, and intermediate results across multiple models](https://www.databricks.com/sites/default/files/inline-images/screenshot_2023-06-07_at_11.46.21_am.png)
  - **Dataset Tracking**, integrated with Autologging, allows you to quickly identify which datasets were used to develop and evaluate each of your models, ensuring fair comparison and simplifying model selection for production deployment
  ![MLflow Tracking now displays comprehensive dataset information in the UI with enhanced visibility into dataset metadata for each run. With the introduction of a new panel, you can easily visualize and explore the details of datasets, conveniently accessible from both the runs comparison view and the runs detail page](https://www.databricks.com/sites/default/files/inline-images/image2_0.png)

- [LLM Model Recommendations](https://www.databricks.com/product/machine-learning/large-language-models-oss-guidance): we often get asked what are the best OSS LLM models to use for which use case. This frequently-updated matrix is a handy reference to identify the right models by use case and depending on whether you are seeking quality-, balanced-, or speed-optimised models

## 🛒 Retail

- [Unlocking the Power of Retail Media Networks: How Data-Driven Advertising is Changing the Retail Promotions Landscape](https://www.databricks.com/blog/unlocking-power-retail-media-networks-how-data-driven-advertising-changing-retail-promotions)

## 😎 User Experience

- [Easy Ingestion to Lakehouse with File Upload and Add Data UI](https://www.databricks.com/blog/easy-ingestion-lakehouse-file-upload-and-add-data-ui)

## 🛠️ Developer Experience

- [What’s New with Databricks Notebooks](https://www.databricks.com/blog/2023/06/16/whats-new-with-databricks-notebooks). Some of my favourite highlights:
  - Run notebooks on SQL Warehouses: SQL warehouses are the same resources that power Databricks SQL, and they deliver better price-performance for SQL execution compared to all-purpose clusters
  - Debug your Notebooks with the Variable Explorer: also allows you to step through and debug Python code by leveraging the support for pdb in Databricks Notebooks. You can set breakpoints with `breakpoint()` or `pdb.set_trace()`
  - Share Notebooks using Delta Sharing: Sharing notebooks empowers you to collaborate across metastores and accounts. This enables people who share data to unpack the value of that data with notebooks

- [▶️ Databricks Connect + Spark Connect: How you can build on Spark from anywhere](https://www.youtube.com/watch?v=Cwj-L8sQRGc): _"Databricks Connect v2 leverages Spark Connect so you can connect to your Spark clusters within Databricks"_

- [Debug your code and notebooks by using Visual Studio Code](https://www.databricks.com/blog/debug-your-code-and-notebooks-using-visual-studio-code)
  - Interactive debugging with Databricks Connect: developers can step through their code and inspect variables in real time. Databricks Connect enables running Spark code on remote clusters from the IDE, thereby enabling code step-through while debugging
  - Support for `ipynb` notebooks
  - Support for `dbutils` and Spark SQL

## 🪛 Data Engineering

- [Unifying Your Data Ecosystem with Delta Lake Integration](https://www.databricks.com/blog/integrating-delta-lakehouse-other-platforms): a useful walkthrough of options (direct cloud storage access, external hive metastore, delta sharing, JDBC/ODBC)for when you need to read/write data from/to different systems and applications
    ![Unifying Your Data Ecosystem with Delta Lake Integration](https://cms.databricks.com/sites/default/files/inline-images/db-580-blog-image-5.png)

- The [Google **Pub/Sub connector**](https://docs.gcp.databricks.com/structured-streaming/pub-sub.html) is now live! Ingest messages from Pub/Sub, with exactly-once semantics, using Structured Streaming from any cloud (requires DBR 13.1+) ([accompanying blog post](https://www.databricks.com/blog/unlock-power-real-time-data-processing-databricks-and-google-cloud))

- An [updated primer on Orchestration with Databricks Worfklows](https://www.databricks.com/blog/lakehouse-orchestration-databricks-workflows)

## 📊 Data Analysis / SQL

- For Power BI users, we have a new set of guides on optimising dashboard performance:
  - [Power Up your BI with Microsoft Power BI and Lakehouse in Azure Databricks: part 1 - Essentials](https://techcommunity.microsoft.com/t5/analytics-on-azure-blog/power-up-your-bi-with-microsoft-power-bi-and-lakehouse-in-azure/ba-p/3810649)
  - [Power Up your BI with Microsoft Power BI and Lakehouse in Azure Databricks: part 2 - Tuning Power BI](https://techcommunity.microsoft.com/t5/analytics-on-azure-blog/power-up-with-power-bi-and-lakehouse-in-azure-databricks-part-3/ba-p/3825010)
  - [Power Up with Power BI and Lakehouse in Azure Databricks: part 3 - Tuning Azure Databricks SQL](https://techcommunity.microsoft.com/t5/analytics-on-azure-blog/power-up-with-power-bi-and-lakehouse-in-azure-databricks-part-3/ba-p/3825010)

## 🛠️ Architecture

- [Multi-cloud Architecture for Portable Data and AI Processing in Financial Services](https://www.databricks.com/blog/multi-cloud-architecture-portable-data-and-ai-processing-financial-services): a useful blueprint for owning a reliable and governed **multi-cloud data architecture**. Although this article is focused on the financial services industry, it is relevant for any organisations with data footprints across clouds

## ⚡️ Performance Optimisation

- [Adaptive Query Execution in Structured Streaming](https://www.databricks.com/blog/adaptive-query-execution-structured-streaming): as part of [Project Lightspeed](https://www.databricks.com/blog/2022/06/28/project-lightspeed-faster-and-simpler-stream-processing-with-apache-spark.html), AQE is applied to `ForeachBatch` to speed up transformation operations, leading to 1.2x-2.87x performance gains

## 🏪 Databricks Marketplace

- [▶️ Introduction to Databricks Marketplace](https://www.youtube.com/watch?v=PGgWOw7g0lM): a short primer on Databricks Marketplace by our partners Advancing Analytics

## 🥂 Customer Stories

- [How **Stack Overflow** built their new course recommendations](https://stackoverflow.blog/2023/05/29/more-on-our-ai-future-building-course-recommendations-and-a-new-data-platform/) solution on Azure Databricks. I think it's safe to say we all owe Stack Overflow some thanks for aiding us in our technical careers; so I was happy to see Databricks play a role in helping the community discover relevant courses. *"[It was] clear that leveraging one platform for as much as possible would be wise, and our platform of choice was Azure Databricks. This allowed us to keep all data processing, feature engineering, model versioning, serving, and orchestration all in one place."*

- [How Instacart Ads Modularized Data Pipelines With Lakehouse Architecture and Spark](https://tech.instacart.com/how-instacart-ads-modularized-data-pipelines-with-lakehouse-architecture-and-spark-e9863e28488d)

- [Ahold Delhaize: Workflows helps data teams scale and reduce costs](https://www.databricks.com/customers/ahold-delhaize): 1K daily ingestion jobs with 50% cost reduction


As always, please let me know if you'd like to find out more about any of the announcements or use cases above 👆🏽