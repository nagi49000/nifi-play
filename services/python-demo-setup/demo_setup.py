import time
import logging
import nipyapi
import requests

logging.basicConfig(level=logging.DEBUG)

nipyapi.config.nifi_config.host = "http://nifi:8080/nifi-api"
nipyapi.config.registry_config.host = "http://nifi-reg:18080/nifi-registry-api"

status_code = 0
status_code_reg = 0
while status_code != 200 or status_code_reg != 200:
    try:
        status_code_reg = requests.get(nipyapi.config.registry_config.host + "/access").status_code
        logging.warning(f"status_code on /nifi-registry-api/access {status_code_reg}")
        status_code = requests.get(nipyapi.config.nifi_config.host + "/system-diagnostics").status_code
        logging.warning(f"status_code on /nifi-api/system-diagnostics {status_code}")
    except Exception as e:
        logging.warning(str(e))
    time.sleep(5)

logging.warning(f"Starting NiPyApi demo run")
# demo and api calls run by import
from nipyapi.demo.console import *
logging.warning(f"demo files created: {dir()}")
