from datetime import datetime


def log(module_name, log_line):
    """
    Log module name and log line
    Parameters:
        module_name(str): Module name
        log_line(str): Log Line
    Returns: None
    """
    open("gameplay.log", 'a+').write(f'{datetime.now()} - {module_name} - {log_line}\n')



