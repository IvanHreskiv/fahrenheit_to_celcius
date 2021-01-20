import time
import asyncio

timeout = 1.0


async def check_port(host: str, start: int, end: int, max_=10):
    found = 0
    for port in range(start, end):
        try:
            future = asyncio.open_connection(host=host, port=port)
            r, w = await asyncio.wait_for(future, timeout=timeout)
            yield port
            found += 1
            w.close()
            if found >= max_:
                return
        except (asyncio.TimeoutError, OSError,):
            pass # port is closed, skip-and-continue


async def scan(start, end, host):
    results = []
    async for port in check_port(host, start, end, max_=1):
        results.append(port)
    return results


if __name__ == '__main__':
    start = time.time()
    host = "localhost" # pick a host you own
    results = asyncio.run(scan(80, 100, host))
    for result in results:
        print("Port {0} is open".format(result))
    print("Completed scan in {0} seconds".format(time.time() - start))
