import random
import uuid
import hashlib
from multiprocessing.pool import ThreadPool

import redis

# r = redis.Redis(host='0.0.0.0', db=5)
# a = r.keys()
# print(r.hkeys("4ec"))
for db_id in range(10):
    r = redis.Redis(host='0.0.0.0', db=5+db_id)
    print(db_id)
    for i in range(1000_000):
        a = hashlib.md5(str(i).encode('utf-8')).hexdigest()
        r.hset(name=a[:5], key=a[5:], value=i)

#
# r.set('foo', 'bar')
# value = r.get('foo')
# print(value)
# md5()
#
# def set_to(x):
#     r.set(uuid.uuid4(), random.randrange(1, 100_000))
#
#
# pool = ThreadPool(10)
# pool.map(set_to, range(10_000_000))
# pool.close()
# pool.join()

