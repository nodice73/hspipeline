FROM ubuntu:18.04

# Apache ENVs
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid
ENV APACHE_SERVER_NAME localhost

# Install services, packages and do cleanup
RUN apt-get update

# Basic packages
RUN apt-get install -y apache2 python git build-essential autoconf vim

# bcftools
RUN apt-get install -y zlib1g-dev libgsl0-dev libbz2-dev \
liblzma-dev libcurl4-openssl-dev libperl-dev \
libtbb-dev

# bowtie2
RUN apt-get install -y libtbb-dev

# libgtextutils
RUN apt-get install -y libtool pkg-config

# samtools
RUN apt-get install -y libncurses-dev

RUN mkdir code && cd code

RUN cd bcftools
RUN autoheader && autoconf && ./configure --enable-libgsl --enable-perl-filters

RUN cd ../bowtie2
RUN make

RUN cd ../libgtextutils/
RUN ./reconf && ./configure && make install

RUN cd ../fastx_toolkit
RUN ./reconf && ./configure

# They include a "-Werror" flag which treats warnings as errors
# and one of their files throws a warning...
RUN sed -i 's/-Werror *//g' src/fasta_formatter/Makefile
RUN make

RUN cd ../samtools
RUN autoheader && autoconf -Wno-syntax && ./configure && make

RUN cd ../htslib
RUN autoheader && autoconf && ./configure && make

RUN cd ../sickle
RUN make

RUN git clone https://github.com/samtools/bcftools.git
RUN git clone https://github.com/BenLangmead/bowtie2.git
RUN git clone https://github.com/agordon/fastx_toolkit.git
RUN git clone https://github.com/agordon/libgtextutils.git
RUN git clone https://github.com/samtools/samtools.git
RUN git clone https://github.com/samtools/htslib.git
RUN git clone https://github.com/najoshi/sickle.git

RUN git clone https://github.com/nodice73/hspipeline.git

RUN 


# Expose Apache
EXPOSE 80

# Launch Apache
#CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]

CMD /bin/bash