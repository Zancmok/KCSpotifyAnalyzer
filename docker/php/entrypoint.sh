#!/bin/sh
set -e

cd /var/www

# Wait for MySQL to be ready to accept queries
echo "Waiting for database..."
until php artisan tinker --execute="DB::select('SELECT 1');" 2>/dev/null; do
    echo "Database not ready, retrying in 2s..."
    sleep 2
done
echo "Database ready."

# Run migrations
php artisan migrate --force

# Clear caches
php artisan config:clear
php artisan cache:clear

# Start PHP-FPM
exec php-fpm
