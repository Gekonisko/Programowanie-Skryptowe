import sys; from collections import Counter; print(dict(Counter(map(lambda x: len(x), sys.stdin.read().split()))))
