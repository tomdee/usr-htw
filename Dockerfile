FROM gliderlabs/alpine:latest
RUN apk --update add python curl
ADD usr-htw.py usr-htw.py
ENTRYPOINT ["python", "usr-htw.py"]

