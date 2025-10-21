from abc import ABC,ABCMeta,abstractmethod
# import logging
# import threading
# class ThreadSafeSingleton(ABCMeta):
#     __instance = {}
#     __lock = threading.Lock()
#     def __call__(cls,*args,**kwargs):
#         with cls.__lock:
#             if cls not in cls.__instance:
#                 cls.__instance[cls] = super().__call__(*args,**kwargs)
#         return cls.__instance[cls]
# class BaseLogger(ABC):
#     @abstractmethod
#     def debug(self,msg):
#         pass
#     @abstractmethod
#     def info(self,msg):
#         pass
#     @abstractmethod
#     def error(self,msg):
#         pass
#     @abstractmethod
#     def warning(self,msg):
#         pass

# class LoggerSystem(BaseLogger,metaclass=ThreadSafeSingleton):
#     def __init__(self,app_name):
#         self.app_name = app_name
#         self.__logger = self.get_or_create_logger()
    
#     def get_or_create_logger(self):
        
#         logger = logging.getLogger(self.app_name)
#         logger.setLevel(logging.DEBUG)
#         formatter = logging.Formatter('%(name)s=========%(message)s')
        
#         if logger.hasHandlers():
#             return logger
        
#         streaming_handler =  logging.StreamHandler()
#         streaming_handler.setFormatter(formatter)
        
#         file_handler = logging.FileHandler('sss.txt')
#         file_handler.setFormatter(formatter)
                
#         logger.addHandler(streaming_handler)
#         logger.addHandler(file_handler)
        
        
#         return logger
        
#     def debug(self,msg):
#         return self.__logger.debug(msg)
        
#     def info(self,msg):
#         return self.__logger.info(msg)
        
#     def warning(self,msg):
#         return self.__logger.warning(msg)
    
#     def error(self,msg):
#         return self.__logger.error(msg)
        
# if __name__ == "__main__":
#     obj = LoggerSystem('s')
#     obj1 = LoggerSystem('s')
#     print(id(obj),id(obj1))
#     obj.debug("hello")
#     obj.info("go")
#=============================factory
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class CreditCardPayment(PaymentGateway):
    def pay(self,amount):
        return f'Credit card payment done {amount}'

class DebitCardPayment(PaymentGateway):
    def pay(self,amount):
        return f'debit card payment done {amount}'

class PaypalPayment(PaymentGateway):
    def pay(self,amount):
        return f'paypal card payment done {amount}'

class PaymentGatewayInterface:
    _gateway = {}
    
    @classmethod
    def get_gateway(cls,name):
        if name.lower() in cls._gateway:
            return cls._gateway[name.lower()]
    @classmethod
    def register_gateway(cls,name,gateway):
        if name.lower() not in cls._gateway:
            cls._gateway[name] = gateway()

            
PaymentGatewayInterface.register_gateway("credit",CreditCardPayment)
PaymentGatewayInterface.register_gateway("debit",DebitCardPayment)
PaymentGatewayInterface.register_gateway("paypal",PaypalPayment)


payment_interface =  PaymentGatewayInterface.get_gateway('credit')
print(payment_interface.pay(1000))
