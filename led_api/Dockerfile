FROM t0rx/rpi-python3.6

RUN pip3.6 install flask

COPY api.py ./api.py

ENV FLASK_APP=api.py
EXPOSE 20001
CMD ["flask", "run", "-p", "20001", "-h", "0.0.0.0"]
