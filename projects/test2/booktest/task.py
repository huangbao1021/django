import time
from celery import task

@task
def shows():
    print('hello....')
    time.sleep(5)
    print('world...')