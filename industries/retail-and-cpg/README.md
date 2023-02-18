# Databricks: Retail & Consumer Packaged Goods (CPG) Use Cases

- [Collaborating Across the Retail Value Chain with Data and AI](https://databricks.com/p/ebook/collaborating-across-the-retail-value-chain-with-data-and-ai)(eBook)
![Product insights use cases](https://databricks.com/wp-content/uploads/2022/03/db-118-blog-img-1.jpg)
![Consumer insights use cases](https://databricks.com/wp-content/uploads/2022/03/db-118-blog-img-2.jpg)

- [Delivering Real-Time Data to Retailers with Delta Live Tables](https://databricks.com/blog/2022/04/12/delivering-real-time-data-to-retailers-with-delta-live-tables.html) (fully documented [notebooks](https://d1r5llqwmkrl74.cloudfront.net/notebooks/RCG/POS_DLT/index.html#POS_DLT_1.html))

## Solutions Accelerators

- [Optimizing Order Picking to Increase Omnichannel Profitability with Databricks](https://www.databricks.com/blog/2022/08/04/optimizing-order-picking-to-increase-omnichannel-profitability-with-databricks.html) ([📄 notebooks](https://d1r5llqwmkrl74.cloudfront.net/notebooks/RCG/Optimized_Picking/index.html#Optimized_Picking_1.html))
- [Scalable Route Generation](https://www.databricks.com/solutions/accelerators/scalable-route-generation) ([📄 notebooks](https://d1r5llqwmkrl74.cloudfront.net/notebooks/RCG/Routing/index.html#Routing_1.html))
- [Intermittent Demand Forecasting](https://www.databricks.com/blog/2022/12/06/intermittent-demand-forecasting-nixtla-databricks.html): Forecasting on a per-SKU and per-store level has always been a challenge, especially when there are periods with zero-unit demand. 
  - In the spirit of embracing open-source and staying away from black-box algorithms, we use [Nixtla's open source forecasting models](https://www.nixtla.io/). This allows you (a) to fine-tune your forecasts and (b) ensures portability across platforms.
  - You can access the notebooks via the second "Download notebook" link [here](https://www.databricks.com/solutions/accelerators/demand-forecasting). The flow covers:
    - Loading [Walmart's M5 Forecasting dataset](https://www.kaggle.com/competitions/m5-forecasting-accuracy/data)
    - Transformation of the data to be in the appropriate shape to work with Nixtla's libraries
    - Building a baseline forecast
    - Evaluating multiple models and identifying the best candidate 
    - Generating forecasts, picking the best model for each time series
    - Bonus: algorithm to determine how frequently forecasts should be generated
  - This solution accelerator can be used to augment your existing forecasting solutions, or as a thought-starter to enhance your existing forecasting models. As with all our solution accelerators, this is free to access and repurpose
  - [Products We Think You Might Like: Generating Personalized Recommendations Using Matrix Factorization](https://www.databricks.com/blog/2023/01/06/products-we-think-you-might-generating-personalized-recommendations.html)

### Brickbuilder Solutions

- [Bending Retails’ Curve – Moving Beyond Possible With Tredence](https://www.databricks.com/blog/2022/12/19/bending-retails-curve-moving-beyond-possible-tredence.html)

## Guides

- [Getting Started with Personalization through Propensity Scoring](https://databricks.com/blog/2022/06/03/getting-started-with-personalization-through-propensity-scoring.html) (accompanying [notebooks](https://d1r5llqwmkrl74.cloudfront.net/notebooks/nightly/RCG/Propensity/index.html#Propensity_1.html))
![Propensity scoring workflow](https://databricks.com/wp-content/uploads/2022/05/db-192-blog-img-1.png)
- [Using MLflow to deploy Graph Neural Networks for Monitoring Supply Chain Risk](https://medium.com/@ajmal.t.aziz/using-mlflow-to-deploy-graph-neural-networks-for-monitoring-supply-chain-risk-644c87e5259e)

## Case Studies

- [84.51° Uses Databricks Lakehouse to improve its forecasting accuracy across Kroger stores](https://www.youtube.com/watch?v=1TcmBjCOnL0)
- [Democratizing Data for Supply Chain Optimization: How Johnson & Johnson Leverages the Databricks Lakehouse](https://databricks.com/blog/2022/04/25/democratizing-data-for-supply-chain-optimization.html)
- [Walgreens uses Databricks Lakehouse to personalize patient experiences & optimize their supply chain](https://www.youtube.com/watch?v=l2rnu-6rEXU) (video)
- [Crisp and Databricks bring supply chain visibility to the lakehouse](https://www.gocrisp.com/blog/databricks)

---

## Industry Trends

- [Retail Info System (RIS) 32nd Annual Retail Technology Study](https://risnews.com/retail-tech-study-2022?from=gate)

---

## Sample Datasets

- [<img src="../../assets/img/kaggle-transparent.svg" width="30"> Dunnhumby - The Complete Journey](https://www.kaggle.com/datasets/frtgnn/dunnhumby-the-complete-journey): "This dataset contains household level transactions over two years from a group of 2,500 households who are frequent shoppers at a retailer. It contains all of each household’s purchases. For certain households, demographic information as well as direct marketing contact history are included. Due to the number of tables and the overall complexity of The Complete Journey, it is suggested that this database be used in more advanced classroom settings"
- [<img src="../../assets/img/kaggle-transparent.svg" width="30"> Instacart Market Basket Analysis](https://www.kaggle.com/competitions/instacart-market-basket-analysis/data): "... a relational set of files describing customers' orders over time. ...anonymized and contains a sample of over 3 million grocery orders from more than 200,000 Instacart users. For each user, we provide between 4 and 100 of their orders, with the sequence of products purchased in each order. We also provide the week and hour of day the order was placed, and a relative measure of time between orders" (accompanying [blog post](https://tech.instacart.com/3-million-instacart-orders-open-sourced-d40d29ead6f2))
