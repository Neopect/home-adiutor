FROM alpine:3.14

RUN apk update
RUN apk add --no-cache git

# Create git user
ENV USER=git
RUN adduser \
    --disabled-password \
    "$USER"

# Enter git enviroment and copy ssh keys
RUN su git
RUN cd && \
    mkdir .ssh && chmod 700 .ssh && \
    touch .ssh/authorized_keys && chmod 600 .ssh/authorized_keys

COPY gitkeys/* /tmp/

# Uncomment when I have ssh keys
# RUN cat /tmp/id_rsa.ty.pub >> ~/.ssh/authorized_keys
# RUN cat /tmp/id_rsa.ty2.pub >> ~/.ssh/authorized_keys
# RUN cat /tmp/id_rsa.ty3.pub >> ~/.ssh/authorized_keys

# Configuring git
RUN git config --global init.defaultBranch main

RUN mkdir /srv/git

# Test project
RUN cd /srv/git && \
    mkdir project.git && \
    cd project.git && \
    git init --bare




ENTRYPOINT ["/bin/sh"]