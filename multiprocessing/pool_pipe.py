import multiprocessing as mp
from to_celcius import to_celcius_with_pipe, DATA

# TODO: Add more loggin

if __name__ == '__main__':
    mp.set_start_method('spawn')
    with mp.Pool(2) as pool:
        parent_pipe, child_pipe = mp.Pipe()
        parent_read_lock = mp.Lock()  # There are two locks required, one on the receiving end of the parent pipe,
        child_write_lock = mp.Lock()  # and another on the sending end of the child pipe

        for item in list(DATA):
            parent_pipe.send(item)
            pool.apply_async(
                to_celcius_with_pipe, args=(
                    child_pipe, parent_pipe, child_write_lock, parent_read_lock
                )
            )
            print(child_pipe.recv())

        parent_pipe.close()
        child_pipe.close()
