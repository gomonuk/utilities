
##### Билдим орбраз с именем postgres_with_python3
docker build -t postgres_with_python3 .

##### Запускаем контейнер с именем postgres_for_cursor, флагом -e передаем в контейнер переменные окружения
docker run --name postgres_for_cursor  -e POSTGRES_PASSWORD=11 -e POSTGRES_USER=postgres postgres_with_python3

##### Чтобы подлючится к конейнеру надо узнать его IP. 
docker inspect postgres_for_cursor | grep IPAddress

Если этот способ не работает, попробуйте при запуске указать флаг *--network host* и подлючится к локалхосту