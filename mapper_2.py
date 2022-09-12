#!/usr/bin/python3.6

import sys

for line in sys.stdin:
    vin, year, make, incidents = line.strip().split("\t")
    for incident in incidents:
        print(f"{year}\t{make}") if incident == "A" else None
