# 1 : Base Images
FROM golang:1.13 AS builder

# Install dependencies
WORKDIR /go/src/github.com/asahiho/dockertext-great

# Build modules
COPY main.go .
RUN GOOS=linux go build -a -o greet .

##--------------------------
# 2 : Production Image
FROM busybox
WORKDIR /opt/greet/bin

# Deploy models
COPY --from=builder /go/src/github.com/asahiho/dockertext-great .
ENTRYPOINT ["./greet"]
