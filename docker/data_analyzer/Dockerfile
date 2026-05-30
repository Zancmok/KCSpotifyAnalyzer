FROM python:3.14-slim

WORKDIR /data_analyzer

COPY ./src/data_analyzer/ /data_analyzer/

COPY ./docker/data_analyzer/requirements.txt /data_analyzer/

RUN pip install --no-cache-dir -r /data_analyzer/requirements.txt

COPY ./src/database_lib/ /database_lib/

RUN pip install /database_lib/

COPY ./docker/data_analyzer/.env /data_analyzer/

CMD ["python", "main.py"]
