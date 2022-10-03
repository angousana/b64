import requests as req
from concurrent.futures import ThreadPoolExecutor

url="http://jae.sg"

def rem(file):
    try:
        return req.post(url, data={'act': 'rem', 'file': str(file)}).text
    except:
        return False
def get(file):
    try:
        return req.post(url, data={'act': 'get', 'file': str(file)}).text
    except:
        return False
def put(file, data):
    try:
        return req.post(url, data={'act': 'put', 'file': str(file), 'data': str(data)}).text
    except:
        return False
def app(file, data):
    try:
        return req.post(url, data={'act': 'app', 'file': str(file), 'data': str(data)}).text
    except:
        return False
def rep(file, data):
    try:
        return req.post(url, data={'act': 'rep', 'file': str(file), 'data': str(data)}).text
    except:
        return False
def exe(workers):
    return ThreadPoolExecutor(max_workers=workers)

angouFTP=True
