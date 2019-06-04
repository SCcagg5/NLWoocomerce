FROM python:3.7-alpine  AS BACK_END

LABEL maintainer="Courtel Eliot"
LABEL maintainermail="eliot.courtel@wanadoo.fr"

WORKDIR /home/api

ENTRYPOINT \
	   if [ -d "./back-end/" ]; then cd ./back-end/src && pip3 install -r ../requirements.txt && set -a && . ../CONFIG && python3 server.py; fi;
