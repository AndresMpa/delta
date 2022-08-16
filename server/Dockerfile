FROM python:3.10-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip --no-cache-dir install "fastapi[all]"

COPY [".", "/app"]

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]
