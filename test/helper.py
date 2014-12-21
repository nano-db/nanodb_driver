import zmq
from threading import Thread

class MockServer(Thread):
    def __init__(self, nb_req):
        Thread.__init__(self)
        self.nb_req = nb_req
        context = zmq.Context()
        self.socket = context.socket(zmq.REP)
        self.socket.bind("tcp://127.0.0.1:8000")

    def run(self):
        while self.nb_req > 0:
            msg = self.socket.recv_json()
            cmd = msg.get('cmd')
            ret = self.process_cmd(cmd)
            self.socket.send_json(ret)
            self.nb_req -= 1

    def process_cmd(self, cmd):
        if cmd == "error":
            return {
                'status': "error",
                'error': "Server side issue"
            }
        else:
            return {
                'status': "OK",
                'data': {
                    'every': "thing",
                    'is': ["g", "o", "o", "d"]
                }
            }