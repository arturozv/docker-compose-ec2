import subprocess
import logging
import sys
import os

logfile = '/home/ubuntu/logsdeploy/start.log'
logger = logging.getLogger('start')
handler = logging.FileHandler(logfile)
formatter = logging.Formatter("%(asctime)s - %(levelname)-5s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

def execute_proc(proc):
    p = subprocess.Popen(proc, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        logger.debug(line.rstrip())
    retval = p.wait()
    return retval
