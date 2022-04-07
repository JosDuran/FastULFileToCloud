# FastULFileToCloud

Esta es una aplicacion para subir documentos e imagenes a la web de manera rapida para su visualizacion. Desarrollado en HTML5 Y como backend he usado  en python (flask) y base de datos postgresql, la particularidad es que la interaccion con la base de datos, es integramente a travez de sentencias SQL, ya que no se a usado ORM alguno. 

Cualquier persona (que hable español o ingles) es bienvenida a unirse a este proyecto, para eso me tiene que enviar un correo a 

 am9zZHVyYW5AZ21haWwuY29t   (esta codificado a base64)

## requerimientos

Se debe instalar postgres y crear una base de datos con un nombre dado, el cual se configurara tambien en el archivo .env en el apartado de acceso a la bd

Se debe usar el mismo password del usuario postgres para configurar el archivo .env

Se adjunta un archivo DATABASE.md, en dicho archivo esta un indice que detalla cada archivo que se indexara en la basde de datos 

Para la creacion de la tabla luego de activar el entorno virtual ejecutar: 

`flask create_tables`

Para llenar la tabla con el archivo de database.md ejecutar:

`flask insert_data`

Para ejecutar el servidor:

`flask run`

Para ver la app web desde el navegador poner en la barra de direcciones

localhost:5000
