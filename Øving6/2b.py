import threading
import time
import logging

m=2
v = input("Gi meg et heltall under 15!: \n")
maks=15

def increment(num):
        if num < 2:
            try:
                var=int(v)
                for i in range(maks):
                    var += 1
                    if var < maks:
                            print("Starting Threads")
                            logging.info("Thread %s incrementing variable", num)
                            time.sleep(1)
            except ValueError:
                print("Feil input\n")
        else:
            logging.info("Thread %s setting flag", num)
            print("Stopping Threads")

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    print("Starting Threads")
    for i in range(m):
        i += 1
        thread = threading.Thread(target=increment(i), args=(1,))
        thread.start