import os.path

# Read a tab delimited file which has 4 columns: gene, chromosome, start and end coordinates.
# Check if the file exists, then compute the length of each gene and store
# its name and corresponding length into a dictionary.
# Write the results into a new tab separated file.

gene_file = os.path.join('data', 'genes.txt')
output_file = "gene_lengths.tsv"

if os.path.exists(gene_file):
    results = []
    with open(gene_file) as f:
        header = f.readline()
        for line in f:
            gene, chrom, start, end = line.strip().split("\t")
            row = {'gene': gene, 'length': int(end) - int(start) + 1}
            results.append(row)
    print(results)
    with open(output_file, "w") as out:
        out.write('gene' + "\t" + 'length' + "\n")  # write header
        for record in results:
            out.write(record['gene'] + "\t" + str(record['length']) + "\n")
else:
    print(gene_file, 'does not exists!')

if os.path.exists(output_file):
    # print contents of output file
    with open(output_file) as f:
        print(f.read())
else:
    print(output_file, 'does not exists!')
