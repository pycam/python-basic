# Script that reads a tab delimited file which has 4 columns:
# gene, chromosome, start and end coordinates; that computes each gene's length
# stores it into a dictionary; and writes the results into a new tab separated file. 

gene_file = ('data/genes.txt')
output_file = "gene_lengths.txt"

results = []
# Read a tab delimited file which has 4 columns: gene, chrom, start and end.
with open(gene_file) as f:
    header = f.readline()
    for line in f:
        gene, chrom, start, end = line.strip().split("\t")
        # compute the length of each gene and
        # store its name and corresponding length into a dictionary
        row = {'gene': gene, 'length': int(end) - int(start) + 1}
        results.append(row)
# print results
print(results)

# Write the results into a new tab separated file
with open(output_file, "w") as out:
    out.write('gene' + "\t" + 'length' + "\n")  # write header
    for record in results:
        out.write(record['gene'] + "\t" + str(record['length']) + "\n")

# print contents of output file
with open(output_file) as f:
    print(f.read())
