import redis        # pip install redis
ip="xxxxx"
r = redis.Redis(host=ip, port=6379, db=0,password='xxxxx')
v=r.get('key1');
print(v);
r.set('key1','30'.encode('utf-8'));
