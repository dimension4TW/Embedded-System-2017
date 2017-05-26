import tornado.ioloop
import tornado.web
import RPi.GPIO as go
import time

go.cleanup()


go.setmode(go.BOARD)
# for car's movement
go.setup(7,  go.OUT)
go.setup(11, go.OUT)
go.setup(13, go.OUT)
go.setup(15, go.OUT)


def front(t):
    go.output(7, False)
    go.output(11,True)
    go.output(13, True)
    go.output(15,False)
    time.sleep(t)

def rear(t):
    go.output(7, True)
    go.output(11,False)
    go.output(13, False)
    go.output(15,True)
    time.sleep(t)
    
def left(t):
    go.output(7, True)
    go.output(11,False)
    go.output(13, True)
    go.output(15,False)
    time.sleep(t)
    
def right(t):
    go.output(7, False)
    go.output(11,True)
    go.output(13,False)
    go.output(15,True)
    time.sleep(t)


class MainHandler(tornado.web.RequestHandler):
    def post(self):
        global mode 
        control = self.get_argument('control', '')
        print(control)
        if control == 'w':
            front(0.5)
        elif control == 'a': 
            left(0.5)
        elif control == 's':
            rear(0.5)
        elif control == 'd':
            right(0.5)
        elif control == 'q':
            if(mode=="mode1"):
                mode = "mode2"
            else:
                mode = "mode1"
            print "now is in "+mode
            
        self.write("ok")
    
    def get(self):
        self.write(mode) 

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print ('server running: 0.0.0.0:8888')
    global mode 
    mode = "mode1"
    tornado.ioloop.IOLoop.current().start()
