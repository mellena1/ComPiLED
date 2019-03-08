FROM golang:1.12-alpine

WORKDIR /src

RUN apk add git gcc musl-dev
COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN go build -o ComPiLED

ENTRYPOINT ["/src/ComPiLED"]
