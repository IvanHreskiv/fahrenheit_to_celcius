import time
import socket
from threading import Thread
from queue import Queue

timeout = 1


# TODO Move it yo utils or somerhing
def check_port(host: str, port: int, results: Queue):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    if result == 0:
        results.put(port)
    sock.close()


if __name__ == "__main__":
    start = time.time()
    threads = []
    scan_range = range(80, 100)
    host = 'localhost'
    outputs = Queue()

    for port in scan_range:
        thread = Thread(target=check_port, args=(host, port, outputs))
        thread.start()
        threads.append(thread)

    for item in threads:
        item.join()

    while not outputs.empty():
        print(f'Port  {outputs.get()} is open')

    print(f'Completed scan in {time.time() - start}')
