from redis import Redis
from rq import Queue, Worker

q = Queue(connection=Redis())
rqworker