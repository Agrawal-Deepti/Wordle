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
        return f"Module is {self.module_name} anf log file name is {self.log_file_name}"

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
                log_file.write(f'{datetime.now()} - {self.module_name} - {log_line}\n')
        finally:
            log_file.close()


class LoggerTest (unittest.TestCase):

    def test_log_file_created_sucessfully_positive(self) -> None:
        """Test file gets created"""
        test_file_path = 'testgameplay.log'
        with patch("logger.get_log_file") as patched_function:
            patched_function.return_value = test_file_path
            log("logger", "test case")
        self.assertTrue(os.path.exists(test_file_path))

    def test_log_file_created_sucessfully_Negative(self) -> None:
        """Test file gets created"""
        test_file_path = 'testgameplay.log'
        with patch("logger.get_log_file") as patched_function:
            patched_function.return_value = test_file_path
            log("logger", "test case")
        self.assertFalse(not os.path.exists(test_file_path))

    def test_logs_are_getting_appended_positive(self) -> None:
        """Test file gets created"""
        test_file_path = 'testgameplay.log'
        log("logger", "test case")
        self.assertTrue(open(test_file_path, "r").readline() != "")
