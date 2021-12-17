import threading
import time
import logging

must_run = True
x = 1
lock = threading.Lock()


def reader():
    global x, must_run
    must_run=False
    name = threading.current_thread().getName()
    logging.debug('Reader %s is reading', name)
    lock.acquire()
    logging.debug('Shared data: %s', x)
    time.sleep(1)
    lock.release()
    print()
    must_run=True
    print_menu()


def read():
    global must_run
    thread1 = threading.Thread(target=reader)
    thread1.start()



def writer():
    global x, must_run
    must_run = False
    name = threading.current_thread().getName()
    logging.debug('Writer %s is writing', name)
    lock.acquire()
    try:
        x = int(input('Please enter a number\n'))
        logging.debug('Writer %s is releasing the lock\n', name)
        lock.release()
        must_run=True
        print_menu()
        print()
    except ValueError:
        logging.debug('Not a valid number\n')
        logging.debug('Please start over \n')
        lock.release()
        must_run=True
        print_menu()
        print()

def write():
    global must_run
    thread2 = threading.Thread(target=writer)
    thread2.start()


def quit():
    global must_run
    must_run = False


actions = [
    {
        "Type":"Reader",
        "function": read
    },
    {
        "Type":"Writer",
        "function": write
    },
    {
        "Type":"Log Out",
        "function": quit
    }]


def print_menu():
    print("==============================================")
    print("What do you want to do now? ")
    print("==============================================")
    print("Available options:")
    i = 1
    for a in actions:
        print("  %i) %s" % (i, a["Type"]))
        i += 1
    print()
    number_of_actions = len(actions)
    hint = "Enter the number of your choice (1..%i):" % number_of_actions
    choice = input(hint)
    try:
        choice_int = int(choice)
    except ValueError:
        choice_int = -1
    if 1 <= choice_int <= number_of_actions:
        action = choice_int - 1
        function_to_run = actions[action]["function"]
        if function_to_run is not None:
            function_to_run()
    else:
        print("Invalid input, please choose a valid action")


if __name__ == "__main__":
    format = "%(asctime)s: %(threadName)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")
    while must_run:
        print_menu()
        time.sleep(1)