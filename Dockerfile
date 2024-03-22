FROM python:3.10-slim
LABEL authors="Jan.Fuesting"

WORKDIR /app
COPY src/ /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9111

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9111"]