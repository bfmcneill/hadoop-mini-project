#!/usr/bin/python3.6

import sys

for line in sys.stdin:
    vin, year, make, incidents = line.strip().split("\t")
    for incident in incidents:
        if incident == "A":
            print("\t".join([year, make, 1]))
