import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        control = self.get_argument('control', '')
        print(control)
        self.write("ok")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print ('server running: 0.0.0.0:8888')
    tornado.ioloop.IOLoop.current().start()
