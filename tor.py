from abc import ABC

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import requests
from camera import picture_data


# 接受图片数据（bit）
class upload_handler(RequestHandler):
    def get(self, urls):
        tmp = picture_data()
        data = {
            "picture_data_bits": tmp,
        }
        requests.get(urls, data)


if __name__ == '__main__':
    app = Application(
        [
            (r'/upload', upload_handler),
        ]
    )

    http_server = HTTPServer(app)
    http_server.listen(8000)
    IOLoop.current().start()
