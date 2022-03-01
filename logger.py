from datetime import datetime


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
