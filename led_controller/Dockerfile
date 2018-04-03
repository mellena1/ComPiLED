# Build c lib in raspbian image first
FROM resin/rpi-raspbian as builder

# Install apt dependencies
RUN apt-get update && apt-get install -y \
                    git \
                    scons \
                    swig \
                    gcc \
                    avr-libc \
                    g++ \
                    libc-dev \
                    make

# Build Neopixel C Library
RUN git clone https://github.com/jgarff/rpi_ws281x.git
WORKDIR /rpi_ws281x
RUN scons


# Switch to python lib so we don't store extra apt libs
FROM t0rx/rpi-python3.6

RUN apt-get update && apt-get install -y swig

RUN mkdir rpi_ws281x
# Copy from other image
COPY --from=builder /rpi_ws281x /rpi_ws281x
# Build and install python Neopixel lib
WORKDIR /rpi_ws281x/python
RUN python3.6 setup.py build && python3.6 setup.py install
RUN rm -rf /rpi_ws281x

# Switch back to / for working dir
WORKDIR /
RUN pip3.6 install flask
COPY setup.py /setup.py
COPY ledcontroller /ledcontroller
RUN python3.6 setup.py install
CMD ["ledcontroller"]
