# Performance Tuning

## Delta Table Tuning
- [ ] Ensure your tables are Delta tables: `CONVERT TO DELTA table_name` (docs: [AWS](https://docs.databricks.com/delta/porting.html#convert-to-delta-table) | [GCP](https://docs.gcp.databricks.com/delta/porting.html#convert-to-delta-table) | [Azure](https://docs.microsoft.com/en-gb/azure/databricks/delta/porting#convert-to-delta-table))
- [ ] Optimise file size for fast file pruning
    - There is an ideal data file size – too small and you will have too many files (the well-known “small-file problem”); too large and you won’t be able to skip enough data
    - [ ] [Autotune baed on workload](https://docs.databricks.com/delta/optimizations/file-mgmt.html#autotune-based-on-workload)
        - SQL: `SET spark.databricks.delta.tuneFilseSizesForRewrites=True`
        - SQL: `ALTER TABLE db_name.table_name SET TBLPROPERTIES (delta.tuneFilseSizesForRewrites=True)`
        - Python: `spark.conf.set("spark.databricks.delta.tuneFilseSizesForRewrites", True)`
    - [ ] [Autotune based on table size](https://docs.databricks.com/delta/optimizations/file-mgmt.html#autotune-based-on-table-size)
        - For tables smaller than 2.56 TB, the autotuned target file size is 256 MB. For tables with a size between 2.56 TB and 10 TB, the target size will grow linearly from 256 MB to 1 GB. For tables larger than 10 TB, the target file size is 1 GB
        - SQL: `SET spark.databricks.delta.tuneFilseSizesForRewrites=True`
        - SQL: `ALTER TABLE db_name.table_name SET TBLPROPERTIES (delta.tuneFilseSizesForRewrites=True)`
        - Python: `spark.conf.set("spark.databricks.delta.tuneFilseSizesForRewrites", True)`
    - [ ] Manual tune
        - Target filesize is expressed in number of bytes. Formula for `MB` to `bytes` is `1024*1024*{n_MB}`
        - SQL: `SET spark.databricks.delta.targetFileSize=33554432`
        - SQL: `ALTER TABLE db_name.table_name SET TBLPROPERTIES (delta.targetFileSize=33554432)`
        - Python: `spark.conf.set("spark.databricks.delta.targetFileSize", True)`
        - A good file size range is 32-128MB
