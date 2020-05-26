#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "db" <<-EOSQL
    CREATE TABLE marvelHeroes1 (id int PRIMARY KEY, nombre char(50),tipos char(150),imagen char(350));
EOSQL
