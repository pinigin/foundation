import datetime


def get_time() -> datetime.datetime:
    date = datetime.datetime.now()

    return date


class Timer:
    __start_time = datetime.datetime.now()

    @classmethod
    def start(cls):
        cls.__start_time = datetime.datetime.now()

    @classmethod
    def stop(cls):
        return datetime.datetime.now() - cls.__start_time


def timeit(method):
    def timed(*args, **kw):
        ts = datetime.datetime.now()
        result = method(*args, **kw)
        te = datetime.datetime.now()
        print(f'{method.__name__}  {te - ts}')
        return result
    return timed
