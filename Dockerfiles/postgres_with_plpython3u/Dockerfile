FROM postgres:11

RUN apt-get update 
RUN apt-get -y install python3 postgresql-plpython3-11

RUN  apt-get clean && \
     rm -rf /var/cache/apt/* /var/lib/apt/lists/*

WORKDIR /
ADD . /
COPY create_exctension.sql /docker-entrypoint-initdb.d/

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 5432
CMD ["postgres"]

