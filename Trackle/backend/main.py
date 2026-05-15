# import all the necessary modules
from collectors import network
from collectors import hardware
from analyzers import network_analyzer


# import other necessary modules
import json
import time
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

while True:
    logger.info("Collecting data")
    data = {
        "network": network.get_network_data(),
        "hardware": hardware.get_hardware_data(),
    }
    print(json.dumps(data))
    sys.stdout.flush()
    time.sleep(1)

