import redis

host = "redis-18369.c16.us-east-1-3.ec2.cloud.redislabs.com"
port = 18369
password = "$123"

database = redis.Redis(host=host, port=port, password=password, decode_responses=True)