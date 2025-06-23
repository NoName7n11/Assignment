FROM golang:1.21-alpine AS builder

WORKDIR /app
COPY . .

RUN go build -o service1 main.go

FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/service1 .
EXPOSE 8001
CMD ["./service1"]