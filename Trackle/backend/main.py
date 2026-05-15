from collectors import network
from collectors import hardware
import logging
import json
import time
import sys

while True:
    logger.info("Collecting data")
    data = {
        "network": network.get_network_data(),
        "hardware": hardware.get_hardware_data()
    }
    print(json.dumps(data))
    sys.stdout.flush()
    time.sleep(1)

