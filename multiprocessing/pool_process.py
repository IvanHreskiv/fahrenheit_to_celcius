import multiprocessing as mp
import multiprocessing.spawn
import pprint
from to_celcius import to_celcius, DATA


if __name__ == '__main__':
    pprint.pprint(mp.spawn.get_preparation_data("example"))
    with mp.Pool(4) as pool:
        pool.map(to_celcius, DATA)
