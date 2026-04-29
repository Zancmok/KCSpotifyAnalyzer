# Stage 1: build the React app
FROM node:20-alpine AS builder

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build

# Stage 2: Nginx with the built static files baked in
FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html
