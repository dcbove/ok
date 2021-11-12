FROM python:3.9-slim

USER root

COPY src /app

WORKDIR /app

CMD ["python", "responder.py"]