FROM python:3.11-slim

# 'build-essential' is a package that includes gcc, g++, and other necessary tools.
RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

