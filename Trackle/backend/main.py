from collectors import network
from collectors import hardware
import json
import time

while True:
    data = {
        "network": network.network_data,
        "hardware": hardware.hardware_data
    }
    print(json.dumps(data))
    time.sleep(1)

