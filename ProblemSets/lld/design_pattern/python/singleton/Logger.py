from Message import Message
from MessageOrigin import MessageOrigin
from MessageType import MessageType
class Logger:
    instances = 0
    def __init__(self):
        Logger.instances += 1
        self.__sinkPaths = {
            MessageType.WARN: {
                MessageOrigin.DB: [],
                MessageOrigin.FILE: [],
                MessageOrigin.CONSOLE: []
            },
            MessageType.ERROR: {
                MessageOrigin.DB: [],
                MessageOrigin.FILE: [],
                MessageOrigin.CONSOLE: []
            },
            MessageType.FATAL: {
                MessageOrigin.DB: [],
                MessageOrigin.FILE: [],
                MessageOrigin.CONSOLE: []
            },
            MessageType.INFO: {
                MessageOrigin.DB: [],
                MessageOrigin.FILE: [],
                MessageOrigin.CONSOLE: []
            }
        }
    def warn(self, message):
        self.__log(message, MessageType.WARN)

    def info(self, message):
        self.__log(message, MessageType.INFO)
    
    def error(self, message):
        self.__log(message, MessageType.ERROR)
    
    def fatal(self, message):
        self.__log(message, MessageType.FATAL)
    
    def __log(self, message, msgType):
        self.__sinkPaths.get(msgType).get(message.getOrigin()).append(message.getMessage() + " " + str(message.getTime()) + " instance Number: " + str(Logger.instances))
    
    def get_logs(self):
        for msgType in self.__sinkPaths.keys():
            for msgOrigin in MessageOrigin:
                logs = self.__sinkPaths[msgType][msgOrigin]
                for log in logs:
                    print(log)