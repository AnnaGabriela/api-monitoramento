import os
import redis

HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
PASSWORD = os.environ.get("PASSWORD")

database = redis.Redis(host=HOST, port=PORT, password=PASSWORD, decode_responses=True)