from logger import Logger
class Box:
    def __init__(self):
        self.logger = Logger()
    
    def debug(self, message:str)->None:
        self.logger.debug(message)

    def info(self, message:str)->None:
        self.logger.info(message)

    def warning(self, message:str)->None:
        self.logger.warning(message)
    
    def error(self, message:str)->None:
        self.logger.error(message)
    
    def critical(self, message:str)->None:
        self.logger.critical(message)