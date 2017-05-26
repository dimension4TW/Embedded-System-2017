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
    go.output(7, False)
    go.output(11,False)
    go.output(13, False)
    go.output(15,False)

def rear(t):
    go.output(7, True)
    go.output(11,False)
    go.output(13, False)
    go.output(15,True)
    time.sleep(t)
    go.output(7, False)
    go.output(11,False)
    go.output(13, False)
    go.output(15,False)
    
def left(t):
    go.output(7, True)
    go.output(11,False)
    go.output(13, True)
    go.output(15,False)
    time.sleep(t)
    go.output(7, False)
    go.output(11,False)
    go.output(13, False)
    go.output(15,False)
    
def right(t):
    go.output(7, False)
    go.output(11,True)
    go.output(13,False)
    go.output(15,True)
    time.sleep(t)
    go.output(7, False)
    go.output(11,False)
    go.output(13, False)
    go.output(15,False)
    
def stop():
    go.output(7, False)
    go.output(11,False)
    go.output(13, False)
    go.output(15,False)

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        global mode 
        control = self.get_argument('control', '')
        print(control)
        if control == 'w' and mode == 'mode2':
            front(0.5)
        elif control == 'a'and mode == 'mode2': 
            left(0.5)
        elif control == 's'and mode == 'mode2':
            rear(0.5)
        elif control == 'd'and mode == 'mode2':
            right(0.5)
        elif control == 'q':
            if(mode=="mode1"):
                mode = "mode2"
            else:
                mode = "mode1"
        else:
            stop()
            
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
