import os
import sys
import binascii
import re
import math
from xor import *

english_freqs = {'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.361, 'x': 0.150, 'y': 1.974, 'z': 0.074}

def histogram_difference(h1, h2): 
    ''' Plainly compute the difference between the two histograms on a per-element basis.
    '''
    #total = 0
    #for i in h1:
    #    total += ((h1[i] - h2[i]) ** 2)
    #return math.sqrt(total)
    total = 0
    for i in h1:
        total += abs(h1[i] - h2[i])
    return total

def compute_frequency(string):
    counts = {}
    for i in range(0, 26):
        character = chr(i + 97)
        counts[character] = 0

    regex = re.compile('[^a-zA-Z]')
    string = regex.sub('', string).lower()
    for c in string:
        counts[c] = counts[c] + 1

    frequency = {k: (float(counts[k]) / len(string)) * 100.0 for k in counts.keys()}
    return frequency

def main(args):
    ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736".decode("hex")
    length = len(ciphertext)
    stats = {}
    
    min_index = 0
    min_diff = 10 ** 10 # too large to start

    for i in range(0, 26):
        character = chr(i + 65) # I assume it's encoded in uppercase ASCII
        pad = character * length
        pt = xor(ciphertext, pad).decode("hex")
        
        frequency = compute_frequency(pt)
        diff = histogram_difference(english_freqs, frequency)
        stats[i] = (character, pt, diff)
        
        print "%s %f: %s" % (character, diff, pt)

        if diff < min_diff:
            min_diff = diff
            min_index = i

    print "\n\n"
    print "Most probable decoding: %s -> %s" % (stats[min_index][0], stats[min_index][1])

if __name__ == "__main__":
    main(sys.argv[1:])
