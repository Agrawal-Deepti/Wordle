from datetime import datetime


def log(module_name, log_line):
    open("gameplay.log", 'a+').write(f'{datetime.now()} - {module_name} - {log_line}\n')



