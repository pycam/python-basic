import os.path
import csv

# Read a tab delimited file which has 4 columns: gene, chromosome, start and end coordinates.
# Check if the file exists, then compute the length of each gene and store
# its name and corresponding length into a dictionary.
# Write the results into a new tab separated file and make use of the csv module.

gene_file = os.path.join('data', 'genes.txt')
output_file = "gene_lengths_csv.tsv"

if os.path.exists(gene_file):
    results = []
    with open(gene_file) as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            record = {'gene': row['gene'], 'length': int(row['end']) - int(row['start']) + 1}
            results.append(record)
    print(results)
    with open(output_file, "w") as out:
        writer = csv.DictWriter(out, results[0].keys(), delimiter='\t')
        writer.writeheader()  # write header
        for record in results:
            writer.writerow(record)
else:
    print(gene_file, 'does not exists!')

if os.path.exists(output_file):
    # print contents of output file
    with open(output_file) as f:
        print(f.read())
else:
    print(output_file, 'does not exists!')
