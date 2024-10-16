# Movie Rank - Plataforma de Recomendaciones de Películas y Series

Este proyecto es una plataforma web que permite a los usuarios recibir recomendaciones de películas y series, calificar las que han visto y mostrar dónde pueden verlas en las plataformas de streaming disponibles. 

## Características

- **Sistema de usuarios, roles y permisos**: Gestión de usuarios con diferentes roles y permisos.
- **Calificaciones de películas y series**: Los usuarios pueden calificar las películas y series que hayan visto.
- **Recomendaciones personalizadas**: Recomendaciones basadas en los géneros favoritos del usuario.
- **Búsqueda avanzada**: Búsqueda de películas y series por título con opción de filtrado por género.
- **Listados por popularidad**: Listados de películas y series más populares.
- **Listas de favoritos**: Los usuarios pueden crear listas personalizadas de sus películas y series favoritas.
- **Historial de películas vistas**: Registro de todas las películas y series vistas por los usuarios.

## Requisitos

- Python 3.6 o superior
- Django 3.0 o superior
- MySQL

## Instalación del Proyecto desde Cero

```markdown
# Guía de Instalación y Configuración del Proyecto Django

## 1. Crear un entorno virtual

### En Windows:
```bash
python -m venv envs/envMysql
```

### En Linux:
```bash
python3 -m venv envs/envMysql
```

## 2. Activar el entorno virtual

### En Windows:
```bash
.\envs\envMysql\Scripts\activate
```

### En Linux:
```bash
source envs/envMysql/bin/activate
```

## 3. Instalar Django y MySQL Client

### En Windows:
```bash
python -m pip install Django
pip install mysqlclient
```

### En Linux:
```bash
sudo apt-get install python-dev default-libmysqlclient-dev
sudo apt-get install python3-dev
pip install mysqlclient
```

## 4. Crear el Proyecto Django
```bash
django-admin startproject movie_rank
```

## 5. Congelar las dependencias
Después de instalar las dependencias, genera el archivo `requirements.txt`:

```bash
pip freeze > requirements.txt
```

## 6. Configuración de la Base de Datos
Abre el archivo `settings.py` que se encuentra en el directorio `movie_rank/movie_rank/`. Configura la base de datos MySQL en la sección `DATABASES` con la siguiente estructura:

```python
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'movie_rankbd',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },

    }
}


```

## 7. Actualizar la Base de Datos MariaDB

Asegúrate de tener la versión de MariaDB 10.6.19 instalada. Si no la tienes, puedes descargarla desde el siguiente enlace:

[Descargar MariaDB 10.6.19](https://mariadb.org/download/?t=mariadb&p=mariadb&r=10.6.19&os=windows&cpu=x86_64&pkg=zip&mirror=raiolanetworks)

Si necesitas ayuda con la instalación, aquí tienes un video tutorial:

[Video de instalación de MariaDB](https://www.youtube.com/watch?v=-GmyjYEfuzE&ab_channel=DecorZone)

## 8. Migraciones de Base de Datos
Crea las migraciones iniciales para configurar las tablas en la base de datos:

```bash
python manage.py migrate
```

## 9. Crear el Superusuario
Para gestionar el panel de administración de Django, necesitarás un superusuario. Puedes crearlo con el siguiente comando:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para configurar las credenciales de administrador.

## 10. Ejecución del Servidor de Desarrollo
Inicia el servidor local para ver tu aplicación en funcionamiento:

```bash
python manage.py runserver
```

Abre tu navegador y visita [http://localhost:8000](http://localhost:8000).

## Licencia
Este proyecto está bajo la licencia MIT. Ver el archivo LICENSE para más detalles.
```