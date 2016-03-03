import sys
import binascii
import math

from xor import *

key = "ICE"

with open(sys.argv[1], 'r') as fh:
    data = fh.read()
    keypad = key * int(math.ceil(len(data) / float(3)))

    ct = xor(data, keypad)
    print ct
