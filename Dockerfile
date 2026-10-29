FROM python:3.12-alpine AS Build

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# stage 2

FROM python:3.12-alpine AS Runner

WORKDIR /app

COPY --from=Build /install /usr/local

COPY app.py /app/

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]