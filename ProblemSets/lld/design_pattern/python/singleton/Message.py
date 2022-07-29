import time
class Message:
    """
    Init @ Message
    """
    def __init__(self, msg, origin):
        self.__msg = msg
        self.__origin = origin
        self.__time = time.time()
    """
    message @ Message
    """
    def getMessage(self):
        return self.__msg
    """
    Origin @ Message
    """
    def getOrigin(self):
        return self.__origin
    """
    Time @ Message
    """
    def getTime(self):
        return self.__time