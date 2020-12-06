FROM python:3.8.5-alpine
WORKDIR /app
ADD requirements.txt requirements.txt

RUN apk update
RUN apk add --no-cache gcc g++ python3 python3-dev postgresql-dev \
    && pip3 install flask \
    && pip3 install psycopg2 \ 
    && pip3 install requests \
    && apk del gcc g++ python3-dev

COPY ./src/app.py /app/src/app.py
ENV FLASK_APP=/app/src/app.py
CMD ["python","src/app.py"]

VOLUME /logs 


