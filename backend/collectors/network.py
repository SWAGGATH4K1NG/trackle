import psutil
import datetime

network_data = {
    "connections": psutil.net_connections(),
    "speed": psutil.net_if_stats(),
    "addrs": psutil.net_if_addrs(),
    "net_io_counters": psutil.net_io_counters(),
    "boot_time": datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

}

    

for connection in network_data["connections"]:
    print(connection.laddr) 

for testSpeed in network_data["speed"]:
    print(testSpeed)

for addr in network_data["addrs"]:
    print(addr)

for io_counter in network_data["net_io_counters"]:
    print(io_counter)


print(network_data["boot_time"])


