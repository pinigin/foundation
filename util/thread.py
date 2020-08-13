import threading


def run_in_new_thread(daemon, name, target):
	threading.Thread(daemon=daemon, name=name, target=target).start()
