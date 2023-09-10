FROM python:3.9-alpine as base
RUN apk add --no-cache \
        libpq \
        libgcc

FROM base as builder
RUN apk add --no-cache \
        g++ \
        musl-dev \
        postgresql-dev
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt --prefix=/install
COPY . /opt/app
RUN cp -r /install/* /usr/local
RUN python /opt/app/manage.py collectstatic --no-input

FROM base as prod
COPY --from=builder /install/ /usr/local/
COPY --from=builder /opt/app/ /opt/app/
WORKDIR /opt/app
CMD ["gunicorn", "djangom9.wsgi:application", "-b 0.0.0.0:8000"]
