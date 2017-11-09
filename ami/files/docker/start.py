#!/usr/bin/python
import time
import requests
from retrying import retry # pip install retrying
from common import *

def main():
    start = time.time()

    pull_images()
    start_compose()
    wait_for_service_to_start()

    end = time.time()
    logger.info("service UP and running in "+ str(int(end - start))+"s!!!")

@retry(stop_max_delay=300000, stop_max_attempt_number=5)
def pull_images():
    logger.info("pulling images...")
    retval = execute_proc('/usr/local/bin/docker-compose pull 2>&1')
    logger.debug("pulling images rc: %s", str(retval))
    if retval > 0:
        raise Exception("Error pulling images")

@retry(stop_max_delay=300000, stop_max_attempt_number=5)
def start_compose():
    logger.info("starting docker-compose...")
    retval = execute_proc('/usr/local/bin/docker-compose up -d 2>&1')
    logger.debug("starting docker-compose rc: %s", str(retval))
    if retval > 0:
        raise Exception("Error starting docker-compose")

@retry(stop_max_delay=300000, wait_fixed=10000) # wait 3min with 10 secs betwen attempts
def wait_for_service_to_start():
    logger.info("waiting for docker containers to be started...")
    r = requests.get("http://localhost/health")
    if r.status_code != 200:
        raise Exception("Waiting for docker containers to start... rc: %s", str(r.status_code))

if __name__ == '__main__':
    main()
