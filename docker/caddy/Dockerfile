# Stage 1: Build the React app
FROM node:20-alpine AS frontend-builder

WORKDIR /app
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci
COPY frontend/ .
RUN npm run build

# Stage 2: Build Caddy with DuckDNS plugin
FROM caddy:2-builder AS caddy-builder
RUN xcaddy build --with github.com/caddy-dns/duckdns

# Stage 3: Final image
FROM caddy:2
COPY --from=caddy-builder /usr/bin/caddy /usr/bin/caddy
COPY --from=frontend-builder /app/dist /srv/react
