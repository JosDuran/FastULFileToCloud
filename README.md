# FastULFileToCloud

Esta es una aplicacion para subir documentos,  imagenes, videos, etc a la web de manera rapida para su visualizacion. Desarrollado en HTML5  como backend he usado  en python (flask) y base de datos postgresql, la particularidad es que la interaccion con la base de datos, es integramente a travez de sentencias SQL, ya que no se a usado ORM alguno. 

Cualquier persona (que hable español o ingles) es bienvenida a unirse a este proyecto, para eso me tiene que enviar un correo a 

 am9zZHVyYW5AZ21haWwuY29t   (esta codificado a base64)

## requerimientos

Se debe instalar postgres y crear una base de datos con un nombre dado, el cual se configurara tambien en el archivo .env en el apartado de acceso a la bd

Se debe usar el mismo password del usuario postgres para configurar el archivo .env

Se adjunta un archivo DATABASE.md, en dicho archivo esta un indice que detalla cada archivo que se indexara en la basde de datos 

Para hacer el despliegue de la aplicacion se esta usando la tecnologia de Docker

# Instalacion

La instalacion de docker va por cuenta del usuario, se recomienda usar linux

Abrir una terminal en la carpeta de la aplicacion y ejecutar

```console
 docker-compose up --build
```

Para la creacion de ls tablas  es necesario ingresar al contenedor pythonapp:

```console
docker exec -it 282 bin/bash
flask create_tables
#donde 282 es el id del contenedor

# Para llenar de data las tablas
flask insert_data
```

Finalmente, para ejecutar la aplicacion entrar a htpp://localhost

Si es desde la misma pc o

htpp://ipadddress

si es desde otra pc de la red
