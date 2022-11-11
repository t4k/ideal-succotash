import logging

import rpyc

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class SuccotashService(rpyc.Service):
    def on_connect(self, conn):
        # code that runs when a connection is created
        # (to init the service, if needed)
        print("client connected")
        pass

    def on_disconnect(self, conn):
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        print("client disconnected")
        pass

    def exposed_start(self, choice, logtime):
        LOGFILE = f"{choice}-{logtime}.log"
        fh = logging.FileHandler(LOGFILE)
        logger.addHandler(fh)
        self.write_log1(choice)
        self.write_log2(choice)
        self.write_log3(choice)
        return

    def write_log1(self, choice):
        logger.info(f"{choice} log")
        return

    def write_log2(self, choice):
        import time

        i = 10
        while i > 0:
            logger.info(f"{choice} {i}")
            time.sleep(1)
            i -= 1
        return

    def write_log3(self, choice):
        logger.info(f"{choice} 😵")
        return


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    server = ThreadedServer(SuccotashService(), port=18861)
    server.start()
