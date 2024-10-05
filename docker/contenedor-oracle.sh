docker run --name oracle \
-e ORACLE_DATABASE=ORCL \
-e APP_USER=ETL \
-e APP_USER_PASSWORD=ETL \
-e ORACLE_PASSWORD=oracle \
-p 1521:1521 -d gvenzl/oracle-free