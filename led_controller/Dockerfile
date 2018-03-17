# Build c lib in raspbian image first
FROM resin/rpi-raspbian

# Install apt dependencies
RUN apt-get update && apt-get install -y \
                    git \
                    scons \
                    swig

# Build Neopixel C Library
RUN git clone https://github.com/jgarff/rpi_ws281x.git
WORKDIR /rpi_ws281x
RUN scons


# Switch to python lib so we don't store extra apt libs
FROM hypriot/rpi-python

# Copy from other image
COPY --from=0 /rpi_ws281x .
# Build and install python Neopixel lib
WORKDIR /rpi_ws281x/python
RUN python setup.py build && python setup.py install

# Switch back to / for working dir
WORKDIR /
#RUN rm -rf /rpi_ws281x
CMD ["python", "/rpi_ws281x/python/examples/strandtest.py"]
