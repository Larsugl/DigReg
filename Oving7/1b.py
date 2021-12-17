import threading
import logging
import time
import random


N=3
sec_rand = random.SystemRandom()
threads=[]


class thread(threading.Thread):
    def __init__(self, b):
        threading.Thread.__init__(self)
        self.b = b


    def barrier(self):
        rand_float = sec_rand.uniform(0, 3)
        name = threading.current_thread().getName()
        logging.debug('%s going to sleep for %s', name, round(rand_float, 2))
        time.sleep(rand_float)
        threads.append(self)
        if len(threads) < N:
            logging.debug('%s waiting at barrier', name)
        else:
            logging.debug('%s found all %s waiting, opening barrier', name, N)
        self.b.wait()
        logging.debug('%s opening barrier for next thread', name)
        threads.remove(self)
        if len(threads) == 0:
            logging.debug('All threads through barrier')



    def run(self):
        self.barrier()


if __name__ == "__main__":
    format = "%(asctime)s: %(threadName)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")
    barrier = threading.Barrier(N)
    for i in range(N):
        t = thread(barrier)
        t.start()