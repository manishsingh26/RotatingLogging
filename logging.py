
import logging
from logging.handlers import RotatingFileHandler

def logger_executor(self):
    """
    Creates a rotating log
    """
    logger = logging.getLogger(self.logger_name)
    logger.setLevel(level=self.logger_level)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s")
    handler = RotatingFileHandler(self.logger_file, maxBytes=10*1024*1024, backupCount=5)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
  
