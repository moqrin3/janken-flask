FROM python:3.7.5-alpine

MAINTAINER moqrin3

USER root

RUN apk update

ENV PROJECT_ROOT /janken
WORKDIR $PROJECT_ROOT

COPY . .

RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN chmod +x docker-entrypoint.sh
EXPOSE 8000

ENTRYPOINT ["./docker-entrypoint.sh"]