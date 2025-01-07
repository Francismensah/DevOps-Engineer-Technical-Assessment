# Multi-stage build
FROM composer:2 as composer

# Copy composer files
COPY composer.json composer.lock ./
RUN composer install --no-dev --no-scripts --no-autoloader

FROM php:8.2-fpm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    zip \
    unzip \
    && docker-php-ext-install pdo_mysql mbstring exif pcntl bcmath gd

# Install Redis extension
RUN pecl install redis && docker-php-ext-enable redis

# Set working directory
WORKDIR /var/www

# Copy composer dependencies
COPY --from=composer /app/vendor/ ./vendor/

# Copy application files
COPY . .

# Generate optimized autoload files
RUN composer dump-autoload --optimize

# Set permissions
RUN chown -R www-data:www-data /var/www \
    && chmod -R 755 /var/www/storage

# Configure PHP
COPY docker/php/custom.ini /usr/local/etc/php/conf.d/

# Expose port 9000
EXPOSE 9000

# Start PHP-FPM
CMD ["php-fpm"]