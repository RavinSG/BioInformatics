import itertools


def generate_words(k):
    letters = ['A', 'C', 'G', 'T']
    a = list(itertools.product(letters, repeat=k))
    a = [''.join(x) for x in a]
    return a


def count_pattern(string, pattern):
    l = len(pattern)
    count = 0
    for i in range(len(string) - l + 1):
        if string[i: i + l] == pattern:
            count += 1
    return count


def compute_frequency(text, k):
    freq = []
    words = generate_words(k)
    for word in words:
        c = count_pattern(text, str(word))
        freq.append(c)

    print(' '.join(map(str, freq)))


letters = ['A', 'C', 'G', 'T']


def pattern_to_number(pattern):
    print(pattern)
    if len(pattern) == 0:
        return 0
    else:
        return 4 * pattern_to_number(pattern[:-1]) + letters.index(pattern[-1])


def number_to_pattern(number, k):
    pattern = []
    while number > 0:
        letter = letters[number % 4]
        pattern.append(letter)
        number = number // 4

    fill = k - len(pattern)
    pattern = pattern + ['A'] * fill
    pattern.reverse()
    return ''.join(pattern)


# compute_frequency(
#     'ACCATACATGACCCACCATTAAGTGGTACCTGAAACTTTAGTCTGCAGGGACATGGCGGATGGGCTCTCTATAGCGAACCTCGCTGTCAAGGAATAGGCCCATCCTAACACAAGAAATAACGGTTGTAACATTGGGAATGGGTCGGCTAAACGAGTCGACGTGTCGGGCAGGGATTAAGCGATTGGTGGCGGGATCGCACGACATGAGTTGGCAAGTAGTGAACGTGATGCAAACTACATAGGAGACGAGCGTTAGGTCCTCTCTATTCATGAAGCTCAATGGGGGGGGGAAACCCTTTACAAACCTCCGGATAAATGCTGATCTGACTCTTGTTAGCAGATCTACTTTCAGAAGGACTAAACGTTCCAGAAACTGACTGGCTTCTGGCTGCAATGGTGTGACATTATAGTCTGGCAGTGAAACAGTCGCATTACCCTCTAATGGGGTAGATCGCAAAAAAAAATACAAACTAATGCCGGGTCAATCATCGCAACTTTACAGGGACCCTACTGTGGGACCTGAGAATTCTTACTCTAATTATACTGTCGACGTACTACGGATGAAGGAGAACCGGAGGTTCAATGGGAACCTGTCTTTATGCACCCGTGCCGCGGGAAT',
#     5)

print(number_to_pattern(7978, 7))
