FROM python:3.10.0

WORKDIR /src

COPY src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "src/app.py" ]
