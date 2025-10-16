"""Basic connection example.
"""
from dotenv import dotenv_values

config = dotenv_values(".env")

password = config['REDIS_PASSWORD']

import redis

r = redis.Redis(
    host='redis-19213.c83.us-east-1-2.ec2.redns.redis-cloud.com',
    port=19213,
    decode_responses=True,
    username="default",
    password=password
)


# success = r.set('foo', 'bar')
# True

# result = r.get('foo')
# 'bar'

key = 'sample_bicycle:1084'
key_type = r.type(key)

print(key_type)

result = r.execute_command('JSON.GET', 'sample_bicycle:1084')
print(result)

r.close()

