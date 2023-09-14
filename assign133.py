import time


def time_runs():
    start_time = time.time()

    end_time = time.time()
    time_taken = end_time - start_time

    return time_taken


if __name__ == "__main__":
    print("Starting the program.")
    elapsed_time = time_runs()
    print(f"Time taken: {elapsed_time:.6f} seconds.")
