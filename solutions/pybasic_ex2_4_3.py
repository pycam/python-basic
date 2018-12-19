genes = []
chromosomes = []

# How many genes are there in *S.cerevisiae*?
# Read a tab delimited file which has 5 columns: systematic_name, standard_name, chrom, start, end
with open('data/yeast_genes.txt') as yeast_gene_file:
    header = yeast_gene_file.readline()
    for line in yeast_gene_file:
        sys_name, std_name, chrom, start, end = line.strip().split('\t')
        chromosomes.append(chrom)
        genes.append({'sys_name': sys_name,
                      'std_name': std_name,  # NB. some genes do not have a standard name
                      'chrom': chrom,
                      'start': int(start),
                      'end': int(end),
                      'length': int(end) - int(start) + 1})

print("There are", len(genes), "genes in S.cerevisiae.")

# Which is the longest and which is the shortest gene?
shortest = genes[0]['length']
shortest_gene = genes[0]['sys_name']
longest = 0
longest_gene = ''
for g in genes:
    if g['length'] > longest:
        longest = g['length']
        longest_gene = g['sys_name']
    if g['length'] < shortest:
        shortest = g['length']
        shortest_gene = g['sys_name']

print("The shortest gene is", shortest_gene, "which is", shortest, "bases long.")
print("The longest gene is", longest_gene, "which is", longest, "bases long.")

# How many genes per chromosome? Print the number of genes per chromosome.
unique_chrom = set(chromosomes)

for chrom in unique_chrom:
    genes_per_chrom = 0
    for g in genes:
        if g['chrom'] == chrom:
            genes_per_chrom += 1
    print(chrom, "has", genes_per_chrom, "genes")

# For each chromosome, what is the longest and what is the shortest gene?
for chrom in unique_chrom:
    shortest = 99999999999
    shortest_gene = ''
    longest = 0
    longest_gene = ''
    for g in genes:
        if g['chrom'] == chrom:
            if g['length'] > longest:
                longest = g['length']
                longest_gene = g['sys_name']
            if g['length'] < shortest:
                shortest = g['length']
                shortest_gene = g['sys_name']
    print("On chrom", chrom, "the shortest gene is", shortest_gene, "(", shortest, ")", "and the longest is", longest_gene, "(", longest, ")")
