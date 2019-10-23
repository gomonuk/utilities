psql --command "CREATE EXTENSION plpython3u;"


docker build -t postgres_with_pytohn3 .
docker run --name postgres_for_cursor  -e POSTGRES_PASSWORD=11 -e POSTGRES_USER=postgres -d postgres_with_pytohn3
docker inspect postgres_for_cursor | grep IPAddress