import redis        # pip install redis
ip='';
r = redis.Redis(host=ip, port=1, db=0,password=1)
v=r.get('uno');
with open("./recievedUno.jpg", "wb") as f:
    f.write(v);

v=r.get('dos');
with open("./recievedDos.jpg", "wb") as f:
    f.write(v);


v=r.get('tres');
with open("./recievedTres.jpg", "wb") as f:
    f.write(v);
