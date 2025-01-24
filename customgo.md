# Custom GO annotation

How to perform GO enrichment analyses if you only have a set of proteins, which are not annotated.

## Annotate proteins

Make use of `interproscan` to annotate the proteins. The important parameter to use is "-goterms". This will add GO terms to the annotation.

## Parse the annotation

Extract the go terms from the annotation. The GO terms needs to be in long format for the downstream enrichment analyses. See the example below that uses "./scripts/cextract_go_from_interproscan.py" to extract the GO terms.


```
python cextract_go_from_interproscan.py -i interproscan.tsv -o go_terms.txt
```

## Perform GO enrichment analyses

There are a couple of things that needs to be done with the output file to make it work with the enrichment analyses.

First, use `GO.db` to get the categoriues for each of the GO terms.

```
library(GO.db)

# Example list of GO terms
go_terms_fh <- read.csv("./go_terms.txt.txt", header=FALSE, sep="\t")
colnames(go_terms_fh) <- c("accession", "go_term")


# Function to get the category of a GO term with error handling
get_go_category <- function(go_term) {
  tryCatch({
    category <- Ontology(GOTERM[[go_term]])
    return(category)
  }, error = function(e) {
    return(NA)  # Return NA if there is an error
  })
}

#perform the conversion
go_categories <- sapply(go_terms_fh$go_term, get_go_category)

#and convert to a data frame
go_categories_df <- data.frame(GO_Term = unique(go_terms_fh$go_term), Category = go_categories)
```

Next, for each category, perform the enrichment analyses.

```
library(clusterProfiler)

#BP
#prepare the dataset
bp_go_db <- go_df %>%
  dplyr::filter(Category == "BP")

#prepare the universe
go_bp_term2gene <-  go_terms_fh %>%
  #dplyr::filter(accession %in% unique(background_input$name)) %>%
  dplyr::filter(go_term %in% bp_go_db$GO_Term) %>%
  select(go_term, accession) %>%
  unique()


go_results_bp <- enricher(gene = current_dep_up$name,
         TERM2GENE = go_bp_term2gene,
         pvalueCutoff = 0.05,
         pAdjustMethod = "BH",
         qvalueCutoff = 0.05,
         minGSSize = 1,
         universe = background_input$name
         )
```

In the case above, the go_bp_term2gene is term2go conversion table that is created from the go_terms.txt file. The current_dep_up is the list of proteins that are differentially expressed. The background_input is the list of all proteins that are in the dataset.

## Add descriptions to the GO terms

To add descriptions to the GO terms, use the following function to convert go ids to descriptions.

```

get_go_description <- function(go_term) {
  tryCatch({
    description <- Term(GOTERM[[go_term]])
    return(description)
  }, error = function(e) {
    return(NA)  # Return NA if there is an error
  })
}


go_descriptions <- sapply(unique(go_results$ID), get_go_description)
go_descriptions <- data.frame(ID = unique(go_results$ID), Descript = go_descriptions)

```
