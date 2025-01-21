###############################################################################
#extracts and converts to long format the go terms from the interproscan output
#Produces a text file with two colums: accession, go_term
#@author:charles.hefer@agresearch.co.nz
#@version:0.1
###############################################################################
import optparse, sys
import re

ko_re = re.compile("(^K[0-9]+) +(.+)")

def __main__():
	"""Parse the cmd lne options"""
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interproscan", default=None, dest="interproscan",
					  help="The input interproscan tsv file")
	parser.add_option("-o", "--output", default=None, dest="output",
					  help="The output file")	
	(options, args) = parser.parse_args()
	
	if not options.interproscan:
		parser.error("Need to specify the input interproscan tsv file")
	if not options.output:
		parser.error("Need to specify the output file")

	#Read the ghostkoala file
	interproscan = []
	with open(options.interproscan, "r") as handle:
		for line in handle:
			cols = line.strip().split("\t")
			accession, go_terms = (cols[0], cols[13])
			for go_term in go_terms.split("|"):
				go_term = go_term.replace("(PANTHER)", "").replace("(InterPro)", "")
				if "-" not in go_term:
					interproscan.append("%s\t%s" % (accession, go_term))

	#write the results
	with open(options.output, "w") as handle:
		for line in interproscan:
			handle.write("%s\n" % (line))


if __name__ == "__main__":
	__main__()
	