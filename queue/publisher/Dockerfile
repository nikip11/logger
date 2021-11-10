FROM python:3.6-alpine3.14
WORKDIR /app
RUN apk add --no-cache  build-base linux-headers pcre-dev
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
