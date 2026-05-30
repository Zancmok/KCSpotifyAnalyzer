FROM node:26-slim AS ts-build

WORKDIR /ts

RUN npm install -g typescript

COPY ./src/web_server/static/ts/ /ts/

RUN tsc -p /ts/ --rootDir /ts --outDir /ts/ts


FROM python:3.14-slim AS py-build

ENV APP_VERSION="alpha-0.0.4"

WORKDIR /web_server

COPY ./src/web_server/ /web_server/

COPY ./docker/web_server/requirements.txt /web_server/

RUN pip install --no-cache-dir -r /web_server/requirements.txt

COPY ./src/database_lib/ /database_lib/

RUN pip install /database_lib/

COPY ./docker/web_server/.env /web_server/

COPY --from=ts-build /ts/ts/ /web_server/static/ts/

EXPOSE 5000

CMD ["python", "main.py"]
