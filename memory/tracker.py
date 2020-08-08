import psutil

class Tracker:

    def get_process_info(self):
        processes = []

        for process in psutil.process_iter():
            processes.append(process)
        
        return processes

    



tracker = Tracker()
processes=tracker.get_process_info()
for process in processes:
    print(process.keys())

