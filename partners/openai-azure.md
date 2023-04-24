# Working with Azure OpenAI

- [Request](https://aka.ms/oai/access) an Azure OpenAI key
- Navigate to [Azure OpenAI Studio](https://oai.azure.com/)
  - Select a resource or [Create](https://portal.azure.com/?microsoft_azure_marketplace_ItemHideKey=microsoft_openai_tip#create/Microsoft.CognitiveServicesOpenAI) an Azure OpenAI resource
- Go to [Deployments](https://oai.azure.com/portal/deployment)

  <img src="https://raw.githubusercontent.com/vinoaj/databricks-resources/main/assets/img/openai/azure-openai-deployments.png" width="600">

  - Click on `Create new deployment`
  - For GPT3.5 Turbo, select the following
    - Model name: `gpt-35-turbo`
    - Model version: `0301`
    - Deployment name: `<deployment name>`
  
      <img src="https://raw.githubusercontent.com/vinoaj/databricks-resources/main/assets/img/openai/azure-openai-deployments-create.png" width="600">

  - Click `Create`
- Get your key and endpoint information
  - [Navigate to Azure Portal > All Services > Cognitive Services > Azure OpenAI](https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/OpenAI)
    
    <img src="https://raw.githubusercontent.com/vinoaj/databricks-resources/main/assets/img/openai/azure-openai-cognitive-services-overview.png" width="600">

  - Click into the relevant resource
  - Click on `Keys and Endpoint`

    <img src="https://raw.githubusercontent.com/vinoaj/databricks-resources/main/assets/img/openai/azure-openai-cognitive-services-keys-endpoints.png" width="470">

  - Note down your:
    - Key (do **NOT** store this in plaintext, include it in your code, and/or commit it into your git repo)
    - Region
    - Endpoint URL (of the form `https://<resource-name>.openai.azure.com/`)

## Store key as a secret in Databricks

We'll use [secrets](https://docs.databricks.com/security/secrets/index.html) to hold our API tokens. 

Use the [Databricks Secrets CLI](https://docs.databricks.com/dev-tools/cli/secrets-cli.html) or [Secrets API 2.0](https://docs.databricks.com/dev-tools/api/latest/secrets.html)

- If you don't already have a secret scope to keep your OpenAI keys in, create one now: `databricks secrets create-scope --scope openai`
- You will need to give `READ` or higher access for principals (e.g. users, groups) who are allowed to connect to OpenAI. We recommend creating a group `openai-users` and adding permitted users to that group. Then give that group `READ` permission to the scope: `databricks secrets put-acl --scope openai --principal openai-users --permission READ`
- Create a secret for your API key. We recommend format `<resource-name>-key`: `databricks secrets put --scope openai --key vvtest-key --string-value yourkeyhere1234567`
