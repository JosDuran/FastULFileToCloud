# FastULFileToCloud

Esta es una aplicacion para subir documentos,  imagenes, videos, etc a la web de manera rapida para su visualizacion. Desarrollado en HTML5  como backend he usado  en python (flask) y base de datos postgresql, la particularidad es que la interaccion con la base de datos, es integramente a travez de sentencias SQL, ya que no se a usado ORM alguno. Puede servir como una aplicacion paperless pues de hecho, permite subir imagenes a una base de datos y tenerlas clasificadas por un el campo de busqueda descripcion.

Cualquier consulta o sugerencia  

 am9zZHVyYW5AZ21haWwuY29t   (esta codificado a base64)


## requerimientos

Debido a que la aplicacion web, corre sobre un ecosistema DOCKER-COMPOSE solo es necesario instalar docker y hacer un par de pasos intermedios.

## Advertencia
 la aplicacion que vamos a desplegar, puede llegar a ser insegura, por contener la instruccion sendfile, sin embargo, para fines didacticos nos sera suficiente

# Instalacion

La instalacion de docker va por cuenta del usuario, se recomienda usar linux

Abrir una terminal en la carpeta de la aplicacion y ejecutar

```console
 docker-compose up --build
```

Para la creacion de las tablas  es necesario ingresar al contenedor pythonapp:

```console
docker exec -it 282 bin/bash
flask create_tables
#donde 282 es el id del contenedor

# Para llenar de data las tablas, dentro del shell del mismo contenedor ejecutar:
flask insert_data
```

Finalmente, para ejecutar la aplicacion entrar a htpp://localhost

Si es desde la misma pc o

htpp://ipadddress

si es desde otra pc de la red
