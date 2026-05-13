import psutil
import pprint
import datetime
import socket

network_data = {
    #Network
    "connections": psutil.net_connections(),
    "speed": psutil.net_if_stats(),
    "addrs": psutil.net_if_addrs(),
    "net_io_counters": psutil.net_io_counters(),
    #System
    "hostname": socket.gethostname(),
    "boot_time": datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

}

pprint.pprint(network_data, sort_dicts=False)


