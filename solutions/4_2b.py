import sys
import gzip

g1k = gzip.GzipFile(sys.argv[1])

g1k_samples = set()

for line in g1k:
    line = line.rstrip()
    pop, sample_id, sample_name, sex = line.split(",")
    g1k_samples.add(sample_id)

search_file = open(sys.argv[2])
output_file = open(sys.argv[3], "w")

for line in search_file:
    line = line.rstrip()
    found = 0
    if line in g1k_samples:
        found = 1
    output_file.write(",".join([line, str(found)])+"\n")


         
