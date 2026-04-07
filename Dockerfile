FROM python:3.12-slim

# Prevent python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Prevent python from buffering stdout
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "data_pipeline.wsgi:application", "--bind", "0.0.0.0:8000"]