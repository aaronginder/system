import psutil
from datetime import datetime

class ProcessTracker:

    def get_process_info(self):
        processes = []

        for process in psutil.process_iter():
            pid = self._get_pid(process)
            name = self._get_process_name(process)
            create_time = self._get_create_time(process)
            status = self._get_status(process)
            priority = self._get_process_priority(process)
            cores = self._get_process_cores(process)
            cpu_usage = self._get_cpu_percent(process)
            memory = self._get_memory_usage(process)
            # read_bytes, read_count, write_bytes, write_count = self._get_process_io_bytes(process)
            threads = self._get_threads_spawned(process)
            user = self.get_user_who_spawned_process(process)

            processes.append({
                'pid': pid, 'name': name, 'create_time': create_time, 'cores': cores, 'cpu_usage': cpu_usage, 'status': status, 'priority': priority,
                'memory_usage': memory,
                # 'read_bytes': read_bytes, 'read_count': read_count, 'write_bytes': write_bytes, 'write_count': write_count,
                'num_threads': threads, 'user': user
            })

        
        return processes

    @staticmethod
    def _get_pid(process: psutil.Process):
        return process.pid

    @staticmethod
    def _get_process_name(process: psutil.Process):
        return process.name()

    @staticmethod
    def _get_create_time(process: psutil.Process):
        # create_time
        try:
            create_time = datetime.fromtimestamp(process.create_time())
        except OSError:
            create_time = datetime.fromtimestamp(process.boot_time())

    @staticmethod
    def _get_status(process: psutil.Process):
        # status = process.status()
        return process.status()

    @staticmethod
    def _get_process_priority(process: psutil.Process):
        # nice = int(process.nice())
        try:
            nice = int(process.nice())
        except psutil.AccessDenied:
            nice = 0

        return nice

    @staticmethod
    def _get_process_cores(process: psutil.Process):
        # cores = len(process.cpu_affinity)
        try:
            core = len(process.cpu_affinity())
        except psutil.AccessDenied:
            cores = 0

    @staticmethod
    def _get_cpu_percent(process: psutil.Process):
        return process.cpu_percent()

    @staticmethod
    def _get_memory_usage(process: psutil.Process):
        # memory_usage = process.memory_full_info().uss
        try:
            memory_usage = process.memory_full_info().uss
        except psutil.AccessDenied:
            memory_usage = 0

        return memory_usage

    @staticmethod
    def _get_process_io_bytes(process: psutil.Process):
        # io_counters, read_bytes, writes_byte
        return process.io_counters()

    @staticmethod
    def _get_threads_spawned(process: psutil.Process):
        # n_threads = process.num_threads()
        return process.num_threads()

    @staticmethod
    def get_user_who_spawned_process(process: psutil.Process):
        # username = process.username()
        try:
            user = process.username()
        except psutil.AccessDenied:
            user = "N/A"

        return user

class ProcessConstructor:

    @staticmethod
    def get_formatted_size(bytes):
        for unit in ['', 'K', 'M', 'G', 'T', 'O']:
            if bytes < 1024:
                return f"{bytes:.2f}{unit}B"
            bytes /= 1024


tracker = ProcessTracker()
processes=tracker.get_process_info()
print(processes)