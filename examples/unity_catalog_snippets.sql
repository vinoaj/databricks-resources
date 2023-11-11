-- Show current user
SELECT current_user();

-- Set default catalog and schema
SHOW CATALOGS;
USE CATALOG vinny_vijeyakumaar;
USE SCHEMA bronze;

-- Querying information_schema
SELECT *
FROM vinny_vijeyakumaar.information_schema.tables
WHERE table_schema NOT IN ("information_schema")
ORDER BY table_schema,
    table_name;