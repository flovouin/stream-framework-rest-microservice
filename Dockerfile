FROM python:2.7.13

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt
# RUN pip uninstall -y celery
# RUN pip install celery==3.1

COPY activity ./activity
COPY main.py .

CMD ["python", "main.py"]
