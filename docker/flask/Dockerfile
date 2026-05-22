FROM node:26-slim AS ts-build

WORKDIR /ts

RUN npm install -g typescript

COPY ./src/static/ts/ /ts/

RUN tsc -p /ts/ --rootDir /ts --outDir /ts/ts


FROM python:3.14-slim AS py-build

ENV APP_VERSION="alpha-0.0.3"

WORKDIR /flask

COPY ./src/ /flask/

COPY ./docker/flask/requirements.txt /flask/

RUN pip install --no-cache-dir -r /flask/requirements.txt

COPY ./docker/flask/.env /flask/

COPY --from=ts-build /ts/ts/ /flask/static/ts/

EXPOSE 5000

CMD ["python", "main.py"]
