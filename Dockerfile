FROM python:3.11

ADD ./ /usr/src/app
# ADD ./sources /usr/src/app/sources

RUN pip install --no-cache-dir --timeout 120 --retries 5 -r /usr/src/app/requirements.txt
# RUN [ ! -f ./.env ] || export $(grep -v '^#' .env | xargs) && envsubst < /usr/src/app/alembic.ini.template > /usr/src/app/alembic.ini
# CMD ["/usr/local/bin/uvicorn /usr/src/app/main:app --host 0.0.0.0 --port 4000"]

# Clean up
RUN apt-get clean