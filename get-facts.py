from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from datetime import datetime
import time

import sys

devices = [
    "192.168.3.72",
    "192.168.3.77",
    "192.168.3.79",
    "192.168.3.74",
    "192.168.3.75",
    "192.168.3.81",
    "192.168.3.127"
]

username = "axians"
password = "Axians"

while True:
    for device in devices:
        print(device, username, password)
        dev = Device(host=device, user=username, passwd=password, port='22')
        try:
            dev.open()
        except ConnectError as err:
            print ("Cannot connect to device: {0}".format(err))
            sys.exit(1)
        except Exception as err:
            print (err)
            sys.exit(1)


        pprint(dev.facts)
        timestamp = datetime.now()
        log = open("facts-stats.log", "a")
        log.write("OK: %s | %s \n" % (device, timestamp))
        time.sleep(10)
        dev.close()
