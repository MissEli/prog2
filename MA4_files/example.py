
from time import perf_counter as pc
from time import sleep as pause
# import multiprocessing as mp   # parallellprogrammering
import concurrent.futures as future   # parallellprogrammering/multithreading


def runner(n):
    # print("Performing a costly function")
    # pause(1)
    # print("Function complete")
    print(f"Performing costly function {n}")
    pause(n)
    return f"Function {n} has completed"


if __name__ == "__main__":
    # start = pc()
    # runner()
    # end = pc()
    # print(f"Process took {round(end-start, 2)} seconds")

    # start = pc()
    # for _ in range(10):
    #     runner()
    #     end = pc()
    #     print(f"Process took {round(end-start, 2)} seconds")

    # start = pc()
    # p1 = mp.Process(target=runner)
    # p2 = mp.Process(target=runner)
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    # end = pc()
    # print(f"Process took {round(end-start, 2)} seconds")

    start = pc()
    # with future.ProcessPoolExecutor() as ex:  # parallellprogrammering
    with future.ThreadPoolExecutor() as ex:     # multithreading
        
        p = [5, 4, 3, 2, 1]
        results = ex.map(runner, p)

        for r in results:
            print(r)
    end = pc()
    print(f"Process took {round(end-start,2)} seconds") # Will be printed once all processes are completed

# För 10 parallella körningar
# processes = []
# for _ in range(10):
#     p = mp.Process(target=some_method, args=[some_var])
#     processes.append(p)
# for p in processes:
#     p.start()
# for p in processes:
#     p.join()