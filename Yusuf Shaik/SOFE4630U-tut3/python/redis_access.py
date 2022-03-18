import redis        # pip install redis
ip=""
r = redis.Redis(host=ip, port=1, db=0,password='')
v=r.get('key1');
print(v);
r.set('key1','30'.encode('utf-8'));
