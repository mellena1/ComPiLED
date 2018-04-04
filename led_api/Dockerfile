# Use go image to build the binary
FROM hypriot/rpi-golang as builder

RUN mkdir api
WORKDIR api
RUN go get github.com/gorilla/mux
COPY api.go api.go
RUN go build && cp api /api

# Switch to raspbian after the go code has been compiled
FROM resin/rpi-raspbian:jessie
COPY --from=builder /api /api
WORKDIR /

EXPOSE 20001
CMD ["./api"]
