import logging
from insertion_sort import insertion_sort
from merge_sort import merge_sort
import timeit
import random

logging.basicConfig(level=logging.INFO, filename='sorting_log.txt', filemode='w')
logger = logging.getLogger(__name__)

SIZES = [500, 1000, 5000]

def generate_random_list(size):
    return [random.randint(0, 1000) for _ in range(size)]

def print_results(size, time_merge, time_insertion, time_timsort):
    logger.info(f"Size: {size}")
    logger.info(f"Insertion Sort Time: {time_insertion:.6f} sec")
    logger.info(f"Merge Sort Time: {time_merge:.6f} sec")
    logger.info(f"Timsort Time: {time_timsort:.6f} sec")
    logger.info("")

def compare_algorithms():
    for size in SIZES:
        random_list = generate_random_list(size)

        time_insertion = timeit.timeit(lambda: insertion_sort(random_list.copy()), number=5)
        time_merge = timeit.timeit(lambda: merge_sort(random_list.copy()), number=5)
        time_timsort = timeit.timeit(lambda: sorted(random_list.copy()), number=5)

        print_results(size, time_merge, time_insertion, time_timsort)

if __name__ == "__main__":
    compare_algorithms()
