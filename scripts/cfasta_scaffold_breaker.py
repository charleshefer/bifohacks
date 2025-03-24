###############################################################################
#Breaks a fasta file that contains the N characer into multiple entries
#
#@author:charles.hefer@agresearch.co.nz
#@version:0.1
###############################################################################
import optparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


def break_fasta_entry(fasta_entry):
	"""Breaks a fasta entry into multiple entries"""
	fasta_entries = []
	sequence = str(fasta_entry.seq)
	if "N" in sequence:
		sequences = sequence.split("N")
		counter = 0
		for seq in sequences:
			seq = seq.replace("N", "")
			if len(seq) > 1:
				counter += 1
				new_entry = SeqRecord(Seq(seq),
					   id = "%s_part%s" % (fasta_entry.id, counter),
				   		description = "")
				fasta_entries.append(new_entry)
	else:
		fasta_entries.append(fasta_entry)
	return(fasta_entries)


def __main__():
	"""Parse the cmd lne options"""
	parser = optparse.OptionParser()
	parser.add_option("-i", "--input", default=None, dest="input",
					  help="The input file")
	parser.add_option("-o", "--ouput", default=None, dest="output",
					  help="The output file")
	(options, args) = parser.parse_args()
	
	if not options.input:
		parser.error("Need to specify the input fasta file")
	if not options.output:
		parser.error("Need to specify the output fasta file")
	
	fasta_entries = []

	with open(options.input, "r") as input_file:
		for fasta_entry in SeqIO.parse(input_file, "fasta"):
			fasta_entries += break_fasta_entry(fasta_entry)

	SeqIO.write(fasta_entries, options.output, "fasta")


if __name__ == "__main__":
	__main__()
	