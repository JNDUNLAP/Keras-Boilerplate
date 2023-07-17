FROM python:3.10.0

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt && pip install uwsgi

RUN useradd -m givens

USER givens

COPY . ./

EXPOSE 8080


CMD ["uwsgi", "--ini", "app.ini"]
