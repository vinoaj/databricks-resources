# YYYY-MM-DD

[Understanding Caching in Databricks SQL: UI, Result, and Disk Caches](https://www.databricks.com/blog/understanding-caching-databricks-sql-ui-result-and-disk-caches)
![Types of DBSQL Caches](https://cms.databricks.com/sites/default/files/inline-images/db-532-blog-img-1.png)




Hi team! I just wanted to share some of the interesting resources/articles that have come from Databricks in the last couple of weeks:

## 🎓 Training & Education

- [Enroll in our New Expert-Led Large Language Models (LLMs) Courses on edX](https://www.databricks.com/blog/enroll-our-new-expert-led-large-language-models-llms-courses-edx) starting Jun 8!  Master Large Language Models with expert guidance, hands-on learning, and insights from industry pioneers. Explore cutting-edge techniques like prompt engineering, embeddings, vector databases, and model tuning. Learn from luminaries like [Stanford Professor & Databricks Co-Founder Matei Zaharia](https://cs.stanford.edu/people/matei/) and the creators of Dolly. Access free course materials to audit and elevate your LLM expertise. Consistent with our goal of keeping things open, course materials are **free** for anyone to audit. **[Enroll today](https://www.edx.org/professional-certificate/databricks-large-language-models)**

## User Experience

- [Test out the new navigation UI](https://www.databricks.com/blog/find-what-you-seek-new-navigation-ui) and give us your feedback. The unified navigation bar has been a great time-saver, allowing me to switch between screens in fewer clicks

## 🧠 ML & AI

- New Solution Accelerator! [Build your own Chatbot](https://d1r5llqwmkrl74.cloudfront.net/notebooks/RCG/diy-llm-qa-bot/index.html#diy-llm-qa-bot_1.html): walks through indexing documents, generating embeddings (using OpenAI embeddings), persisting embeddings in a vector store (FAISS), creating a Q&A flow (using Langchain), persisting the model in MLflow registry, and serving the model for your applications ([Accompanying blog post](https://www.databricks.com/blog/driving-large-language-model-revolution-customer-service-and-support))

- [Actioning Customer Reviews at Scale with Databricks SQL AI Functions](https://www.databricks.com/blog/actioning-customer-reviews-scale-databricks-sql-ai-functions): bring meaning to unstructured data using the simplicity of SQL and GPT-3.5

## 🛠️ Developer Experience

- [30+ reusable Terraform modules to provision your Databricks Lakehouse platform](https://www.databricks.com/blog/announcing-terraform-databricks-modules): the newly released [Terraform Registry modules for Databricks](https://registry.terraform.io/modules/databricks/examples/databricks/latest) provides 30+ reusable Terraform modules and examples to provision your Databricks Lakehouse platform. I've found this useful for exploring best practices and speeding up Terraform development

- [New debugging features for Databricks Notebooks with Variable Explorer](https://www.databricks.com/blog/new-debugging-features-databricks-notebooks-variable-explorer): a welcome productivity boost for debugging! Variable Explorer allows you to inspect the value of any variable or dataframe as you step through your code. Combine this with [`pdb`](https://docs.python.org/3/library/pdb.html) to set breakpoints and investigate interactively with UI support in the Databricks notebook.

- [▶️ Databricks Connect v2 Quickstart](https://www.youtube.com/watch?v=BIysxyh_lro)

## 🪛 Data Engineering

- [How Databricks improved query performance by up to 2.2x by automatically optimizing file sizes](https://www.databricks.com/blog/how-databricks-improved-query-performance): Unity Catalog managed tables takes care of optimising file sizes for you, so you don't have to worry about it. Instead you can sit back and enjoy the performance boost!

- [Processing data simultaneously from multiple streaming platforms using Delta Live Tables](https://www.databricks.com/blog/processing-data-simultaneously-multiple-streaming-platforms-using-delta-live-tables): walkthrough of simultaneously ingesting and transforming streams across Azure Event Hubs, Kafka, and Kinesis

- [Track health and fitness goals with Apple Healthkit and Databricks](https://www.databricks.com/blog/track-health-and-fitness-goals-apple-healthkit-and-databricks): great walkthrough of building out health insights using a metadata-driven approach with Delta Live Tables for ETL ([GitHub repo](https://github.com/jesusr-db/db-ahk))

## 📊 Data Analysis / SQL

- [Using Databricks SQL in VSCode](https://www.advancinganalytics.co.uk/blog/2023/4/12/using-databricks-sql-in-vscode)

- [Actioning Customer Reviews at Scale with Databricks SQL AI Functions](https://www.databricks.com/blog/actioning-customer-reviews-scale-databricks-sql-ai-functions): bring meaning to unstructured data using the simplicity of SQL and GPT-3.5

- [Predictive I/O for Reads](https://www.databricks.com/blog/announcing-general-availability-predictive-io-reads.html) is now GA! It's an ML feature, to enhance the speed and efficiency of point lookups. By intelligently predicting required data and eliminating the need for costly indexes or optimization services, it significantly improves query performance. Real-world applications have demonstrated up to 35x faster response times compared to other cloud data warehouses, all while reducing complexity and maintenance overhead

- [Introduction to Databricks SQL](https://www.advancinganalytics.co.uk/blog/2023/4/6/introduction-to-databricks-sql): a good walkthrough by one of our partners on the capabilities of Databricks SQL

## 🛒 Retail

- [Simplify entity resolution with Databricks Automated Record Connector (ARC)](https://www.databricks.com/blog/improving-public-sector-decision-making-simple-automated-record-linking) ARC abstracts away the complexity of utilising UK Ministry of Justice's [Splink library](https://github.com/moj-analytical-services/splink) for entity resolution. It determines the optimal set of blocking rules, comparisons, and deterministic rules ([GitHub repo](https://github.com/databricks-industry-solutions/auto-data-linkage))

## ⚡️ Performance Optimisation

- [Understanding Caching in Databricks SQL: UI, Result, and Disk Caches](https://www.databricks.com/blog/understanding-caching-databricks-sql-ui-result-and-disk-caches)
![Types of DBSQL Caches](https://cms.databricks.com/sites/default/files/inline-images/db-532-blog-img-1.png)

- [Predictive I/O for Optimised Reads](https://www.databricks.com/blog/announcing-general-availability-predictive-io-reads.html) is now generally available for SQL Pro and Serverless. Provides the benefits of indexes and optimization services, but without the complexity and cost of maintaining them.

## 🔐 Security

- [Welcome Okera: Adopting an AI-centric approach to governance](https://www.databricks.com/blog/welcome-okera-adopting-ai-centric-approach-governance). Databricks will integrate Okera's capabilities into Unity Catalog, including AI-powered discovery and handling of sensitive (e.g. PII) data and new isolation technology for workloads.

## Delta Sharing

- []()

## 🥂 Customer Stories

- []()

## Upcoming Events

- []()


As always, please let me know if you'd like to find out more about any of the announcements or use cases above 👆🏽
