#!/usr/bin/env python3

import signal
import time
import sys


def shut_down():
    sys.exit("Termination requested")


def handler(signum, frame):
    print("Signal handler called with signal", signum)
    shut_down()


signal.signal(signal.SIGTERM, handler)

while True:
    print('sleeping...')
    time.sleep(1.0)
