# Examples of working with the Databricks CLI

- [Documentation](https://docs.databricks.com/dev-tools/cli/databricks-cli.html)

## Installation

### macOS Homebrew

```sh
brew tap databricks/tap
brew install databricks
```

#### zsh

```sh
echo fpath+=$(brew --prefix)/share/zsh/site-functions >> ~/.zshrc
echo 'autoload -Uz compinit && compinit' >> ~/.zshrc
source ~/.zshrc
```

### Verify version

`databricks -v`

## Working with connection profiles

### Find your .databrickscfg file (usually in ~/)

`find / -name ".databrickscfg"`

### List profiles

`less ~/.databrickscfg`

### Create new profile

`databricks configure --token --profile new_profile_name`

### Using a profile

`databricks workspace ls --profile new_profile_name`

## Working with secrets

### List scopes

`databricks secrets list-scopes --profile profile_name`

### Create a secrets scope

`databricks secrets create-scope scopenamehere`

#### Add Secrets

`databricks secrets put-secret scopenamehere keynamehere --string-value XXXXXXXX`

##### If using older version of CLI

`databricks secrets put --scope scopenamehere --key KAGGLE_USERNAME --string-value vinoaj`

## Troubleshooting

`Error: Get "https://xyz.xyz.databricks.com/api/2.0/preview/scim/v2/Me": EOF`

- Check that you have connectivity to the given URL
  - Check firewall, VPN, etc
