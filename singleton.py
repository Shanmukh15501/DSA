import logging
from abc import ABC, abstractmethod, ABCMeta
import threading

# Thread-safe Singleton Metaclass
class ThreadSafeSingleton(ABCMeta):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
		


# Interface for Logger
class BaseLogger(ABC):
    @abstractmethod
    def debug(self, message): pass

    @abstractmethod
    def info(self, message): pass

    @abstractmethod
    def warning(self, message): pass

    @abstractmethod
    def error(self, message): pass
	
class LoggerSystem(BaseLogger, metaclass=ThreadSafeSingleton):
    """
        LoggerSystem is a class which deals with invoking the logger methods
        Methods :- 
            _get_or_create_logger :- Helps to get or create the logger instance
            debug :- This Functions reads the level 10 logger data
            info :- This Functions reads the level 20 logger data
            error :- This Functions reads the level 40 logger data
            warning :- This Functions reads the level 30 logger data

    """
    def __init__(self):
        self.app_name = 'CodeGeN'
        self.level = logging.DEBUG  
        self.formatter = '[%(asctime)s] %(levelname)s - %(message)s]'
        self._logger = self._get_or_create_logger()
        
    def _get_or_create_logger(self):
        logger = logging.getLogger(self.app_name)
        logger.setLevel(self.level)

        if logger.hasHandlers():
            return logger

        formatter = logging.Formatter(self.formatter)

        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # File Handler
        file_handler = logging.FileHandler('app.log', mode='a')
        file_handler.setFormatter(formatter)

        # Add handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        return logger
    
    def debug(self, message):
        return self._logger.debug(message)
    def error(self, message):
        return self._logger.error(message)
    def warning(self, message):
        return self._logger.warning(message)
    def info(self, message):
        return self._logger.info(message)

