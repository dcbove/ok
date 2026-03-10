FROM python:3.12-slim

USER root

COPY src /app

WORKDIR /app

CMD ["python", "responder.py"]