#!/usr/bin/python3.6

import sys

for line in sys.stdin:
    (
        incident_id,
        incident_type,
        vin_number,
        make,
        model,
        year,
        incident_date,
        description,
    ) = line.split(",")

    print("\t".join([vin_number, incident_type, make, year]))
