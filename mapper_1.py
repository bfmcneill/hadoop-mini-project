#!/usr/bin/env python

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
    print '{}\t{}\t{}\t{}'.format(vin_number, incident_type, make, year)
    
