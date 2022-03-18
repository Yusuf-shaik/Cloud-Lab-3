import redis        # pip install redis
ip='xxxxx';
r = redis.Redis(host=ip, port=6379, db=0,password='xxxxx')
v=r.get('OntarioTech');
with open("./recieved.jpg", "wb") as f:
    f.write(v);
