# Perform a Hifiasm assembly with ONT data

Since version 0.9, HiFiasm has been able to take in ONT data directly. This is a guide on how to run HiFiasm with ONT data, including the steps needed to make sure that you can use the ONT data to polish the genome as well.


## Steps
### Basecalling

Using dorado, basecall the ONT data. Make sure to include the `--emit-moves` flag to ensure the ONT data can be used for polishing later. 

```
dorado basecaller hac {library}/ --emit-moves > {library}.bam
```

### Convert bam to fastq

Convert the bam file into fastq. This can be done using `samtools`:

```
samtools fastq {library}.bam > {library}.fastq
```

### Run HiFiasm

Run HiFiasm with the fastq file. Make sure to include the `--ont` flag to ensure that HiFiasm knows that the data is ONT data.

```
hifiasm -t {threads} --ont -o ../results/03_HIFIASM/assembly {input}
```

In this example, I had about 95Gb of sequence data for a 2.3Gb genome. The assembly took approximately 8 hours to complete, using 32 threads and 300Gb of RAM.

### Map ONT reads to genome

Use the dorado aligner to map the ONT reads to the genome. This will be used for polishing the genome.

```
dorado aligner -t {threads} {input.haplotype} {input.bam} > {output.bam}
```

### Polish the genome

After sorting and indexing the alignment bam file with samtools, use the dorado polish command to polish the genome. You can specify the read groups, or ignore them if you want to merge them. This ran fine on the GPU, but never completed after more than 7 days on the CPU.

```
dorado polish -t {threads} --ignore-read-groups {input.bam} {input.haplotype} > {output.fasta}
```



