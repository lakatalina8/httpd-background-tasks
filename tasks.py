import time
from tornado.concurrent import return_future
import requests
import settings


class User(object):

    def save(self):
        time.sleep(0.02)

    def send_email(self):
        time.sleep(0.06)

    def social_api(self):
        time.sleep(0.2)


def sleep():
    user = User()
    user.save()
    user.send_email()
    user.social_api()


def sleep_sync():
    sleep()


@return_future
def sleep_async(callback=None):
    sleep()
    callback()


def network_sync():
    res = requests.get("http://localhost")
    return res.content


def file_sync():
    f = open("template.html")
    content = f.read()
    f.close()
    return content


def get_task(name):
    return globals()[name]
