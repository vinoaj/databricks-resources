# Using Power BI with Databricks

- [▶️ Connect to Power BI Desktop from Databricks](https://www.youtube.com/watch?v=EcKqQV0rCnQ)
- [Architecting Aggregations in PowerBI with Databricks SQL](https://medium.com/@kyle.hale/architecting-aggregations-in-powerbi-with-databricks-sql-675899014ce3)
- [Easier data model management for Power BI using Delta Live Tables](https://techcommunity.microsoft.com/t5/analytics-on-azure-blog/easier-data-model-management-for-power-bi-using-delta-live/ba-p/3500698)

- **Azure Databricks vs Spark Connector** in Power BI? Prefer the native Azure Databricks connector, for the following reasons
    - Utilises Databricks SQL endpoints, which is designed for high-concurrency low-latency applications such as BI
    - SQL endpoint benefits include:
        - Dual queue workload management
        - Multi-cluster load balancing
        - Elastic horizontal scaleout
        - Resultset caching
        
- **Azure Analysis Services (AAS)**
    - Cannot use Databricks SQL directly, only via ODBC (which requires PBI gateway)
    - Microsoft's recommendation is to migrate AAS workloads to Power BI Premium. Offers similar functionality to AAS **but** with a wider array of native connectors
