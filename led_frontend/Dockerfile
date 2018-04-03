FROM t0rx/rpi-python3.6

COPY www_data ./www_data

WORKDIR ./www_data
CMD ["python3.6", "-m", "http.server", "20000"]
