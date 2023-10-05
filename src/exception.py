import sys
from src.logger import logging


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # from sys carries information and 3rd value contains which file
    file_name = exc_tb.tb_frame.f_code.co_filename  # extracting the file name
    error_message = (f"Error encountered under Python Script name [{file_name}] "
                     f"line number[{exc_tb.tb_lineno}] with error message [{str(error)}]")
    return error_message


class CustomException(Exception):  # Inheriting from inbuilt Exception class
    def __init__(self, error_message, error_detail: str):  #
        super().__init__(error_message)  # inheriting __init__ function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message


""" FOR CHECKING WORKING FINE
if __name__ == ('__main__'):
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero Error")
        raise CustomException(e, sys) """
