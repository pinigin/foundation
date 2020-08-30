import threading


def run_in_new_thread(daemon, name, target, *args, **kwargs):
	threading.Thread(daemon=daemon, name=name, target=target, *args, **kwargs).start()
