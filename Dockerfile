FROM python:3.10.0

WORKDIR /app

COPY src/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt && pip install uwsgi

RUN useradd -m myuser

USER myuser

COPY src/ ./

EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8080/health || exit 1

CMD ["uwsgi", "--ini", "app.ini"]
