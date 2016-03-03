import os
import sys
import binascii
import math

from xor import *
from byte_cipher import *

with open(sys.argv[1], 'r') as fh:
    all_candidates = []
    for line in fh:
        line = line.strip()
        candidates = crack(line)
        if len(candidates) > 0:
            all_candidates.append((line, candidates[-1]))

    for (line, (k, pt, diff)) in all_candidates:
        print line, k, pt
