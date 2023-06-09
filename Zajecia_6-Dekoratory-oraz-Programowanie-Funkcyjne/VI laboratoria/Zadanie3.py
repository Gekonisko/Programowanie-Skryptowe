import sys; print(len(list(filter(lambda x: int(x) % 2 == 0, sum(list(map(lambda file: open(file, 'r').read().split(), sys.argv[1:])), [])))));
