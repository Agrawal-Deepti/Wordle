import os
from datetime import datetime
from typing import IO
import unittest
from unittest.mock import patch


class Logger(object):

    def __init__(self, module_name, log_file_name="gameplay.log"):
        self.module_name = module_name
        self.log_file_name = log_file_name

    def __str__(self):
        return f"Module is {self.get_module_name()} anf log file name is {self.get_log_file()}"

    def get_module_name(self):
        return self.module_name

    def get_log_file(self):
        return self.log_file_name

    def log(self, log_line):
        """
        Log module name and log line
        Parameters:
            log_line(str): Log Line
        Returns: None
        """
        try:
            log_file: IO = open(self.get_log_file(), 'a+')
        except FileNotFoundError:
            print(f"Can't open file {self.get_log_file()}")
        else:
            with log_file:
                log_file.write(f'{datetime.now()} - {self.get_module_name()} - {log_line}\n')
        finally:
            log_file.close()


class LoggerTest (unittest.TestCase):

    def test_log_file_created_sucessfully_positive(self) -> None:
        """Test file gets created"""
        test_file_path = 'testgameplay.log'
        __logger = Logger("Logger", test_file_path)
        __logger.log("test case1 - test_log_file_created_sucessfully_positive")
        self.assertTrue(os.path.exists(test_file_path))

    def test_log_file_created_sucessfully_Negative(self) -> None:
        """Test file gets created"""
        test_file_path = 'testgameplay.log'
        __logger = Logger("Logger", test_file_path)
        __logger.log("test case2 - test_log_file_created_sucessfully_Negative")
        self.assertFalse(not os.path.exists(test_file_path))

    def test_logs_are_getting_appended_positive(self) -> None:
        """Test file gets created"""
        test_file_path = 'testgameplay.log'
        __logger = Logger("Logger", test_file_path)
        __logger.log("test case3 - test_logs_are_getting_appended_positive")
        self.assertTrue(open(test_file_path, "r").readline() != "")
