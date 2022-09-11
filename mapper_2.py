import sys

for line in sys.stdin:
    vin, year, make, incidents = line.strip().split("\t")
    for incident in incidents:        
        if incident == 'A':
            print "{}\t{}\t{}".format(year,make,1)
