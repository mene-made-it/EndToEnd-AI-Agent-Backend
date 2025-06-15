FROM ubuntu:latest
LABEL authors="gianl"

ENTRYPOINT ["top", "-b"]