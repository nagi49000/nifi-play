import time
import logging
import nipyapi

logging.basicConfig(level=logging.DEBUG)

nipyapi.config.nifi_config.host = 'http://localhost:8091/nifi-api'
nipyapi.config.registry_config.host = 'http://localhost:18080/nifi-registry-api'

sleep_secs = 10
logging.info(f"sleeping for {sleep_secs} seconds")
time.sleep(10)
logging.info(f"woke up after {sleep_secs} seconds")
# demo and api calls run by import
from nipyapi.demo.console import *
dir()
