FROM python:3.10-slim
LABEL authors="Jan.Fuesting"



ENTRYPOINT ["top", "-b"]