#!/usr/bin/env python3
import random
import sys

seed = int(sys.argv[1])

a = set()

for i in range(random.randint(1, 1000)):
    a.add(random.randint(-1000, 100))

a = list(a)
random.shuffle(a)
print(' '.join(map(str, a)))

