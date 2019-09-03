# hspipeline
`hspipeline` connects existing tools together to analyse high-throughput sequencing data.

`hspipeline` is a command-line tool. Run it without arguments to see instructions and a detailed description of the arguments. 

Upon execution, `hspipeline` will first check to see if all necessary tools are on the path and will exit if they can't be found.

## Tools needed to run the pipeline

Make sure the following tools are compiled and available on your system PATH:

* [bcftools](https://github.com/samtools/bcftools)
* [bowtie2](https://github.com/BenLangmead/bowtie2)
* [samtools](https://github.com/samtools/samtools)
* [htslib](https://github.com/samtools/htslib)
* [sickle](https://github.com/najoshi/sickle)

## Directory structure
Each fastq file (or pair of fastq files for paired-end reads) should go in a directory named after its sample name. All the sample folders should go into a project directory. All of the project directories should go into a top-level directory. See diagram below.

```
    top-level directory
    |
    +----project1
         |
         +----Sample_1
         |    |
         |    +----sample1_R1.fastq.gz
         |    |
         |    +----sample1_R2.fastq.gz
         |
         +----Sample_2  
         |    |
         |    +----sample2_R1.fastq.gz
         |    |
         |    +----sample2_R2.fastq.gz
         |
         ...
         |
         +----Sample_N
```

## Symbols in plots
(until I add legends...)

### Coverage plots
* Magenta points = Less than 5 reads for that position.

### anc/evo coverage ratio plots
* Orange X = No reads in evolved strain
* Purple X = No reads in ancestor strain
* Cyan X = No reads in either strain

* Red circles = Point is > *x* sds away from mean ratio for that chromosome (*x* = 3 by default).

## Docker
To run `hspipeline` as a docker container:

1. [Install docker](https://www.docker.com/products/docker-desktop)

2. Make a directory to hold the sequence data somewhere on your computer (this is the "top-level directory" in the **Directory structure** diagram).

3. Move your project-level directory to the top-level directory.

3. Make the top-level directory and everything in it world-writable (apache runs as user 'www-data' and needs to write to these folders).

       $ chmod -R a+w /path/to/top_level_directory

4. Build and run docker in `hspipeline` folder:

       $ docker build docker
       $ docker run -it -p 9876:80 \
                    --mount type=bind,source=<location on computer>,target=/seq_data

**NOTE:** If you want to use symlinks instead of copies of your data files, you need to mount the directories containing the original (unlinked) data as well so that the links will be valid inside the docker environment.
