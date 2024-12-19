# backend/Dockerfile
FROM python:3.10.12

WORKDIR /code

# Install FFmpeg
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . /code

# Local development key set
# ENV TYPES: dev, production
# When set to dev, API Key on endpoint requests are just 'dev'
# When set to production, API Key on endpoint requests are the actual API Key

ENV PYTHONPATH=/code

CMD ["python", "main.py"]