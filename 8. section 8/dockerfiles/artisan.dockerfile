FROM php:alpine3.9

WORKDIR /var/www/html

COPY ./src .

ENTRYPOINT [ "php", "/var/www/html/artisan" ]