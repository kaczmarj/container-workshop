FROM neurodebian:stretch-non-free

ARG DEBIAN_FRONTEND=noninteractive

#----------------------------------------------------------
# Install common dependencies and create default entrypoint
#----------------------------------------------------------
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
      python3-setuptools \
      # Text editors
      emacs \
      nano \
      vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
