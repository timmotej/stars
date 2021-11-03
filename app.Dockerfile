FROM python:alpine

ENV GID=1000 \
    GNAME=group \
    UID=1000 \
    UNAME=user \
    HOME=/home/user \
    HOST=0.0.0.0 \
    PORT=8085 \
    LOG_LEVEL=debug \
    APP_MODULE=main:app \
    PATH="/app:${PATH}"

# set -x: print commands and their outputs
RUN set -x && \
    apk --update add bash vim tzdata git && \
    addgroup -g $GID -S $GNAME && \
    adduser -S -D -H -u $UID -h $HOME -s /sbin/nologin -G $GNAME -g $GNAME $UNAME && \
    unlink /usr/bin/env && \
    unlink /usr/bin/top && \
    unlink /bin/ps && \
    echo user was created && \
    mkdir /app && \
    chown $UID:$GID /app && \
    apk add --no-cache --virtual .build-deps gcc libc-dev make && \
    pip install uvicorn gunicorn fastapi urllib3 && \
    apk del .build-deps gcc libc-dev make && \
    echo "Set disable_coredump false" >> /etc/sudo.conf

COPY init/appd /etc/init.d/appd
# create image with right timezone for Vienna
ARG TZ=Europe/Vienna
RUN touch "/etc/timezone" && \
    ln -sf "/usr/share/zoneinfo/$TZ" /etc/localtime && \
    echo "$TZ" > /etc/timezone && \
    chmod 755 /etc/init.d/appd

WORKDIR /app
USER $UNAME
COPY app .

ENTRYPOINT ["/bin/bash"]
CMD ["-x","/etc/init.d/appd","start"]
 
