import requests


class ApiClient:
    def __init__(self, url):
        self.url = url

    def get(self, path):
        return requests.get(self.url + path)

    def post(self, path, data):
        return requests.post(self.url + path, data=data)

    def put(self, path, data):
        return requests.put(self.url + path, data=data)

    def delete(self, path):
        return requests.delete(self.url + path)