FROM ubuntu:18.04

#
#
# Install services, packages and do cleanup
#
#

RUN apt-get update

# Basic packages
RUN apt-get install -y \
    apt-utils \
    apache2 apache2-utils ssl-cert \
    python python-dev python-pip git build-essential autoconf vim \
    libapache2-mod-wsgi

RUN service apache2 restart

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

# cleanup
RUN apt-get clean


#
#
#
# Build third-party tools
#
#
#

RUN mkdir code
RUN chmod o+rx code

RUN cd code && \
    git clone https://github.com/samtools/bcftools.git && \
    git clone https://github.com/BenLangmead/bowtie2.git && \
    git clone https://github.com/agordon/fastx_toolkit.git && \
    git clone https://github.com/agordon/libgtextutils.git && \
    git clone https://github.com/samtools/samtools.git && \
    git clone https://github.com/samtools/htslib.git && \
    git clone https://github.com/najoshi/sickle.git && \
    git clone https://github.com/nodice73/hspipeline.git

RUN cd code/bcftools && \
    autoheader && autoconf && \
    ./configure --enable-libgsl --enable-perl-filters

RUN cd code/bowtie2 && make

RUN cd code/libgtextutils && \
    ./reconf && ./configure && make install

RUN cd code/fastx_toolkit && \
    ./reconf && ./configure && \
    ## They include a "-Werror" flag which treats warnings as errors
    ## and one of their files throws a warning...
    sed -i 's/-Werror *//g' src/fasta_formatter/Makefile && \
    make

RUN cd code/samtools && \
    autoheader && autoconf -Wno-syntax && ./configure && make

RUN cd code/htslib && \
    autoheader && autoconf && ./configure && make

RUN cd code/sickle && make

#
#
#
# Setup Apache
#
#
#

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid
ENV APACHE_SERVER_NAME localhost

RUN ln -s /code/hspipeline /var/www
RUN ln -s /code/hspipeline/web/hspipeline.conf /etc/apache2/sites-available
RUN a2ensite hspipeline.conf && a2dissite 000-default.conf
RUN apache2ctl restart

EXPOSE 80

## Launch Apache
CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]
