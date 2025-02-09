FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2-binary

WORKDIR /app
COPY upload-data.py upload-data.py 

ENTRYPOINT [ "python", "upload-data.py"]

docker run taxi_upload_data:v001 \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table=ny_taxi_data \
    --url=${URL}