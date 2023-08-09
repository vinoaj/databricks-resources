# YYYY-MM-DD

Hi team! I just wanted to share some of the interesting resources/articles that have come from Databricks in the last couple of weeks:

## Upcoming Events

🚨 **Data+AI World Tour ANZ!**: I want to extend an invite to our in-person **Data+AI World Tour** events happening in **Melbourne**, **Sydney**, and **Brisbane**!

We'll have talks from practitioners at Endeavour, Atlassian, NAB, SportsBet, Red Cross, Seven West Media, Tabcorp, and more! Besides learning about what's new in the world of Databricks, this is a fantastic opportunity to meet and mingle with peers in the industry.

Please sign up at the below links, and I'm looking forward to seeing you there!

- **Melbourne** Thu 31 Aug: [https://vnjv.co/daiwt23mel](https://vnjv.co/daiwt23mel)
- **Sydney** Tue 19 & Wed 20 Sep: [https://vnjv.co/daiwt23syd](https://vnjv.co/daiwt23syd) (Day 1 is in-person training and certification)
- **Brisbane** (TBC) Tue 14 Nov: (link coming soon)

## 💪🏽 Best Practices

- **NEW** ✨ [Comprehensive Guide to Optimize Databricks, Spark and Delta Lake Workloads](https://www.databricks.com/discover/pages/optimize-data-workloads-guide): a new guide walking you through all the possible ways to tune your workloads for ⚡️ performance and 💰 cost

- **NEW** ✨ [Demo Hub](https://www.databricks.com/resources/demos): access ready-to-run Notebooks that walk you through common worfklows and use cases on Databricks

- **NEW** ✨ [What's coming page](https://docs.gcp.databricks.com/whats-coming.html): provides an overview of what's coming in near future releases, helping you plan ahead of time

- [] XXXX summit videos

## 🧠 ML & AI

- The recent big LLM news is [Meta releasing Llama 2]([https://ai.meta.com/llama/](https://ai.meta.com/llama/)) to open source and for commercial use. Databricks is happy to be [one of the launch partners]([https://www.databricks.com/blog/building-your-generative-ai-apps-metas-llama-2-and-databricks](https://www.databricks.com/blog/building-your-generative-ai-apps-metas-llama-2-and-databricks)). Check out the [sample notebooks]([https://github.com/databricks/databricks-ml-examples/tree/master/llm-models/llamav2](https://github.com/databricks/databricks-ml-examples/tree/master/llm-models/llamav2)) on how to load, serve, and fine-tune Llama 2 all within Databricks!

- [Managing Complex Propensity Scoring Scenarios with Databricks](https://www.databricks.com/blog/managing-complex-propensity-scoring-scenarios-databricks)([Notebooks](https://notebooks.databricks.com/notebooks/RCG/Propensity/index.html#Propensity_1.html)| [GitHub](https://github.com/databricks-industry-solutions/propensity-workflows)): a new Solution Accelerator to manage regular feature updates (utilising Feature Store) and periodic model re-training

- [Announcing the MLflow AI Gateway](https://www.databricks.com/blog/announcing-mlflow-ai-gateway): an API gateway to govern enterprise use of Saas (e.g. OpenAI, Bard, Anthropic) and OSS LLMs. With MLflow AI Gateway you can:
  - Manage API keys in a central location
  - Manage costs by enforcing quota and rate controls
  - Improve developer productivity by exposing a standard API interface across all model providers

## 🛠️ Developer Experience

- [Introducing Lakehouse Apps](https://www.databricks.com/blog/introducing-lakehouse-apps): build secure native data and AI applications without compromise. Are you building applications on top of your Lakehouse data? Lakehouse Apps allows you to build and host those applications directly on your Lakehouse, preventing the need to move data around and worrying about inconsistent governance models.

## 🪛 Data Engineering

- [Never Miss a Beat: Announcing New Monitoring and Alerting capabilities in Databricks Workflows](https://www.databricks.com/blog/never-miss-beat-announcing-new-monitoring-and-alerting-capabilities-databricks-workflows):
  - **Duration warnings** alert you when jobs take longer than usual to execute. This allows you to identify and rectify issues sooner rather than later!
  - **Fine-grained notifications** allow you to control the types of alerts (e.g. failure, duration warning) each recipient receives

## 🛒 Retail

- [Go from Months to Hours with Databricks Marketplace for Retailers](https://www.databricks.com/blog/go-months-hours-databricks-marketplace-retailers)

## 🔐 Security

- [] XXXX ajmal video

- [Identifying and Tagging PII data with Unity Catalog](https://medium.com/@andrewpweaver/identifying-and-tagging-pii-data-with-unity-catalog-870522f25730)

## 🥂 Customer Stories

- [Australian Red Cross Lifeblood wins 2023 Data for Good Award](https://www.databricks.com/blog/announcing-winners-2023-databricks-data-team-awards): Red Cross are able to attract more donations and strengthen community bonds through initiatives that span granular forecasting, real-time wait-time predictions, customer segmentation, and marketing attribution

- [How Akamai Leverages Databricks Unity Catalog For Distributed Data Governance](https://medium.com/@agilad_3118/how-akamai-leverages-databricks-unity-catalog-for-distributed-data-governance-d1eda1c5851) (accompanying [Summit presentation and slides](https://www.databricks.com/dataaisummit/session/distributing-data-governance-how-unity-catalog-allows-collaborative-approach/)): with 50 exabytes of data accessed across 80 workspaces, Unity Catalog brought many efficiencies to the team:
  - Eliminated the need for duplicating mounts for shared datasets across workspaces
  - Implemented fine-grained access controls at the row and column levels
  - Eliminated the pains of syncing user management and access control across multiple workspaces
  - Single pane of glass for data observability

- [Accelerating Innovation at JetBlue 🛫 Using Databricks](https://www.databricks.com/blog/accelerating-innovation-jetblue-using-databricks): ([▶️ video](https://youtu.be/h4z4vBoxQ6s?t=5958)) thanks to Databricks JetBlue has benefited with: Rapid prototyping, iteration, and launching of data pipelines, jobs, and ML models; Elevated customer experience; Continuous improvement of overall value; Lowered TCO
    ![JetBlue Lakehouse architecture](https://www.databricks.com/sites/default/files/inline-images/image15.png)
    ![JetBlue BlueSky AI](https://www.databricks.com/sites/default/files/inline-images/image002.png)

- [**FactSet**'s Lakehouse adoption](https://medium.com/factset/the-factset-enterprise-solutions-lakehouse-5932ee5276f) resulted in faster processing times and improved team productivity while reducing costs by 83%

---

As always, please let me know if you'd like to find out more about any of the announcements or use cases above 👆🏽
