# create sequence
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC

my_seq=Seq('AAAACCCCGGGGGTTT', IUPAC.unambiguous_dna)
print my_seq
print GC(my_seq)
print my_seq.complement()
print my_seq.reverse_complement()
print my_seq.transcribe()
print my_seq.translate()

print "----------"
# read fasta from file
from Bio import SeqIO
for seq_record in SeqIO.parse("Course_Materials/data/glpa.fa", "fasta"):
  print seq_record.id
  print seq_record.seq

print "----------"
# read fasta from NCBI GenBank
from Bio import Entrez
Entrez.email = "A.N.Other@example.com"
entrez=Entrez.efetch(db='protein', rettype='fasta', id='71066805')
my_dna=SeqIO.read(entrez, 'fasta')
entrez.close()
print my_dna.id
print my_dna.description
print my_dna.seq

print "----------"
# read swissprot record from ExPASy
from Bio import ExPASy
expasy=ExPASy.get_sprot_raw('HBB_HUMAN')
my_protein=SeqIO.read(expasy, 'swiss')
expasy.close()
print my_protein.id
print my_protein.description
print my_protein.seq

print "----------"
# write fasta file
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_protein
rec1 = SeqRecord(Seq("MMYQQGCFAGGTVLRLAKDLAENNRGARVLVVCSEITAVTFRGPSETHLDSMVGQALFGD" \
                    +"GAGAVIVGSDPDLSVERPLYELVWTGATLLPDSEGAIDGHLREVGLTFHLLKDVPGLISK" \
                    +"NIEKSLKEAFTPLGISDWNSTFWIAHPGGPAILDQVEAKLGLKEEKMRATREVLSEYGNM" \
                    +"SSAC", generic_protein), 
                 id="gi|14150838|gb|AAK54648.1|AF376133_1",
                 description="chalcone synthase [Cucumis sativus]")

rec2 = SeqRecord(Seq("YPDYYFRITNREHKAELKEKFQRMCDKSMIKKRYMYLTEEILKENPSMCEYMAPSLDARQ" \
                    +"DMVVVEIPKLGKEAAVKAIKEWGQ", generic_protein),
                 id="gi|13919613|gb|AAK33142.1|",
                 description="chalcone synthase [Fragaria vesca subsp. bracteata]")

rec3 = SeqRecord(Seq("MVTVEEFRRAQCAEGPATVMAIGTATPSNCVDQSTYPDYYFRITNSEHKVELKEKFKRMC" \
                    +"EKSMIKKRYMHLTEEILKENPNICAYMAPSLDARQDIVVVEVPKLGKEAAQKAIKEWGQP" \
                    +"KSKITHLVFCTTSGVDMPGCDYQLTKLLGLRPSVKRFMMYQQGCFAGGTVLRMAKDLAEN" \
                    +"NKGARVLVVCSEITAVTFRGPNDTHLDSLVGQALFGDGAAAVIIGSDPIPEVERPLFELV" \
                    +"SAAQTLLPDSEGAIDGHLREVGLTFHLLKDVPGLISKNIEKSLVEAFQPLGISDWNSLFW" \
                    +"IAHPGGPAILDQVELKLGLKQEKLKATRKVLSNYGNMSSACVLFILDEMRKASAKEGLGT" \
                    +"TGEGLEWGVLFGFGPGLTVETVVLHSVAT", generic_protein),
                 id="gi|13925890|gb|AAK49457.1|",
                 description="chalcone synthase [Nicotiana tabacum]")
               
my_records = [rec1, rec2, rec3]
print rec1.format('fasta')

from Bio import SeqIO
SeqIO.write(my_records, "my_example.faa", "fasta")
print 'File created'



