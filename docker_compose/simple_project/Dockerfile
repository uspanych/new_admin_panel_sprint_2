FROM python:3.10.2-alpine

WORKDIR /app

RUN  \
    apk update && \
    apk upgrade && \
    pip install --upgrade pip

COPY ./requirements.txt .


RUN   \
     apk add --no-cache postgresql-libs &&  \
     apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
     python3 -m pip install -r /app/requirements.txt --no-cache-dir &&  \
     apk --purge del .build-deps


EXPOSE 8000

COPY ./app /app

ENTRYPOINT ["/app/entrypoint.sh"]
