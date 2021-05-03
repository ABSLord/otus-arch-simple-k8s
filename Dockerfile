FROM python:3.9.4-slim-buster

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r /app/requirements.txt

ENV PYTHONPATH /app

COPY app.py /app/app.py

WORKDIR /app

CMD ["python", "app.py"]
