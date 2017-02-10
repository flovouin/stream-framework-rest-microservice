FROM python:3.6.0

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY activity ./activity
COPY manage.py .
COPY db_setup.py .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
