#!/usr/bin/python3.6
import sys

# define group level master information
current_vin = ""
year = ""
make = ""
incidents = list()


def reset():
    """Reset master info for every group"""
    global current_vin
    global year
    global make
    global incidents
    current_vin = ""
    year = ""
    make = ""
    incidents = list()


def flush():
    """write the output"""
    print(
        f"{current_vin}\t{year}\t{make}\t{''.join(incidents)}"
    ) if current_vin else None


for line in sys.stdin:

    # parse the input from mapper and update the master info
    vin, incident_type, *data = line.strip().split("\t")

    # detect key changes
    if current_vin != vin:
        if current_vin is not None:
            # write result to stdout
            flush()
        reset()

    # update more master info after the key change handling
    current_vin = vin
    incidents.append(incident_type)

    if incident_type == "I":
        make, year = data


# do not forget to output the last group if needed
flush()
