import threading
import logging
import time
import random


lock = threading.Lock()
sec_rand = random.SystemRandom()
threads = []

class thread(threading.Thread):
    lock1=threading.Lock()
    lock1.acquire()
    lock2=threading.Lock()
    lock2.acquire()
    def __init__(self,val):
        threading.Thread.__init__(self)
        self.param = val

    def run(self):
        if self.param == 1:
            self.thread1()
        else:
            self.thread2()



    def thread1(self):
        threads.append(self)
        name = threading.current_thread().getName()
        rand_float = sec_rand.uniform(0.1, 3)
        logging.debug('%s sleeps %s', name, round(rand_float, 2))
        time.sleep(rand_float)
        thread.lock1.release()
        logging.debug('%s has Arrived', name)
        thread.lock2.acquire()
        threads.remove(self)

    def thread2(self):
        threads.append(self)
        name = threading.current_thread().getName()
        rand_float = sec_rand.uniform(0.1, 3)
        logging.debug('%s sleeps %s', name, round(rand_float, 2))
        time.sleep(rand_float)
        thread.lock2.release()
        logging.debug('%s has Arrived', name)
        thread.lock1.acquire()
        threads.remove(self)



if __name__ == "__main__":
    format = "%(asctime)s: %(threadName)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")

    thread1 = thread(1)
    thread2 = thread(2)

    thread1.start()
    thread2.start()

    for t in threads:
        thread1.join()
        thread2.join()
    logging.debug('Both threads finished rendezvous')


