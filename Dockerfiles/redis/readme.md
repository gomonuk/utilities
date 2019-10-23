#### Хочется записывать большое кол-во пар

https://instagram-engineering.com/storing-hundreds-of-millions-of-simple-key-value-pairs-in-redis-1091ae80f74c

hash-zipmap-max-entries 1024

docker run -v ~/PycharmProjects/utilities/Dockerfiles/redis/redis.conf:/usr/local/etc/redis/redis.conf  \
          --network host \
           -m 15GB \
          --name myredis redis redis-server /usr/local/etc/redis/redis.conf
