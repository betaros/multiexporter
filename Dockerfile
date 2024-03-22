FROM python:3.10-slim
LABEL authors="Jan.Fuesting"

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9111
CMD ["ls"]
CMD ["python", "src/app.py"]