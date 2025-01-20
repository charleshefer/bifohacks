###############################################################################
#Merging ghostkoala and kegg orthology files
#Produces a text file with three colums: accession, ko term, ko description
#@author:charles.hefer@agresearch.co.nz
#@version:0.1
###############################################################################
import optparse, sys
import re

ko_re = re.compile("(^K[0-9]+) +(.+)")

def __main__():
	"""Parse the cmd lne options"""
	parser = optparse.OptionParser()
	parser.add_option("-g", "--ghostkoala", default=None, dest="ghostkoala",
					  help="The input ghostkoala file (user_ko.txt)")
	parser.add_option("-k", "--kegg", default=None, dest="kegg_orthology",
					  help="The input kegg orthology file")
	parser.add_option("-o", "--output", default=None, dest="output",
					  help="The output file")	
	(options, args) = parser.parse_args()
	
	if not options.ghostkoala:
		parser.error("Need to specify the input ghostkoala file")
	if not options.kegg_orthology:
		parser.error("Need to specify the input kegg orthology file")
		

	#Read the ghostkoala file
	ghostkoala = {}
	with open(options.ghostkoala, "r") as handle:
		for line in handle:
			try:
				accession,ko = line.strip().split("\t")
				if ko:
					ghostkoala[accession] = ko
			except ValueError:
				pass
	
	#print(ghostkoala)

	#read the kegg orthology file
	kegg = {}
	with open(options.kegg_orthology, "r") as handle:
		#parse out the 4th column
		for line in handle:
			#print(line)
			description = line.strip().split("\t")[3]
			#print(description)
			#the ko id is the first part before the space, split using the re
			ko_description = ko_re.match(description)
			kegg[ko_description.groups()[0]] = ko_description.groups()[1]

	#print(kegg)

	#write the results
	with open(options.output, "w") as handle:
		for accession in ghostkoala.keys():
			ko_term = ghostkoala[accession]
			if ko_term in kegg.keys():
				handle.write("%s\t%s\t%s\n" % (accession, ko_term, kegg[ko_term]))


if __name__ == "__main__":
	__main__()
	