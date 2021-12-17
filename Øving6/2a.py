import threading
import time
import logging



def helloWorld(num):
    logging.info("Hello world from thread %s", num)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    num = 2
    print("Starting Threads")
    for i in range(num):
        i+=1
        thread = threading.Thread(target=helloWorld(i), args=(1,))
        thread.start
    print("Finishing program")


