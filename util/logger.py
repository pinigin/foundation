import os
from threading import Lock
import traceback

from src.foundation.util.time import get_time


class Log:
    _lock = Lock()

    def __init__(self, name: str):
        self.name = name

    def _log(self, log_type, text):
        text = str(text)
        date_time = get_time()
        date = f"{date_time.day}.{date_time.month}.{date_time.year}"
        time = f"{date_time.hour}:{date_time.minute}:{date_time.second}.{date_time.microsecond}:"

        with self._lock:
            if os.path.isdir("data/log"):
                with open(f"data/log/{date}.log", 'a', encoding="UTF-8") as file:
                    try:
                        file.write(f"{time}: {log_type}:{self.name} {text} \n")
                    except UnicodeEncodeError as e:
                        self.exception(e)
        print(f"{date} {time}: {log_type}:{self.name} {text}")

    def _log_raw(self, text):
        text = str(text)
        date_time = get_time()
        date = f"{date_time.day}.{date_time.month}.{date_time.year}"

        with self._lock:
            with open(f"data/log/{date}.log", 'a') as file:
                try:
                    file.write(f"{text} \n")
                except UnicodeEncodeError as e:
                    self.exception(e)
        print(f"{text}")

    def warning(self, text):
        log_type = "WARNING"
        self._log(log_type, text)

    def info(self, text):
        log_type = "INFO"
        self._log(log_type, text)

    def debug(self, text):
        log_type = "DEBUG"
        self._log(log_type, text)

    def exception(self, text):
        log_type = "EXCEPTION"
        self._log(log_type, text)
        trace = traceback.format_exc()
        self._log_raw(trace)

    def error(self, text):
        log_type = "ERROR"
        self._log(log_type, text)

    def critical(self, text):
        log_type = "CRITICAL"
        self._log(log_type, text)


def get_logger(name: str):
    logger = Log(name)
    return logger
