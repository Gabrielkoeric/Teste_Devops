FROM php:8.2-apache

# Atualize os pacotes e instale dependências
RUN apt-get update && \
    apt-get install -y vim && \
    apt-get install -y \
    libpng-dev \
    && docker-php-ext-install gd

# Copie o arquivo index.html
COPY index.html /var/www/html/index.html

# Ajuste as permissões
RUN chown -R www-data:www-data /var/www/html \
    && chmod -R 755 /var/www/html

EXPOSE 80

CMD ["apache2-foreground"]
