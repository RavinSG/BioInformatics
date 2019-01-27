import numpy as np
import itertools
from collections import defaultdict
import reverse_compliment as rc


def skew(DNA):
    count = [0]
    for i in range(len(DNA)):

        if DNA[i] == 'C':
            count.append(count[i] - 1)
        elif DNA[i] == 'G':
            count.append(count[i] + 1)
        else:
            count.append(count[i])
    x = np.array(count)
    x = np.where(x == x.min())[0]
    # print(x[0])
    # print(' '.join(map(str, count)))
    return count, x


def hamming_distance(string1, string2):
    l = len(string1)
    dist = 0
    for i in range(l):
        if string1[i] != string2[i]:
            dist += 1

    return dist


def approximate_match(DNA, pattern, d):
    l = len(pattern)
    start = []
    for i in range(len(DNA) - l + 1):
        if hamming_distance(DNA[i:i + l], pattern) <= d:
            start.append(i)
    print(len(start))
    # print(' '.join(map(str, start)))


letters = ['A', 'C', 'G', 'T']


def generate_neighbours(string, d):
    neighbours = []
    l = len(string)
    a = list(itertools.product(letters, repeat=l))
    candidates = [''.join(x) for x in a]

    for i in candidates:
        if hamming_distance(i, string) <= d:
            neighbours.append(i)

    return neighbours


def k_mers_d_mismatches(DNA, k, d):
    neighbours = {}
    count = defaultdict(int)

    for i in range(len(DNA) - k + 1):
        print('At pos:', i, 'Built Neighbourhood size: ',len(neighbours))
        segment = DNA[i:i + k]
        if segment in neighbours.keys():
            for neighbour in neighbours[segment]:
                count[neighbour] += 1
        else:
            neighbours[segment] = generate_neighbours(segment, d)
            for neighbour in neighbours[segment]:
                count[neighbour] += 1

    # print(get_highest(count))
    total = 0
    pair = []
    for key in count.keys():
        rev = rc.reverse_compliment(key)
        if rev in count.keys():
            temp = count[key] + count[rev]
            if temp > total:
                total = temp
                pair = [key, rev]
            elif temp == total:
                if key not in pair:
                    pair = pair + [key, rev]

    print(' '.join(pair))


def get_highest(count):
    mismatch = []
    highest = max(count.values())

    for key, value in count.items():
        if value == highest:
            mismatch.append(key)

    return (' '.join(mismatch))


# dna = 'aatgatgatgacgtcaaaaggatccggataaaacatggtgattgcctcgcataacgcggtatgaaaatggattgaagcccgggccgtggattctactcaactttgtcggcttgagaaagacctgggatcctgggtattaaaaagaagatctatttatttagagatctgttctattgtgatctcttattaggatcgcactgcccTGTGGATAAcaaggatccggcttttaagatcaacaacctggaaaggatcattaactgtgaatgatcggtgatcctggaccgtataagctgggatcagaatgaggggTTATACACAactcaaaaactgaacaacagttgttcTTTGGATAActaccggttgatccaagcttcctgacagagTTATCCACAgtagatcgcacgatctgtatacttatttgagtaaattaacccacgatcccagccattcttctgccggatcttccggaatgtcgtgatcaagaatgttgatcttcagtg'
#
# k_mers_d_mismatches(dna.upper(), 9, 1)
