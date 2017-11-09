#!/usr/bin/python
import time
from retrying import retry # pip install retrying
from common import *

def main():
    start = time.time()

    docker_compose_kill()
    docker_compose_rm()

    end = time.time()
    logger.info("service STOPPED in "+ str(int(end - start))+"s!!!")


@retry(stop_max_delay=300000, stop_max_attempt_number=5)
def docker_compose_kill():
    logger.info("docker_compose_kill...")
    retval = execute_proc('/usr/local/bin/docker-compose kill')
    logger.debug("docker_compose_kill rc: "+str(retval))
    if retval > 0:
        raise Exception("Error in docker_compose_kill")

@retry(stop_max_delay=300000, stop_max_attempt_number=5)
def docker_compose_rm():
    logger.info("docker_compose_rm...")
    retval = execute_proc('/usr/local/bin/docker-compose rm --force')
    logger.debug("docker_compose_rm rc: "+str(retval))
    if retval > 0:
        raise Exception("Error in docker_compose_rm")

if __name__ == '__main__':
    main()
