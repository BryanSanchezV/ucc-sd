FROM postgres:15
COPY init.sql /docker-entrypoint-initdb.d/
COPY postgresql.conf /etc/postgresql/
COPY pg_hba.conf /etc/postgresql/
RUN chmod 644 /etc/postgresql/postgresql.conf /etc/postgresql/pg_hba.conf
