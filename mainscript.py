from Bio import Entrez
from Bio import ExPASy
from Bio import SeqIO
from Bio.Align import Alignment
from Bio.Data import CodonTable
from Bio.Seq import MutableSeq
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import gc_fraction
from Bio.SeqUtils.ProtParam import ProteinAnalysis

ammlett=["A","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","Y","X","B","J","Z"]
ammname=["Alanine","Cysteine","Aspartate","Glutammate","Fenylalanine","Glycine","Histidine","Isoleucine","Lysine","Leucine","Metionine","Asparagine","Pyrrolisine","Proline","Glutammine","Arginine","Serine","Threonine","Selenocysteine","Valine","Tryptophane","Tyrosine","(undetermined)","ERROR: UNKNOWN","ERROR: UNKNOWN","ERROR: UNKNOWN"]

parseq=SeqIO.read("s.fasta", "fasta")
seq=parseq.seq
anaseq=ProteinAnalysis(str(seq))

# PRIMARY STRUCTURE
print("")
print("Primary structure (aminoacid sequence):")
for i in seq:   # For each letter, prints the respective full name.
    print(ammname[ammlett.index(i)])
print("")

# SECONDARY STRUCTURE
print("")
print("Secondary structure (alpha-helix/beta-sheet sequence):")
print("(not available yet...)")
print("")

# TERTIARY STRUCTURE
print("")
print("Tertiary structure (functional group sequence):")
print("(not available yet...)")
print("")

# OTHER PARAMETERS
print("")
print("Aminoacid composition (count and percentage):")
amicnt=list(anaseq.count_amino_acids().items())
#amiprc=list(anaseq.amino_acids_percent().items())
for i in amicnt:
    print(ammname[ammlett.index(str(i[0]))]+":   "+str(i[1])+" units   ("+str(100*i[1]/len(seq))+"%)")
print("")

print("")
print("Total molecular weight:")
print(str(anaseq.molecular_weight())+" a.u.")
print("")

print("")
print("Isoelectric point:")
print("pH "+str(anaseq.isoelectric_point()))
print("")

print("")
print("Hydrophobicity:")
print(str(anaseq.gravy())+" (grand average of hydropathy)")
print("")
