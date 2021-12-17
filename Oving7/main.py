import threading
import logging
import time
from random import randint


lock = threading.Lock()
def threadA():
    name = threading.current_thread().getName()
    logging.debug('%s has Arrived', name)
    lock.acquire
    time.sleep(randint(0, 3))


def threadB():
    name = threading.current_thread().getName()
    logging.debug('%s has Arrived', name)
    lock.acquire
    time.sleep(randint(0, 3))




if __name__ == "__main__":
    format = "%(asctime)s: %(threadName)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")
    thread1 = threading.Thread(target=threadA)
    thread2 = threading.Thread(target=threadB)
    thread1.start()
    thread2.start()