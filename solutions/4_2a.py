import gzip
import sys
import csv

if len( sys.argv ) != 3:
  print "Usage: %s DATABASE ACCESSION" % sys.argv[0]
  sys.exit(1)

with gzip.GzipFile( sys.argv[1] ) as fobj:
  reader = csv.reader( fobj )
  
  for record in reader:
    if record[1] == sys.argv[2]:
      print "Found"
      sys.exit(0)

print "Not found"
