from MessageOrigin import MessageOrigin
from Message import Message
from Logger import Logger

import threading 

class Log:
    def __init__(self):
        self.__loggerInstance = None

    def get_logger(self):
        # Double locking for unnecessary lock uncalled for - optimization
        if(self.__loggerInstance is None):
            lock = threading.Lock()
            lock.acquire()
            if(self.__loggerInstance is None):
                self.__loggerInstance = Logger()
            lock.release()
        return self.__loggerInstance

if __name__ == "__main__":
    log = Log()
    logger = log.get_logger()
    warnMessage = Message("warning message", MessageOrigin.DB)
    logger.warn(warnMessage)
    warnMessage = Message("warning message", MessageOrigin.CONSOLE)
    logger.warn(warnMessage)

    infoMessage = Message("info message", MessageOrigin.CONSOLE)
    logger.info(infoMessage)
    warnMessage = Message("info message", MessageOrigin.FILE)
    logger.info(infoMessage)
    logger.get_logs()