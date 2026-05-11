import psutil

hardware_data = {
    "loadavg": psutil.getloadavg(),
    "cpu_freq": psutil.cpu_freq(),
    "cpu_stats": psutil.cpu_stats(),
    "cpu_count": psutil.cpu_count(),
}