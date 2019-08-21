FROM ubuntu:18.04

#
#
# Install services, packages and do cleanup
#
#

RUN apt-get update
RUN apt-get install -y apt-utils

# Basic packages

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata

RUN apt-get install -y \
    apt-utils \
    apache2 apache2-utils ssl-cert \
    python python-dev python-pip git build-essential autoconf vim \
    software-properties-common r-base libapache2-mod-wsgi

RUN service apache2 restart

# Add R repo
RUN apt-key adv --keyserver keyserver.ubuntu.com \
    --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
RUN add-apt-repository \
    'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'


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

# Make a folder to contain results
RUN mkdir seq_data
RUN chmod a+rx seq_data

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
    git clone https://github.com/samtools/samtools.git && \
    git clone https://github.com/samtools/htslib.git && \
    git clone https://github.com/najoshi/sickle.git && \
    git clone https://github.com/nodice73/hspipeline.git

RUN cd code/htslib && \
    autoheader && autoconf && ./configure && make && \
    make htslib_static.mk

RUN cd code/bcftools && \
    autoheader && autoconf && \
    ./configure --enable-libgsl --enable-perl-filters && \
    make

RUN cd code/bowtie2 && make

RUN cd code/samtools && \
    autoheader && autoconf -Wno-syntax && ./configure && make

RUN cd code/sickle && make

# Link binary files to common location.
RUN ln -s /code/bcftools/bcftools /bin/ && \
    ln -s /code/bowtie2/bowtie2 /bin/ && \
    ln -s /code/bowtie2/bowtie2-build /bin/ && \
    ln -s /code/bowtie2/bowtie2-inspect /bin/ && \
    ln -s /code/hspipeline/hspipeline /bin/ && \
    ln -s /code/hspipeline/cnvfind /bin/ && \
    ln -s /code/sickle/sickle /bin/ && \
    ln -s /code/samtools/samtools /bin/ && \
    ln -s /code/bcftools/misc/vcfutils.pl /bin/ && \
    ln -s /code/hspipeline/vcfunique /bin/

# Setup paths
RUN sed -i 's/\/home\/adamw//g' /code/hspipeline/web/paths.py

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
