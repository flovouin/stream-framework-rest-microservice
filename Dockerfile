FROM python:2.7.13

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY activity ./activity
COPY main.py .

CMD ["python", "main.py"]
