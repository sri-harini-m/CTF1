# Use an official PHP image
FROM php:7.4-apache

# Set working directory
WORKDIR /var/www/html

# Copy application files
COPY . .

# Expose the web server port
EXPOSE 80

# Start Apache
CMD ["apache2-foreground"]
