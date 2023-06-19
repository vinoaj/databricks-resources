# Developing in IDEs

## VS Code Extension

- Documentation: [Databricks](https://docs.gcp.databricks.com/dev-tools/vscode-ext.html)
- [Extension](https://marketplace.visualstudio.com/items?itemName=databricks.databricks)
- Requirements
  - Workspace
    - Contain at least one cluster
    - Enabled for Files in Repos
    - Relies on workspace directories
  - Cluster requirements
    - DBR 11.2+
  - Local machine requirements
    - VS Code 1.69.1+
    - VS code must be configured for Python coding, including availability of a Python interpreter
  - Authentication options
    - User PAT
    - Cloud credentials

### Setup

- Click on Databricks extension icon
- Click on `Configure Databricks`
- Select configuration profile living in `~/.databrickscfg`
- [Set the cluster](https://docs.gcp.databricks.com/dev-tools/vscode-ext.html#set-the-cluster)
- [Set the workspace directory](https://docs.gcp.databricks.com/dev-tools/vscode-ext.html#set-the-workspace-directory)
  - Recommended not to sync with your repo directory
  - Click on sync icon next to `Sync Destination` item
  - **Important**: The Databricks extension for Visual Studio Code only performs one-way, automatic synchronization of file changes from your local Visual Studio Code project to the related workspace directory in your remote Databricks workspace. The files in this remote workspace directory are intended to be transient. Do not initiate changes to these files from within your remote workspace, as these changes will not be synchronized back to your local project.
- [Enable PySpark and Databricks Utilities code completion](https://docs.gcp.databricks.com/dev-tools/vscode-ext.html#enable-pyspark-and-databricks-utilities-code-completion)
- Setup [Databricks Connect](https://docs.gcp.databricks.com/dev-tools/vscode-ext.html#run-or-debug-python-code-with-databricks-connect)
  - `python3.10 -m venv ./.venv`
  - `source ./.venv/bin/activate`
