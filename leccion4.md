Flask + SSLPostgres + SSLnginx + Docker  

## Requisitos

Recomendado desplegarlo sobre linux con los siguientes paquetes: Docker, Docker-Compose, y si usan windows ademas deberan instalar git para windows

## Pasos a seguir para hacer el deploy

1) Clonamos el repositorio

git@github.com:JosDuran/FastULFileToCloud.git

```console
 git-clone ```console
```
2) nos ubicamos en la rama nginxsssl, para traer el codigo de la rama correcta

```console
 git checkout nginxsssl

3) ejecutamos el archivo aios_gen_cert.sh (cortesia de https://itnext.io/postgresql-docker-image-with-ssl-certificate-signed-by-a-custom-certificate-authority-ca-3df41b5b53) para generar los certificados
    3.1) ```console
 chmod +x aios_gen_cert.sh
 ./aios_gen_cert.sh
```
    3.2) creamos una carpeta ssl y ponemos ahi todos los archivos de clave generados

```
4) construimos el ecosistema de contenedores

```console
 docker-compose up --build
```

5) A continuacion se debe listar los procesos creados

```console
 docker ps -a
```
![](dockerps.png)

6) Elegir el id del contenedor que apunta a la imagen pythonapp

7) ejecutar

```console
 docker exec -it edd bin/bash
 flask create_tables
 flask insert_data
 exit
 # Debe remplazar el edd por el id de su contenedor
```
8)  ingresar a la siguiente direccion de su navegador: http://localhost para probar la aplicacion
