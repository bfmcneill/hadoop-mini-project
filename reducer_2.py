#!/usr/bin/python3.6

import sys

# define group level master information
current_year_make = ""
count = 0


def reset():
    """Reset master info for every group"""
    global current_year_make
    global count
    current_year_make = ""
    count = 0


def flush():
    """write the output"""
    print(f"{current_year_make}\t{count}") if current_year_make else None


for line in sys.stdin:

    # parse the input from mapper and update the master info
    year, make = line.strip().split("\t")

    # detect key changes
    if current_year_make != f"{year}_{make}":
        if current_year_make is not None:
            # write result to stdout
            flush()
        reset()

    # update more master info after the key change handling
    current_year_make = f"{year}_{make}"
    count += 1


# do not forget to output the last group if needed
flush()
