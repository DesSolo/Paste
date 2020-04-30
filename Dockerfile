FROM python:3.7-slim

WORKDIR /add
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD app .

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
