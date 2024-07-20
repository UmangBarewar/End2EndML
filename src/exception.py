import sys
from src.logger import logging
# this sys library helps in manipulating python runtime environemnt
# so all the exception error will be handled here

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    #using this exc_tb we can get where the error has occured in which file and what line
    error_message="Error occured in python script number\
            [{0}] line number [{1}] error is : [{2}]".format(
                file_name,exc_tb.tb_lineno,str(error)
            
            )
    return error_message
class CustomException(Exception):
    def __init__(self,error_message,error_detail):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self) -> str:
        return self.error_message
    
# this is the testing code

# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide By zero")
#         raise CustomException(e,sys)
    

    # NOTES:
    # 1.This exception.py file is designed to handle exceptions in a Python project by providing detailed error \
    #     messages that include the filename and line number where the error occurred. Let's go through each \
    #         part of the file and explain its purpose and functionality:
    
    # 2.This function takes two parameters:
    # error: The error that occurred.
    # error_detail: The sys module to get detailed information about the exception.
    # exc_info(): Returns a tuple of three values that give information about the exception that is currently being handled:
    # Type of the exception.
    # Exception instance.
    # Traceback object.
    # The traceback object (exc_tb) provides details about where the exception occurred, including the file name and line number.
    # The function constructs an error message string that includes the file name, line number, and error message.

    # 3.This class inherits from the built-in Exception class to create a custom exception.
    # __init__ method:
    # Initializes the exception with an error_message and error_detail.
    # Calls super().__init__(error_message) to initialize the base Exception class with the error message.
    # Calls error_message_detail to get a detailed error message and assigns it to self.error_message.
    # __str__ method:
    # Overrides the __str__ method to return the detailed error message.
    # This ensures that when the exception is converted to a string (e.g., when printed), it shows the detailed error message.