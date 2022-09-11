import sys

for line in sys.stdin:
    vin, year, make, incidents = line.strip().split("\t")
    for incident in incidents:        
        if incident == 'A':
            print "%s\t%s\t%s\1" % (year,make,1)
