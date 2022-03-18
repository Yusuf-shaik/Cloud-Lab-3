from email.mime import image
from kafka import KafkaProducer;
import json;
import time
import io;
from avro.io import DatumWriter, BinaryEncoder
import avro.schema
import numpy as np;

data=json.load(open('cred.json'))
bootstrap_servers=data['bootstrap_servers'];
sasl_plain_username=data['Api key'];
sasl_plain_password=data['Api secret'];

producer = KafkaProducer(bootstrap_servers=bootstrap_servers,security_protocol='SASL_SSL',sasl_mechanism='PLAIN',\
        sasl_plain_username=sasl_plain_username,sasl_plain_password=sasl_plain_password,key_serializer=lambda v: v.encode())
    
imageArr = {"uno": "image1.jpg", "dos": "image2.jpg", "tres": "image3.jpg"}
for a in imageArr:
    with open(imageArr[a], "rb") as f:
        value = f.read(); 
        print("imagename: ", imageArr[a], "\nkey: ", a)
        producer.send('ToRedis', value,key=a);

    
producer.close();
