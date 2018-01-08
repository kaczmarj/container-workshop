# Start off with a fresh Ubuntu 16.04 base.
FROM ubuntu:16.04

# Install packages.
RUN apt-get update -qq \
    && apt-get install -y -q git python3 \
    # Remove unnecessary files to keep our image small.
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copy file from the host machine into the container.
COPY helloworld.py /opt/helloworld.py

# ENTRYPOINT is the command that is run when executing `docker run ...`.
ENTRYPOINT ["python3"]

# CMD provides default arguments to the entrypoint. A user can override these
# arguments with `docker run <this_image> <args>`
CMD ["/opt/helloworld.py"]
