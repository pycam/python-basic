import sys
import gzip

try:
    g1k_samples = set()
    with gzip.GzipFile(sys.argv[1]) as g1k:
        for line in g1k:
            line = line.rstrip()
            pop, sample_id, sample_name, sex = line.split(",")
            g1k_samples.add(sample_id)

    with open(sys.argv[3], "w") as output_file:
        with open(sys.argv[2]) as search_file:
            for line in search_file:
                line = line.rstrip()
                found = 0
                if line in g1k_samples:
                    found = 1
                output_file.write(",".join([line, str(found)]) + "\n")

except IndexError as e:
    print("Please supply 3 command line arguments")
    print("Usage: %s 1000genomes search output" % sys.argv[0])
    print(e)
except IOError as e:
    print("I can't read the file:", e)