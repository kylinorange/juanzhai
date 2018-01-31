import time

class Timer:
    def __init__(self, process_name, verbose=1):
        self.process_name = process_name
        self.verbose = verbose

    def __enter__(self):
        if self.verbose:
            print(self.process_name + " started.")
            self.begin_time = time.time()

    def __exit__(self, type, value, traceback):
        if self.verbose:
            end_time = time.time()
            # print(self.process_name + " ended.")
            print('{}: {:.2f}s'.format(self.process_name, end_time - self.begin_time))
