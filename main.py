import logging
from time import time
from multiprocessing import cpu_count, Pool
from concurrent.futures import ProcessPoolExecutor

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def factorize(*args):
    return [
        [digit for digit in range(1, number // 2 + 1) if number % digit == 0] + [number]
        for number in args
    ]


if __name__ == "__main__":

    logger.debug("Synchronous execution: ")
    before = time()
    result = factorize(128, 255, 99999, 10651060)
    logger.debug(f"Time: {time() - before}")
    # print(*result)

    logger.debug("Multiprocessing execution: ")
    with Pool() as pool:
        before = time()
        result = pool.map(factorize, (128, 255, 99999, 10651060))
        logger.debug(f"Time: {time() - before}")
        # print(*result)

    logger.debug("Multiprocessing execution: ")
    pool = Pool(1)
    before = time()
    result = pool.apply_async(factorize, (128, 255, 99999, 10651060)).get()
    logger.debug(f"Time: {time() - before}")
        # print(*result)

    logger.debug("With concurrent packet execution: ")
    with ProcessPoolExecutor(max_workers=1) as executor:
        before = time()
        result = executor.map(factorize, (128, 255, 99999, 10651060))
        logger.debug(f"Time: {time() - before}")
        # print(*result)
