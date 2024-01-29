# Servicio Web - REST/API (Lubex)
- Servicio Web desarrollado por Latamig, 2018 contacto: ep@latamig.com

# Función del servicio web
  - Servir a las aplicaciones móviles Android y iOS buscar datos relacionado a tablas con información lubricantes de la empresa Lubrax via HTTPS Requests así mismo poder modificar la información a través de un panel administrativo Web.

# Tecnologias
librerías y lenguaje(s) necesarios para ejecutar el siguiente servicio web

  - Python 3.7 o superior
  - MySQL5.1 o superior
  - Django 2.1 o superior
  - pyQuery
  - Docker
  - Git

# Instalación (Modo: Desarrollo)

El Servicio Web requiere instalar [Docker](https://www.docker.com/) para ejecutarse.

Ejecutar Aplicación.

```sh
$ cd esmaxws
$ docker-compose up -d --build
```
Accesar a contenedor deberas ejecutar el siguiente comando:
```sh
$ docker ps
```
Luego deberas seleccionar el ID del contenedor:
```sh
CONTAINER ID        IMAGE                   COMMAND                  CREATED             STATUS              PORTS                               NAMES
0442b22542f4        esmax_web               "python3 manage.py r…"   7 minutes ago       Up 7 minutes        0.0.0.0:8000->8000/tcp              esmax_web_1
```
Luego entramos en el contenedor
```sh
$ docker exec -ti 0442b22542f4 bash
```
Ejecutamos los siguiente comando para crear un usuario administrativo de Django, seguir instrucciones de consola
```sh
$ python manage.py createsuperuser
```

En caso de no poseer los datos recopilados para el funcionamiento de la data previamente en el Docker 

### Accesar al panel administrador
para accesar al panel administrador debió haber ejecutado el comando de crear un nuevo usuario por primera vez, una vez tenga uno. Ingresar en **http://localhost:8000/admin/login/** y ingresar el usuario y contraseña que ingreso cuando realizo la ejecución del comando python manage.py createsuperuser en la shell.

Luego puedes accesar a las siguientes URLs bajo **http://localhost:8000/**:

- /webservice/
  - product/make/<int:category> HTTP/GET
  - product/model/<uuid:manufacture> HTTP/GET
  - product/type/<uuid:model> HTTP/GET
  - product/filter/<uuid:type> HTTP/GET
  - product/filter/ HTTP/GET
  - company/ HTTP/GET
  - company/<int:id> HTTP/GET
  - product/ HTTP/GET
  - product/<uuid:uk> HTTP/GET
  - product/search/<int:manufacture>/<int:model>/<int:type> HTTP/GET
  - faq/ HTTP/GET
  - faq/<uuid:uk> HTTP/GET
- /admin/ HTTP/GET
- /static/ HTTP/GET
- /media/ HTTP/GET



# Instalación (Modo: Producción)
Para ejecutar el servicio web en modo producción usted deberá ejecutar el script en una imagen ubicado en el registry de 
gitlab que usted fue previamente asignado acceso. 

Recuerde que para accesar el registry de gitlab del grupo latamig en la sección ***cl-esmax*** usted deberá iniciar con su cuenta 
previamente autorizada. Así mismo usted deberá tener en cuenta las variables de entorno ilustradas abajo; Así como contemplar que esta imagen
la deberá ejecutar en algún Orquestador de Contenedores ***Docker*** como:

- Kubernetes
- Rancher
- Portainer
- Azure Cloud
- Google Cloud


```sh
docker login registry.gitlab.com
```
Recuerde que la versión actual imagen ***V0.1*** de este contenedor es ***registry.gitlab.com/latamig/cl-esmax/esmaxws:0.1***
es posible que haya una nueva versión por lo cual le pedimos que revise el registry y la versión actual; ya que este
documento puede estar desactualizado para el momento en que usted este corriendo esta versión.

```yml
version: '3'

services:
  esmax:
    image: registry.gitlab.com/latamig/cl-esmax/esmaxws:0.1
    ports:
      - 8000:8000
    env_file:
    - production.env
```

### Archivo production.env
Aquí usted deberá modificar el siguiente archivo ***production.env*** para asignarlo a la Base de datos MySQL que haya usted
destinado a producción.
``` sh
 DB_PORT=3306
 DB_HOST=localhost
 DB_NAME=esmax
 DB_USER=root
 DB_PASSWORD=root
 DOMAIN=localhost
 DEBUG=0
```
### Pasos posteriores
Una vez usted tenga corriendo el contenedor; deberá entrar al contenedor en modo bash 
según sea el gestor de contenedores Docker que este utilizando, y seguir los pasos a continuación.

#  Información: Data Predeterminada
El siguiente Servicio Web funciona bajo una data colectada previamente cuyo uso es fundamental para la operatividad básica del servicio es por ello que si usted por alguna
razón no posee esta data, obtendrá información incorrecta o nula en el caso de consultar por primera vez alguna URL indicada previamente.
Es por ello que usted deberá visitar el repositorio Git seguir la ejecución en orden numérico de los siguientes archivos.

```sh
-rw-r--r--  1 root root      886 Feb 26 12:21 company_9.json
-rw-r--r--  1 root root    71094 Feb 26 12:21 company_product_10.json
-rw-r--r--  1 root root     7796 Feb 26 12:21 faq_11.json
-rw-r--r--  1 root root     1300 Feb 26 12:21 formats_1.json
-rw-r--r--  1 root root    58288 Feb 26 12:21 product_7.json
-rw-r--r--  1 root root     1017 Feb 26 12:21 uses_2.json
-rw-r--r--  1 root root     1321 Feb 26 12:21 vehicle_category_3.json
-rw-r--r--  1 root root   139543 Feb 26 12:21 vehicle_manufacture_4.json
-rw-r--r--  1 root root  1348424 Feb 26 12:21 vehicle_model_5.json
-rw-r--r--  1 root root 17460359 Mar  1 16:31 vehicle_type_6.json
```

Para ello deberá ejecutar el siguiente comando seguido del documento cuyo numero avance de forma ascendente 1....9

```sh
python manage.py loaddata formats_1.json
```