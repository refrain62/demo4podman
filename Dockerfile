FROM python:3.9.10

WORKDIR /app

ENV PORT 80

COPY ./app /app/

RUN pip install Flask

CMD ["python", "index.py"]
