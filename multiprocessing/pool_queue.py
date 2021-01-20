import multiprocessing as mp
from to_celcius import to_celcius_with_queue, DATA, reader


if __name__ == '__main__':
    mp.set_start_method('spawn')
    pool_manager = mp.Manager()

    with mp.Pool(2) as pool:
        inputs = pool_manager.Queue()
        outputs = pool_manager.Queue()

        for item in list(DATA):
            inputs.put(item)

        while not inputs.empty():
            pool.apply(to_celcius_with_queue, (inputs, outputs,))

        while not outputs.empty():
            pool.apply(reader, (outputs,))
