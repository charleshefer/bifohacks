# Custom KEGG

Tips on how to perform a custom KEGG analysis, for any of the weird and wonderful organisms that dont have OrgDB databases associated with them.

## Annotate proteins 
### GhostKoala
Run the protein sequences through [GHOSTKOALA](https://www.kegg.jp/ghostkoala/) to get the KEGG annotation for the proteins. Download the relavent results after processing, should be a file called `user_ko.txt`.

### kegg annotation

Grab tehe kegg pathway descriptions from the KEGG database.

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


