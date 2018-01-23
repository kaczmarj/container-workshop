FROM neurodebian:stretch-non-free

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -qq \
    && apt-get install -yq --no-install-recommends  \
      # General system packages
    	apt-utils \
      bzip2 \
      ca-certificates \
      curl \
      unzip \
      # Version control packages
      datalad \
      git \
      git-annex-standalone \
      # Python
      python3 \
      python3-pip \
      python3-numpy \
      python3-setuptools \
      python3-wheel \
      # Text editors
      emacs \
      nano \
      vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    # Set default Python
    && ln -sfv /usr/bin/python3.5 /usr/bin/python \
    && ln -sfv /usr/bin/pip3 /usr/bin/pip \
    && useradd --no-user-group --create-home --shell /bin/bash neuro

USER neuro
ENV HOME="/home/neuro"
WORKDIR $HOME
