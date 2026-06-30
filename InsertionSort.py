def insertion_sort(seq):
    for slicend in range(1, len(seq)):
        pos = slicend

        while pos > 0 and seq[pos] < seq[pos-1]:
            (seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos])
            pos = pos-1
    print(seq)
seq = [67, 44, 82, 17, 20]
insertion_sort(seq)
