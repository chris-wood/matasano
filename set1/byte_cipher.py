import os
import sys
import binascii
import string
import re
import math
from xor import *

english_freqs = {'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.361, 'x': 0.150, 'y': 1.974, 'z': 0.074}

bigram_freqs = {'th': 1.52, 'he': 1.28, 'in': 0.94, 'er': 0.94, 'an': 0.82, 're': 0.68, 'nd': 0.63, 'at': 0.59, 'on': 0.57, 'nt': 0.56, 'ha': 0.56, 'es': 0.56, 'st': 0.55, 'en': 0.55, 'ed': 0.53, 'to': 0.52, 'in': 0.50, 'ou': 0.50, 'eu': 0.47, 'hi': 0.46, 'is': 0.46, 'or': 0.43, 'ti': 0.34, 'as': 0.33, 'te': 0.27, 'et': 0.19, 'ng': 0.18, 'of': 0.16, 'al': 0.09, 'de': 0.09, 'se': 0.08, 'le': 0.08, 'sa': 0.06, 'si': 0.05, 'ar': 0.04, 've': 0.04, 'ra': 0.04, 'ld': 0.02, 'ur': 0.02}
total = 0.0
for k in bigram_freqs:
    total += bigram_freqs[k]
bigram_freqs = {k: (bigram_freqs[k] / total) * 100.0 for k in bigram_freqs}

def histogram_difference(truth, h2):
    ''' Plainly compute the difference between the two histograms on a per-element basis.
    '''
    total = 0
    for i in h2:
        if i in truth:
            total += abs(truth[i] - h2[i])
    for i in truth:
        if i not in h2:
            total += truth[i]
    return total

def compute_bigram_frequency(string):
    counts = {}
#    for i in range(0, 26):
#        for j in range(0, 26):
#            c1, c2 = chr(i + 97), chr(j + 97)
#            counts[(c1, c2)] = 0

    regex = re.compile('[^a-zA-Z]')
    string = regex.sub(' ', string).lower()
    for i in range(len(string) - 1):
        c1, c2 = string[i], string[i + 1]
        if (c1, c2) not in counts:
            counts[(c1, c2)] = 0
        counts[(c1, c2)] = counts[(c1, c2)] + 1

    frequency = {"".join(k): (float(counts[k]) / len(string)) * 100.0 for k in counts.keys()}

    return frequency, len(string)

def compute_frequency(string):
    counts = {}
#    for i in range(0, 26):
#        character = chr(i + 97)
#        counts[character] = 0

    regex = re.compile('[^a-zA-Z]')
    string = regex.sub(' ', string).lower()
    for c in string:
        if c not in counts:
            counts[c] = 0
        counts[c] = counts[c] + 1

    frequency = {k: (float(counts[k]) / len(string)) * 100.0 for k in counts.keys()}

    return frequency, len(string)

def crack(input_string):
    ciphertext = input_string.decode("hex")
    length = len(ciphertext)

    min_diff = 10 ** 10 # too large to start

    candidates = []
    for k in string.printable:
        pad = k * length
        pt = xor(ciphertext, pad).decode("hex")

        frequency, l1 = compute_frequency(pt)
        bigram_frequency, l2 = compute_bigram_frequency(pt)

        single_diff = histogram_difference(english_freqs, frequency)
        bigram_diff = histogram_difference(bigram_freqs, bigram_frequency)

        reduce1 = float(l1) / len(pt)
        reduce2 = float(l2) / len(pt)

        diff = (single_diff / reduce1) + (bigram_diff / reduce2)
        diff = single_diff + bigram_diff

        if all(map(lambda c : c in set(string.printable), pt)) and diff < min_diff:
            min_diff = diff
            candidates.append((k, pt, diff))

    return candidates

def main(args):
    ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    candidates = crack(ciphertext)
    print "Most probable decoding: %s -> %s" % (candidates[-1][0], candidates[-1][1])

if __name__ == "__main__":
    main(sys.argv[1:])
