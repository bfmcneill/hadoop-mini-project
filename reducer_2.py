#!/usr/bin/env python

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
    if current_year_make:
        print "{}\t{}".format(current_year_make,count)


for line in sys.stdin:

    # parse the input from mapper and update the master info
    year,make, uno = line.strip().split("\t")
    year_make = "{}__{}".format(year,make)

    # detect key changes
    if current_year_make != year_make:
        if current_year_make is not None:
            # write result to stdout
            flush()
        reset()

    # update more master info after the key change handling
    current_year_make = year_make
    count += 1


# do not forget to output the last group if needed
flush()
