# Custom KEGG

Tips on how to perform a custom KEGG analysis, for any of the weird and wonderful organisms that dont have OrgDB databases associated with them.

## Annotate proteins 
### GhostKoala
Run the protein sequences through [GHOSTKOALA](https://www.kegg.jp/ghostkoala/) to get the KEGG annotation for the proteins. Download the relevant results after processing, should be a file called `user_ko.txt`.

### Kegg annotation

Grab the kegg pathway descriptions from the KEGG database. This bit of code was taken from [this blog post at the merenlab](https://merenlab.org/2018/01/17/importing-ghostkoala-annotations/#export-anvio-gene-calls) from 2018. All credit goes to them.

```
wget 'https://www.genome.jp/kegg-bin/download_htext?htext=ko00001&format=htext&filedir=' -O ko00001.keg
```

Convert the .keg file to something a bit more readable. Copy and this this in bash:

```
kegfile="ko00001.keg"

while read -r prefix content
do
    case "$prefix" in A) col1="$content";; \
                      B) col2="$content" ;; \
                      C) col3="$content";; \
                      D) echo -e "$col1\t$col2\t$col3\t$content";;
    esac
done < <(sed '/^[#!+]/d;s/<[^>]*>//g;s/^./& /' < "$kegfile") > KO_Orthology_ko00001.txt
```

This will give you a file called `KO_Orthology_ko00001.txt` which contains the KEGG orthology descriptions.

### Merge the files

Use the script `cmerge_ghostkoala_kegg_orthology.py` to merge the GhostKoala and KEGG Orthology files to get a nice table of KEGG annotations for your proteins.

```
python scripts/cmerge_ghostkoala_kegg_orthology.py -g user_ko.txt -k KO_Orthology_ko00001.txt -o ko_results.txt
```

#Perform Enrichment analysis

Make use of `clusterProfiler` to perform the enrichment analysis. Clusterprofiler provides the `enricher` function for this exact purpose. See this [blog post](http://guangchuangyu.github.io/2015/05/use-clusterprofiler-as-an-universal-enrichment-analysis-tool/) for more information. A quartro/markdown file to perform the analyses on an example set of data is provided [here](www.google.com).

# Use clusterProfiler::enricher to perform enrichment analysis


```
library(clusterProfiler)

# read the background, custom database
custom_kegg_fh <- read.delim("./custom_kegg.txt", header=FALSE) #this was made through ghostkoala and kegg
colnames(custom_kegg_fh) <- c("protein", "pathway", "description")

custom_kegg_db <- NULL
custom_kegg_db$term <- custom_kegg_fh$pathway
custom_kegg_db$gene <- custom_kegg_fh$protein
custom_kegg_db <- data.frame(custom_kegg_db)

# have 2 gene lists, one with the universe, and one with the genes of interest

kegg_enrichment <- enricher(gene = geneList,
                            TERM2GENE = custom_kegg_db,
                            pvalueCutoff = 0.05,
                            pAdjustMethod = "BH",
                            qvalueCutoff = 0.05,
                            minGSSize = 1, #adjust based on database size
                            universe = universeList
                            )

```
