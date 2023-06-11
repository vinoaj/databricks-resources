# YYYY-MM-DD

Hi team! I just wanted to share some of the interesting resources/articles that have come from Databricks in the last couple of weeks:

## 🧠 ML & AI

- [Announcing MLflow 2.4: LLMOps Tools for Robust Model Evaluation](https://www.databricks.com/blog/announcing-mlflow-24-llmops-tools-robust-model-evaluation)
  - the new **Artifact View** in MLflow Tracking simplifies comparing the performance of LLMs across different runs. This data can be downloaded for further analysis, data labeling, etc.
  ![The MLflow Artifact View provides a side-by-side comparison of inputs, outputs, and intermediate results across multiple models](https://www.databricks.com/sites/default/files/inline-images/screenshot_2023-06-07_at_11.46.21_am.png)
  - **Dataset Tracking**, integrated with Autologging, allows you to quickly identify which datasets were used to develop and evaluate each of your models, ensuring fair comparison and simplifying model selection for production deployment
  ![MLflow Tracking now displays comprehensive dataset information in the UI with enhanced visibility into dataset metadata for each run. With the introduction of a new panel, you can easily visualize and explore the details of datasets, conveniently accessible from both the runs comparison view and the runs detail page](https://www.databricks.com/sites/default/files/inline-images/image2_0.png)

## 🛒 Retail

- [Unlocking the Power of Retail Media Networks: How Data-Driven Advertising is Changing the Retail Promotions Landscape](https://www.databricks.com/blog/unlocking-power-retail-media-networks-how-data-driven-advertising-changing-retail-promotions)

## 🎓 Training & Education

- [Now Available: **New Generative AI Learning** Offerings](https://www.databricks.com/blog/now-available-new-generative-ai-learning-offerings) in Databricks Academy! This is similar content to the [Databricks LLM courses on edX](https://www.edx.org/professional-certificate/databricks-large-language-models), but also giving you the ability to download the teaching slides and notebooks. Sign up to the [first course here](https://customer-academy.databricks.com/learn/course/internal/view/elearning/1749/large-language-models-llms-application-through-production)
  - If you don't already have access to the Databricks Academy, sign up with your work e-mail address to gain immediate free access

## 😎 User Experience

- [Easy Ingestion to Lakehouse with File Upload and Add Data UI](https://www.databricks.com/blog/easy-ingestion-lakehouse-file-upload-and-add-data-ui)

## 🛠️ Developer Experience


## 🪛 Data Engineering

- [Unifying Your Data Ecosystem with Delta Lake Integration](https://www.databricks.com/blog/integrating-delta-lakehouse-other-platforms): a useful walkthrough of options (direct cloud storage access, external hive metastore, delta sharing, JDBC/ODBC)for when you need to read/write data from/to different systems and applications
    ![Unifying Your Data Ecosystem with Delta Lake Integration](https://cms.databricks.com/sites/default/files/inline-images/db-580-blog-image-5.png)

## 📊 Data Analysis / SQL

- For Power BI users, we have a new set of guides on optimising dashboard performance:
  - [Power Up your BI with Microsoft Power BI and Lakehouse in Azure Databricks: part 1 - Essentials](https://techcommunity.microsoft.com/t5/analytics-on-azure-blog/power-up-your-bi-with-microsoft-power-bi-and-lakehouse-in-azure/ba-p/3810649)
  - [Power Up your BI with Microsoft Power BI and Lakehouse in Azure Databricks: part 2 - Tuning Power BI](https://techcommunity.microsoft.com/t5/analytics-on-azure-blog/power-up-with-power-bi-and-lakehouse-in-azure-databricks-part-3/ba-p/3825010)
  - [Power Up with Power BI and Lakehouse in Azure Databricks: part 3 - Tuning Azure Databricks SQL](https://techcommunity.microsoft.com/t5/analytics-on-azure-blog/power-up-with-power-bi-and-lakehouse-in-azure-databricks-part-3/ba-p/3825010)

## 🛠️ Architecture

- [Multi-cloud Architecture for Portable Data and AI Processing in Financial Services](https://www.databricks.com/blog/multi-cloud-architecture-portable-data-and-ai-processing-financial-services): a useful blueprint for owning a reliable and governed **multi-cloud data architecture**. Although this article is focused on the financial services industry, it is relevant for any organisations with data footprints across clouds

## ⚡️ Performance Optimisation

- [](): as part of [Project Lightspeed](https://www.databricks.com/blog/2022/06/28/project-lightspeed-faster-and-simpler-stream-processing-with-apache-spark.html), AQE is applied to `ForeachBatch` to speed up transformation operations, leading to 1.2x-2.87x performance gains

## 🔐 Security


## 🏪 Databricks Marketplace

- [▶️ Introduction to Databricks Marketplace](https://www.youtube.com/watch?v=PGgWOw7g0lM): a short primer on Databricks Marketplace by our partners Advancing Analytics

## 🥂 Customer Stories

- [How **Stack Overflow** built their new course recommendations](https://stackoverflow.blog/2023/05/29/more-on-our-ai-future-building-course-recommendations-and-a-new-data-platform/) solution on Azure Databricks. I think it's safe to say we all owe Stack Overflow some thanks for aiding us in our technical careers; so I was happy to see Databricks play a role in helping the community discover relevant courses. *"[It was] it clear that leveraging one platform for as much as possible would be wise, and our platform of choice was Azure Databricks. This allowed us to keep all data processing, feature engineering, model versioning, serving, and orchestration all in one place."*

- [How Instacart Ads Modularized Data Pipelines With Lakehouse Architecture and Spark](https://tech.instacart.com/how-instacart-ads-modularized-data-pipelines-with-lakehouse-architecture-and-spark-e9863e28488d)

As always, please let me know if you'd like to find out more about any of the announcements or use cases above 👆🏽
