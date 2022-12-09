ARG         base=python:3.11.1-alpine3.17

###


FROM        ${base} AS poetry

ARG         MAKEFLAGS
ARG         POETRY_VERSION=1.2.2

RUN         apk add --no-cache --virtual .build-deps \
                curl \
                build-base \
                libffi-dev && \
            curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/install-poetry.py | python && \
            apk del .build-deps

###

FROM        ${base} as builder

WORKDIR     /usr/app

ENV         PATH=.venv/bin:$PATH
ENV         POETRY_VIRTUALENVS_IN_PROJECT=true
ENV         PATH=/root/.local/bin:$PATH

COPY        --from=poetry /root/.local /root/.local
COPY        pyproject.toml poetry.lock ./

RUN         apk add --no-cache --virtual .build-deps \
              build-base \
              libffi-dev \
              openssl-dev \
              rust \
              cargo && \
            poetry install -vv -n --no-dev --no-root --remove-untracked && \
            apk del .build-deps

###

FROM        ${base}

WORKDIR     /usr/app

ENV         PYTHON_VENV=/usr/app/.venv
ENV         PATH=/root/.local/bin:$PYTHON_VENV/bin:$PATH
ENV         PYTHONPATH=/usr/app/libs

ENTRYPOINT  ["python"]
CMD         ["main.py"]

COPY        --from=poetry /root/.local /root/.local
COPY        --from=builder /usr/app/.venv /usr/app/.venv
COPY        . .