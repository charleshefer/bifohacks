# Scaffold breaker

Given a fasta file with scaffolded sequences (i.e. sequences that are joined together with the `N` character), this script will break any `scaffolds` on the `N` character, and will create a new entry in the fasta file for each of the sequences containin `NNs`. The new entry will have the same name as the original entry, but with a `_partn` suffix.

This will not take into account the length of the new entries, and needs to be filtered out using a different script.

## Dependencies

Requires the `biopython` package. 

## Usage

```bash
python cfasta_scaffold_breaker.py -i input.fasta -o output.fasta
```

## Example

The input fasta file:

```
>seq1
ATGC
>seq2
AAAAAANNNNNCCCCCC
>seq3
NAAACCCGGGTTTN
```

The output fasta file:

```
>seq1
ATGC
>seq2_part1
AAAAAA
>seq2_part2
CCCCCC
>seq3_part1
AAACCCGGGTTT
```