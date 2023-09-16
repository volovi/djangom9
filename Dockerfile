FROM python:3.9-alpine
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /tmp/requirements.txt
RUN apk add --no-cache libgcc \
        && apk add --no-cache --virtual build-dependencies g++ \
        && pip install -r /tmp/requirements.txt \
        && apk del build-dependencies
COPY . /opt/app
RUN python /opt/app/manage.py collectstatic --no-input
RUN adduser --disabled-password --gecos "" user && chown -R user /opt/app
USER user
WORKDIR /opt/app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "djangom9.wsgi"]
