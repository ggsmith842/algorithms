from concurrent.futures import ProcessPoolExecutor, as_completed
from time import sleep, time


# define a cpu intensive process as those are the most beneficial from multicore processing vs multithread.
def cpu_intensive_process(taskid: int):
    sleep(5) # simulate waiting for a computaion to complete
    return f"task with id {taskid} complete"

if __name__ == '__main__':

    tasks = [1, 2, 3, 4]

    # iterative example and time (expected to take approx. 20 seconds)
    start = time()
    for task in tasks:
        print(cpu_intensive_process(taskid=task))
    end = time() - start
    print(f'Total Execution time: {end}s')    

    
    # parallel process using multiple cores
    start = time()
    with ProcessPoolExecutor() as executor:

        for task, status in zip(tasks, executor.map(cpu_intensive_process, tasks)):
            print(task, status)

    end = time() - start
    print(f'Total Execution time: {end}s')





