## Celery Configurations

pip install celery
pip install daphne
pip install channel
pip install redis
pip install django-redis



## docker 

1. database :

3542d1aae65d  - djangoframework   - database

2. memcache

01dc329ef3c7   memcatchdjangoframework

3. rabbitmq

25fbe527d7ee  myrabbitmq

4. redis

6d56391b84bb    RedisLearning


## start celery worker and beat commands

```celery -A mainsrc worker --beat --loglevel=info```
