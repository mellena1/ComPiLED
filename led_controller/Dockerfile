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
FROM hypriot/rpi-python

RUN apt-get update && apt-get install -y \
                    swig \
                    gcc

RUN mkdir rpi_ws281x
# Copy from other image
COPY --from=builder /rpi_ws281x /rpi_ws281x
# Build and install python Neopixel lib
WORKDIR /rpi_ws281x/python
RUN python setup.py build && python setup.py install

# Switch back to / for working dir
WORKDIR /
COPY led_test.py .
#RUN rm -rf /rpi_ws281x
CMD ["python", "led_test.py", "-c"]
