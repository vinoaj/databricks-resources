# Inspecting Azure Log Analytics for key Databricks events

What is KQL? KQL stands for [Kusto Query Language](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/). It is a read-only request to process data and return results. The request is stated in plain text, using a data-flow model designed to make the syntax easy to read, author, and automate. KQL is not a case-sensitive language. KQL is used for querying large volumes of data in Azure Data Explorer, Log Analytics, and Application Insights

Databricks ActionNames and requestParam fields are documented [here](https://learn.microsoft.com/en-us/azure/databricks/administration-guide/account-settings/azure-diagnostic-logs)

## Changes to Workspace configurations

```kql
DatabricksWorkspace
| where ActionName in ("workspaceConfEdit")
| where TimeGenerated > ago(30d)| project ActionName, parse_json(Identity).email, parse_json(Response).statusCode, parse_json(RequestParams).workspaceConfKeys, parse_json(RequestParams).workspaceConfValues, SourceSystem, TimeGenerated, Type, UserAgent
```

## Changes to Workspace ACLs & role assignments

```kql
DatabricksWorkspace
| where ActionName in ("changeWorkspaceAcl", "updateRoleAssignment", "workspaceConfEdit")
| where TimeGenerated > ago(24h)
| project ActionName, parse_json(Identity).email, parse_json(Response).statusCode, RequestParams, SourceSystem, TimeGenerated, Type, UserAgent
```

## Changes to Global Init Scripts

```kql
// Monitor changes to Global Init Scripts

DatabricksGlobalInitScripts
| where ActionName in('create', 'delete', 'update') 
// Specifically search for unsuccessful actions
// | where parse_json(Response).statusCode != 200 
| where TimeGenerated > ago(24h)| project ActionName, Identity, parse_json(Response).statusCode, RequestParams, parse_json(RequestParams).name, parse_json(RequestParams).script_id, TimeGenerated, _ResourceId
```

## Detect any erroneous job operations

```kql
DatabricksJobs
| where TimeGenerated > ago(24h)
| where parse_json(Response).statusCode != 200
| project ActionName, parse_json(Identity).email, parse_json(Response).statusCode, RequestParams, parse_json(RequestParams).jobId, parse_json(RequestParams).runId, parse_json(RequestParams).jobTriggerType, parse_json(RequestParams).clusterId, parse_json(RequestParams).jobClusterType, parse_json(RequestParams).jobTaskType, parse_json(RequestParams).taskKey, _ResourceId
```

## Detect job configuration changes

```kql
DatabricksJobs
| where ActionName in ("changeJobAcl", "delete", "deleteRun", "reset", "update")
| where TimeGenerated > ago(24h)| project ActionName, parse_json(Identity).email, parse_json(Response).statusCode, RequestParams, parse_json(RequestParams).jobId, parse_json(RequestParams).runId, parse_json(RequestParams).jobTriggerType, parse_json(RequestParams).clusterId, parse_json(RequestParams).jobClusterType, parse_json(RequestParams).jobTaskType, parse_json(RequestParams).taskKey, _ResourceId
```

## Detect failed secrets requests

```kql
DatabricksSecrets
| where parse_json(Response).statusCode != 200
| where TimeGenerated > ago(30d)
```

## Changes to Databricks Account-level permissions

```
// Monitor account-level user/group account & ACL changes

DatabricksAccounts 
| where ActionName in('activateUser', 'add', 'addPrincipalToGroup', 'changeDbTokenAcl', 'deactivateUser', 'removeAdmin', 'removeGroup', 'removePrincipalFromGroup', 'setAdmin', 'updateUser') 
// Specifically search for unsuccessful actions
// | where parse_json(Response).statusCode != 200 
| where TimeGenerated > ago(24h)
| project ActionName, Identity, parse_json(Response).statusCode, RequestParams, TimeGenerated, _ResourceId
```

## Monitor login attempts

```kql
// Monitor user- and token-based logins

DatabricksAccounts 
| where ActionName in('aadBrowserLogin', 'aadTokenLogin', 'tokenLogin') 
// Specifically search for unsuccessful logins
// | where parse_json(Response).statusCode != 200 
| where TimeGenerated > ago(24h)
| project ActionName, Identity, parse_json(Response).statusCode, parse_json(RequestParams).user, TimeGenerated, _ResourceId
```
