import multiprocessing as mp
import time
import socket


timeout = 1


# TODO Move it yo utils or somerhing
def check_port(host: str, port: int, results: mp.Queue):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    if result == 0:
        results.put(port)
    sock.close()


if __name__ == "__main__":
    start = time.time()
    processes = []
    scan_range = range(80, 100)
    host = 'localhost'
    mp.set_start_method('spawn')
    pool_manager = mp.Manager()
    with mp.Pool(len(scan_range)) as pool:
        outputs = pool_manager.Queue()
        for port in scan_range:
            processes.append(pool.apply_async(check_port,
                                              (host, port, outputs)))

        for process in processes:
            process.get()

        while not outputs.empty():
            print(f'Port  {outputs.get()} is open')

        print(f'Completed scan in {time.time() - start}')
