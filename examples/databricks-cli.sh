#!/bin/bash

# Examples of working with the Databricks CLI

## Working with connection profiles

### Find your .databrickscfg file (usually in ~/)
find / -name ".databrickscfg"

### List profiles
less ~/.databrickscfg

### Create new profile
databricks configure --token --profile new_profile_name

### Using a profile
databricks workspace ls --profile new_profile_name

## Working with secrets

### Create a secrets scope
databricks secrets create-scope --scope vinnyvijeyakumaar

databricks secrets put --scope vinnyvijeyakumaar --key KAGGLE_USERNAME --string-value vinoaj
databricks secrets put --scope vinnyvijeyakumaar --key KAGGLE_KEY --string-value XXXXXXXX


### List scopes
databricks secrets list-scopes --profile profile_name
