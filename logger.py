import logging
import colorlog


def Singleton(cls):
    _instance = {}
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton

@Singleton
class Logger:
    def __init__(self)->None:    
        self.log_colors_config = {
            'DEBUG': 'white',  
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }
        self.logger = logging.getLogger('logger_name')
        self.console_handler = logging.StreamHandler()
        self.logger.setLevel(logging.DEBUG)
        self.console_handler.setLevel(logging.DEBUG)
        self.console_formatter = colorlog.ColoredFormatter(
            fmt='%(log_color)s[%(asctime)s.%(msecs)03d] -> [%(levelname)s] : %(message)s',
            datefmt='%Y-%m-%d  %H:%M:%S',
            log_colors=self.log_colors_config
        )
        self.console_handler.setFormatter(self.console_formatter)
        if not self.logger.handlers:
            self.logger.addHandler(self.console_handler)
        self.console_handler.close()

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