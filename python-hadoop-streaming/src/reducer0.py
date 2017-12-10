#!/usr/bin/env python3
 
import sys
 
current_word = None
current_count = 0
word = None
 
# input comes from STDIN
for line in sys.stdin:
     
    # parse the input we got from mapper.py
    pair = line.split('\t')
    word = pair[0]
    count = pair[1]

    # here count can be >1 since the mapper has performed local aggregation
 
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
 
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    # recall that no ordering is ensured by deafult Hadoop on the value component (here count) 
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            if current_count > 1:
                print('{}\t{}'.format(current_word, current_count))
        current_count = count
        current_word = word
 
# do not forget to output the last word if needed!
if current_word == word:
    print('{}\t{}'.format(current_word, current_count))
