USE CATALOG my_catalog;


-- Generic prompt handler
CREATE OR REPLACE FUNCTION PROMPT_HANDLER(prompt STRING)
RETURNS STRING 
COMMENT "Wrapper function to handle all our calls to Azure OpenAI. Analysts who want to use arbitrary prompts can use this handler" 
RETURN AI_GENERATE_TEXT(prompt,
        "azure_openai/gpt-35-turbo",
        "apiKey", SECRET("vinnyvijeyakumaar", "azure-openai"),
        "temperature", CAST(0.0 AS DOUBLE),
        "deploymentName", "my-deployment-name",
        "resourceName", "my-resource-name",
        "apiVersion", "2023-03-15-preview"
    );


-- Generate sample data
CREATE OR REPLACE FUNCTION GENERATE_SAMPLE_DATA(num_reviews INT DEFAULT 5) 
RETURNS array < struct < review_date :date, review_id :string, product_name :string, review :string >> RETURN
SELECT FROM_JSON(
        PROMPT_HANDLER(
            CONCAT(
                'Generate a sample dataset for me of ', num_reviews, 
                ' rows that contains the following columns: "date" (random dates in 2022), 
                "review_id" (random id), "product_name" (use realistic but not real product brands), and "review". 
                Reviews should mimic useful product reviews left on an e-commerce marketplace website. 

                The reviews should vary in length (shortest: one sentence, longest: 3 paragraphs), sentiment, and 
                complexity. A very complex review would talk about multiple topics (entities) about the product with 
                varying sentiment per topic. Provide a mix of positive, negative, and neutral reviews

                Give me JSON only. No text outside JSON. No explanations or notes
                [{"review_date":<date>, "review_id":<review_id>, "product_name":<product_name>, "review":<review>}]'
            )
        ),
        "array<struct<review_date:date, review_id:string, product_name:string, review:string>>"
    );

WITH data_sample AS (SELECT GENERATE_SAMPLE_DATA(10) AS sample_data),
exploded AS (SELECT EXPLODE(sample_data) AS sample_data FROM data_sample)
SELECT sample_data.*
FROM exploded;
