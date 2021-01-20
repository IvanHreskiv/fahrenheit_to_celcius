import time
import _xxsubinterpreters as subinterpreters
import textwrap as tw

from threading import Thread
from queue import Queue


timeout = 1


def run(host: str, port: int, result: Queue):
    # Create a communication chanel
    channel_id = subinterpreters.channel_create()
    interid = subinterpreters.create()
    subinterpreters.run_string(
        interid,
        tw.dedent(
        """
        import socket; import _xxsubinterpreters as subinterpreters
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        subinterpreters.channel_send(channel_id, result)
        sock.close()
        """),
        shared={
            "channel_id": channel_id,
            "host": host,
            "port": port,
            "timeout": timeout
        }
    )
    output = subinterpreters.channel_recv(channel_id)
    subinterpreters.channel_release(channel_id)
    if output == 0:
        result.put(port)


if __name__ == "__main__":
    start = time.time()
    host = "127.0.0.1"
    threads = []
    results = Queue()

    for port in range(80, 100):
        t = Thread(target=run, args=(host, port, results))
        t.start()
        threads.append(t)

    for item in threads:
        item.join()

    while not results.empty():
        print("Port {0} is open".format(results.get()))
    print("Completed scan in {0} seconds".format(time.time() - start))
