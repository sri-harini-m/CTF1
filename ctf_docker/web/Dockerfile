FROM php:7.4-apache

# Install MySQLi extension
RUN docker-php-ext-install mysqli

# Copy website files to the container
COPY . /var/www/html/

# Set permissions
RUN chown -R www-data:www-data /var/www/html

# Expose port 80
EXPOSE 80

CMD ["apache2-foreground"]
