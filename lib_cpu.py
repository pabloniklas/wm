from multiprocessing import Pool, cpu_count

def parallel_process(func, data):
    with Pool(cpu_count()) as pool:
        pool.map(func, data)
