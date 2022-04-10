FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false

RUN mkdir /app
WORKDIR /app/
# Установка пакетов python и зависимостей необходимых для их сборки
RUN apk add --no-cache --virtual build-deps curl `# для установки poetry` \
    make gcc g++ `# для сборки пакетов` \
    postgresql-dev python3-dev musl-dev\
    zlib-dev libffi-dev
# Зависимости необходимые для работы
RUN apk add --no-cache \
    git `# для установки зависимостей из git` \
    zlib libffi
COPY poetry.lock pyproject.toml /app/
RUN pip install --no-cache-dir cryptography==2.1.4 \
    psycopg2-binary==2.9.3 `# проблемы с установкой через poetry на apple silicon`
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi
RUN apk del --no-cache build-deps

COPY entrypoint.sh /app/
RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh

COPY / /app/

ENTRYPOINT ["/app/entrypoint.sh"]