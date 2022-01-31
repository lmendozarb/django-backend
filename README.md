# Proyecto

## Comenzando 🚀
_Estas instrucciones te permitirán obtener una copia del esqueleto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

### Pre-requisitos 📋

-   Docker 19.03^
-   Docker Compose 1.25^
***

## Instalación 🔧

1. Clonar el repositorio
    ```
    git clone ...
    ```

2. Crear copia de variables de entorno

3. Contruir el contenedor
    ```
    make build
    ```
4. Levantar el contenedor
    ```
    make up
    ```
5. Ejecutar migraciones
    ```
    make migrate
    ```
6. Crear superusuario
    ```
    make superuser
    ```
***

## Utilitarios 💻
- Ver servicios disponibles en el proyecto: [http://localhost:8000/api/schema/redoc/](http://localhost:8000/api/schema/redoc/)
***

## Referencias 📖
- Projecto basado en el libro: Django 3 Web Development Cookbook Fourth Edition ([Enlace al libro](https://www.packtpub.com/product/django-3-web-development-cookbook-fourth-edition/9781838987428))
- Testing con pytest en django
    - [Enlace 1](https://djangostars.com/blog/django-pytest-testing/)
    - [Enlace 2](https://dev.to/sherlockcodes/pytest-with-django-rest-framework-from-zero-to-hero-8c4)
    - [Enlace 3](https://stackoverflow.com/questions/47576635/django-rest-framework-jwt-unit-test)

***

---