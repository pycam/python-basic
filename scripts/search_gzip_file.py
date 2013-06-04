import gzip
import sys
import csv

if len( sys.argv ) != 2:
    print "Usage: %s ACCESSION" % sys.argv[0]
    sys.exit(1)

with gzip.GzipFile( 'data/1000genomes_samples.csv.gz' ) as fobj:
    reader = csv.reader( fobj )
  
    for record in reader:
        if record[1] == sys.argv[1]:
            print "Found"
            sys.exit(0)

print "Not found"