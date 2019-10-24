import random
import uuid
import hashlib
from multiprocessing.pool import ThreadPool

import redis

r = redis.Redis(host='0.0.0.0', db=0)

for i in range(200_000_000):
    a = hashlib.md5(str(i*20).encode('utf-8')).hexdigest()
    r.hset(name=a[:4], key=a[4:], value=i)

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

