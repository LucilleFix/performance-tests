from redis import Redis

cache = Redis(host='redis', port=6379)
cache.incr('times',amount=)
print(cache.get('times'))