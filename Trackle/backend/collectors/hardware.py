import psutil
import datetime

hardware_data = {
    #CPU
    "cpu_freq": psutil.cpu_freq(),
    "cpu_stats": psutil.cpu_stats(),
    "cpu_count": psutil.cpu_count(),
    "cpu_percentage": psutil.cpu_percent(),
    #Memory
    "virtual_memory": psutil.virtual_memory(),
    "swap_memory": psutil.swap_memory(),
    #System
    "loadavg": psutil.getloadavg(),
    #Disks
    "disk_partitions": psutil.disk_partitions(),
    "disk_usage": psutil.disk_usage("C://"),
    "disk_io_counters": psutil.disk_io_counters(),
}

print(hardware_data)