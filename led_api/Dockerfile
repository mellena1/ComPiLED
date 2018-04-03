# Use go image to build the binary
FROM resin/raspberry-pi-golang as builder

RUN go get "github.com/gorilla/mux"
RUN mkdir -p $GOPATH/src/led_api
COPY . $GOPATH/src/led_api/
WORKDIR $GOPATH/src/led_api
RUN cd cmd/api && \
    go build && \
    cp api /api

# Switch to raspbian after the go code has been compiled
FROM resin/rpi-raspbian:jessie
COPY --from=builder /api /api
WORKDIR /

EXPOSE 20001
CMD ["./api"]
