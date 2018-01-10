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

# CMD provides default execution options. A user can override these
# arguments with `docker run <this_image> <args>`
CMD ["python3", "/opt/helloworld.py"]
