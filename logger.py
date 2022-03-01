import os
from datetime import datetime
import unittest
from unittest.mock import patch


def get_log_file(log_file_name="gameplay.log"):
    return log_file_name


def log(module_name, log_line):
    """
    Log module name and log line
    Parameters:
        module_name(str): Module name
        log_line(str): Log Line
    Returns: None
    """
    open(get_log_file(), 'a+').write(f'{datetime.now()} - {module_name} - {log_line}\n')


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
