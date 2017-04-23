import itertools


def annograms(word):
    words = [w.rstrip() for w in open('WORD.lst')]
    words = set([ w for w in words if len(w) == len(word)])
    comb = set([ ''.join(w) for w in 
                itertools.permutations(word, len(word))])

    return comb.intersection(words)


if __name__ == '__main__':
    print annograms("train")
    print '--'
    print annograms('drive')
    print '--'
    print annograms('python')

