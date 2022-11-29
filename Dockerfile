FROM python:3.10.7-slim as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

RUN pip install --upgrade pip
COPY . .

COPY ./pip-requirements.txt .
RUN pip wheel --no-cache-dir --no-deps \
        --wheel-dir /usr/src/app/wheels \
        -r pip-requirements.txt

# -----------------------------------------------------------------------------
FROM python:3.10.7-slim

ARG USER=app
ARG GROUP=app
ARG HUID=1113
ARG HGID=1113

RUN addgroup --system --gid ${HGID} ${GROUP} || echo 'Skipping'
RUN adduser --system --uid ${HUID} --group ${USER} || echo 'Skipping'

ENV HOME=/home/${USER}
ENV APP_HOME=/home/${USER}/service
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/pip-requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

COPY . $APP_HOME
RUN chown -R ${USER}:${GROUP} $APP_HOME

RUN mkdir -p /logs
RUN chown ${USER}:${USER} /logs

USER ${HUID}:${HGID}

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:80", "application:app"]
