FROM python:3.10-slim

WORKDIR /app

RUN apt update && \
    apt install -y ffmpeg git && \
    pip install git+https://github.com/openai/whisper.git flask

COPY whisper-api.py /app/whisper-api.py

EXPOSE 9000

CMD ["python", "/app/whisper-api.py"]
