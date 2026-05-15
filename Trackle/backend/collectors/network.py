import psutil
import pprint
import datetime
import socket
import logging


def get_network_data():
    return {
    #Network
    "connections": psutil.net_connections(),
    "speed": psutil.net_if_stats(),
    "addrs": psutil.net_if_addrs(),
    "net_io_counters": psutil.net_io_counters(),
    #System
    "hostname": socket.gethostname(),
    "boot_time": datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

}



