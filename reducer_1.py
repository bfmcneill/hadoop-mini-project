#!/usr/bin/env python

import sys

# define group level master information
current_vin = ""
year = ""
make = ""
incidents = ""


def reset():
    """Reset master info for every group"""
    global current_vin
    global year
    global make
    global incidents
    current_vin = ""
    year = ""
    make = ""
    incidents = ""


def flush():
    """write the output"""

    if current_vin:
        print "%s\t%s\t%s\t%s" % (current_vin,year,make,incidents)


for line in sys.stdin:

    # parse the input from mapper and update the master info
    # vin, incident_type, *data = line.strip().split("\t")
    data = line.strip().split('\t')
    _vin = data[0]
    _incident_type = data[1]

    if len(data) >2:
        # make and year exists
        make = data[2]
        year= data[3]

    # detect key changes
    if current_vin != _vin:
        if current_vin is not None:
            # write result to stdout
            flush()
        reset()

    # update more master info after the key change handling
    current_vin = _vin
    incidents += _incident_type



# do not forget to output the last group if needed
flush()
