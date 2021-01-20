import multiprocessing as mp


from to_celcius import to_celcius


if __name__ == '__main__':
    mp.set_start_method('spawn')  # Could be ['spawn', 'fork', 'forkserver']
    # The parent process starts a fresh python interpreter process.
    # The child process will only inherit those resources necessary to run the process object’s run() method.
    # In particular, unnecessary file descriptors and handles from the parent process will not be inherited.
    # Starting a process using this method is rather slow compared to using fork or forkserver.

    p = mp.Process(target=to_celcius, args=(110,))
    p.start()
