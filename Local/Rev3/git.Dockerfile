FROM alpine:3.14

RUN apk update
RUN apk add --no-cache git

ENV USER=git
RUN adduser \
    --disabled-password \
    "$USER"

RUN su git
RUN cd && \
    mkdir .ssh && chmod 700 .ssh && \
    touch .ssh/authorized_keys && chmod 600 .ssh/authorized_keys

COPY gitkeys/* /tmp/

RUN cat /tmp/id_rsa.ty.pub >> ~/.ssh/authorized_keys
RUN cat /tmp/id_rsa.ty2.pub >> ~/.ssh/authorized_keys
RUN cat /tmp/id_rsa.ty3.pub >> ~/.ssh/authorized_keys




ENTRYPOINT ["/bin/sh"]