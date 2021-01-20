import os
import multiprocessing as mp


DATA = range(110, 150, 10)


def to_celcius(f):
    c = (f - 32) * (5/9)
    pid = os.getpid()
    print(f"{f}F is {c}C (pid {pid})")
    return c


def to_celcius_with_queue(input_: mp.Queue, output: mp.Queue):
    print(f'Queue size: {input_.qsize()}')
    output.put(to_celcius(input_.get()))


def to_celcius_with_pipe(
    child_pipe: mp.Pipe, parent_pipe: mp.Pipe,
    child_write_lock: mp.Lock, parent_read_lock: mp.Lock
):
    pid = os.getpid()

    parent_read_lock.acquire()
    try:
        f = parent_pipe.recv()
    finally:
        parent_read_lock.release()

    # time-consuming task ...
    c = (f - 32) * (5/9)

    child_write_lock.acquire()
    try:
        child_pipe.send(c)
    finally:
        child_write_lock.release()

    print(f"{f}F is {c}C (pid {pid})")


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))


def recur_fibo_with_queue(input_: mp.Queue, output: mp.Queue):
    while not input_.empty():
        print(f'Queue size: {input_.qsize()}')
        # TODO: Make it decorator
        pid = os.getpid()
        print(f"pid {pid}")

        output.put(recur_fibo(input_.get()))


def reader(q):
    pid = os.getpid()
    message = q.get(block=False)
    # block is false return an item if one is immediately available,
    # else raise the Empty exception (timeout is ignored in that case).
    print(f"Message: {message} (pid {pid})")
