FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV AUTHOR="Владислав Колчин"

EXPOSE 8000

CMD ["python", "echo.py"]