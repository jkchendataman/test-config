import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        with open("/data/conf/conf.ini", "r") as fp:
            content = fp.read()

            self.render('index.html', content=content)


if __name__ == "__main__":
    settings = {
        'template_path': '/data/src/templates',
        'debug': True,
    }
    application = tornado.web.Application([
        (r"/", MainHandler),
    ], **settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()

