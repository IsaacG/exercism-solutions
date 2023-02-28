def distance(strand_a, strand_b):
    same = 0
    for i in range(len(strand_a)):
        if strand_a[i] == strand_b[i]:
            same += 1
    return same


distance("abc", "ab")  # Note the first strand is longer than the second strand.
