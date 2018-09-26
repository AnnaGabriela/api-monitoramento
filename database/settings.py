import os
import redis

HOST = os.environ.get("REDIS_HOST")
PORT = os.environ.get("REDIS_PORT")
PASSWORD = os.environ.get("REDIS_PASSWORD")

db = redis.Redis(host=HOST, port=PORT, password=PASSWORD, decode_responses=True)