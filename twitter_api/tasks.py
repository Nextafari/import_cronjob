from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379')


@app.task
def say_hello():
    print("Hello World")
