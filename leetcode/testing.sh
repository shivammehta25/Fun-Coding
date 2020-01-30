#!/bin/sh
for((i = 1; ; ++i)); do
    echo $i
    (./test_generator.py $i) > int
    # (./first_missing_positive.py < int) > out1
    # (./first_missing_positive_bf.py < int) > out2
    # diff -w out1 out2 || break
    diff -w <(./first_missing_positive.py < int) <(./first_missing_positive_bf.py < int) || break
done
