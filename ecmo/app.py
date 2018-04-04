import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.auth
import tornado.gen
import tornado.concurrent

from ecmo.config import PORT
from ecmo.config import KEYCLOAK_OPENID_CONFIG, KEYCLOAK_CLIENT_ID, KEYCLOAK_CLIENT_SECRET



class BaseHandler(tornado.web.RequestHandler):
    pass


class MainHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self):
        self.write("Hello, world")


def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(PORT)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
