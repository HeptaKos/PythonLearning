from abc import ABC

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import requests


def translation(path):
    return


class result_handler(RequestHandler):
    def get(self,picture_data):
        with open("image.jpg","wb") as f:
            f.write(picture_data)
        result = translation("image.jpg")
        data = {
            "result_word": result,
        }
        requests.post("pi_url", data)


if __name__ == '__main__':
    app = Application(
        [
            (r'/upload', upload_handler),
        ]
    )

    http_server = HTTPServer(app)
    http_server.listen(8000)
    IOLoop.current().start()
