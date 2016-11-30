gene_filename = "../data/genes.txt"
with open(gene_filename, "r") as gene_file:
    with open("gene_lengths.txt", "w") as out:
        for line in gene_file:
            gene, chrom, start, end = line.split("\t")
            length = int(end) - int(start) + 1
            out.write("%s %d\n" % (gene, length))
    print("gene_lengths.txt created from %s" % gene_filename)



