
SELECT pg_start_backup('replica_backup', true);
SELECT pg_stop_backup();
