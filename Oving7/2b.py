import threading
import logging
import random
from threading import Timer, Lock

locks = [Lock() for i in range(2)]
deadlock_detected = False
N=3

class watchdog(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def worker(self):
        global deadlock_detected
        name = threading.current_thread().getName()
        logging.debug('%s has started', name)
        i = random.randint(0,1)
        j = random.randint(0,1)
        logging.debug('%s requesting lock %s & %s', name, i+1, j+1)

        locks[i].acquire()
        locks[j].acquire()
        if i != j:
            locks[i].release()
            locks[j].release()
            deadlock_detected = False
        else:
            logging.debug('Worker thread exiting due to deadlock')



    def run(self):
        self.worker()


def watchdog_function():
    global deadlock_detected

    logging.debug('Watchdog timer expired, releasing locks')
    if locks[0].locked():
        locks[0].release()
        logging.debug('Releasing lock 1')
    else:
        locks[1].release()
        logging.debug('Releasing lock 2')
    deadlock_detected = True

def run():
    n=0
    for i in range(N):
        watchdog_timer = Timer(3.0, watchdog_function)
        watchdog_timer.setName('Watchdog Thread')
        watchdog_timer.start()
        worker = watchdog()
        n+=1
        worker.setName("Worker Thread " + str(n))
        worker.start()
        worker.join()
        watchdog_timer.cancel()



if __name__ == "__main__":
    format = "%(asctime)s: %(threadName)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")

    run()
    while deadlock_detected == True:
        run()
    else:
        logging.debug('Worker threads finished without deadlocks')