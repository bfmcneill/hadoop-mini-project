import sys

for line in sys.stdin:
    vin, year, make, incidents = line.strip().split("\t")
    for incident in incidents:
        print(f"{year}_{make}\t{1}") if incident == "A" else None
