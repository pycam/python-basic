gene_file = open("../data/genes.txt", "r")
out_file = open("gene_lengths.txt", "w")

for line in gene_file:
    gene, chrom, start, end = line.split("\t")
    length = int(end) - int(start) + 1
    out_file.write("%s %d\n" % (gene, length))

gene_file.close()
out_file.close()

