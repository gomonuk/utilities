CREATE EXTENSION plpython3u;

create or replace function count_odd_iterator() returns integer
  language plpython3u
as
$$
odd = 0
for row in plpy.cursor("select num from largetable"):
    if row['num'] % 2:
         odd += 1

try:
    for row in plpy.cursor("select nm from largetable"):
        if row['num'] % 2:
             odd += 1
except plpy.spiexceptions.UndefinedColumn:
     plpy.info("!!!!!!!!!!!!!!!!!!!!!!!")
return odd
$$;


create table largetable (num integer);
insert into largetable (num) VALUES (2),(1),(3);
select * from count_odd_iterator();