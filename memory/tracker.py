import psutil
from datetime import datetime

class ProcessTracker:

    def get_process_info(self):
        processes = []

        for process in psutil.process_iter():
            processes.append(process)
        
        return processes

    def _get_create_time(self, process: psutil.Process):
        # create_time
        pass

    def _get_status():
        # status = process.status()
        pass

    def _get_process_priority(self):
        # nice = int(process.nice())
        pass

    def _get_process_cores(self):
        # cores = len(process.cpu_affinity)
        pass

    def _get_memory_usage(self):
        # memory_usage = process.memory_full_info().uss
        pass

    def _get_process_io_bytes(self, process):
        # io_counters, read_bytes, writes_byte
        pass

    def _get_threads_spawned(self, process):
        # n_threads = process.num_threads()
        pass

    def get_user_who_spawned_process(self, process):
        # username = process.username()
        pass

class ProcessConstructor:

    def get_formatted_size(bytes):
        for unit in ['', 'K', 'M', 'G', 'T', 'O']:
            if bytes < 1024:
                return f"{bytes:.2f}{unit}B"
            bytes /= 1024


tracker = ProcessTracker()
processes=tracker.get_process_info()

print(processes[0].name())
