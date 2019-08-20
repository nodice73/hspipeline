# hspipeline
As the name suggests, `hspipeline` is a pipeline that connects existing tools together to analyse high-throughput sequencing data.

`hspipeline` is a command-line tool. Run it without arguments to see instructions and a detailed description of the arguments. 

Upon execution, `hspipeline` will first check to see if all necessary tools are on the path and will exit if they can't be found.

# Tools needed to run the pipeline

Make sure the following tools are compiled and available on your system PATH:

* [bcftools](https://github.com/samtools/bcftools)
* [bowtie2](https://github.com/BenLangmead/bowtie2)
* [fastx_toolkit](https://github.com/agordon/fastx_toolkit) (which requires [libgtextutils](https://github.com/agordon/libgtextutils))
* [samtools](https://github.com/samtools/samtools)
* [htslib](https://github.com/samtools/htslib)
* [sickle](https://github.com/najoshi/sickle)

# Symbols in plots
(until I add legends...)

## Coverage plots
* Magenta points = Less than 5 reads for that position.

## anc/evo coverage ratio plots
* Orange X = No reads in evolved strain
* Purple X = No reads in ancestor strain
* Cyan X = No reads in either strain

* Red circles = Point is > *x* sds away from mean ratio for that chromosome (*x* = 3 by default).
