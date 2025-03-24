# bifohacks

Tips on bioinformatics activities

## Guides:

### Assemblies
  - [hifiasm_with_ont.md](https://github.com/charleshefer/bifohacks/blob/main/hifiasm_with_ont.md) How to run hifiasm with ONT reads.

### Snakemake
  - [snakemake_lamda.md]() How to make use of lambda to access dictionary values in a Snakemake config file.

### KEGG and GO enrichnment analyses
  -  [customkegg.md](https://github.com/charleshefer/bifohacks/blob/main/customkegg.md) How to perform KEGG enrichment analyses on a completely unannotated set of proteins
  -  [customgo.md](https://github.com/charleshefer/bifohacks/blob/main/customkegg.md) How to perform GO enrichment analyses on a set of proteins annotated with InterProscan


## Scripts:
### KEGG and GO enrichment analyses
  - [cmerge_ghostkoala_kegg_orthology.py](https://github.com/charleshefer/bifohacks/blob/main/scripts/cmerge_ghostkoala_kegg_orthology.py) Merge the GhostKoala and KEGG Orthology files to get a nice table of KEGG annotations for your proteins.
  - [cextract_go_from_interproscan.py](https://github.com/charleshefer/bifohacks/blob/main/scripts/cextract_go_grom_interproscan.py) Extract GO terms from an InterProscan annotationm, making the dataset "long".

### FASTA format manipulation
  - [cfasta_scaffold_breaker.py] (hppts://github.com/charleshefer/bifohacks/blob/main/cfasta_scaffold_breaker.md) Break a scaffolded fasta file on the NNs, keep the names of the sequences.
