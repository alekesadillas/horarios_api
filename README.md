# Uso del API

Listo! Ya tenemos corriendo nuestros contendores, tanto nuestro Sistema Operativo con nuestra API , tanto como nuestro servidor PostreSQL.
Ahora pasemos al uso de nuestra API.
Esta API puede realizar consultas **POST, INSERT, PUT y DELETE** en nuestra base de datos _**”horario_v2”**_.  Para realizar consultas y verificar su funcionalidad haremos uso del ayudante Postman.

## Paso 1: Iniciar la API
Nuestra API esta desarrollada mediante el framework Flask en Python, por lo que para incializarla nos buscaremos en la barra lateral de nuestro VSCode  la carpeta src y abriremos el archivo app.py.

![image](https://github.com/user-attachments/assets/68bec4bf-2d97-4e6f-8189-f015171fb49f)


Una vez abierto en la barra superior de nuestro archivo daremos click en el botón **RUN** (icono play), y esperaremos que nos muestre el siguiente output en la terminal:

![image](https://github.com/user-attachments/assets/0a65e94c-ac2f-48a2-a11b-cc60e6a59807)

 
La URL que nos marca es la direccion HTTP por la cual podemos acceder a nuestra API y realizar las peticiones mediante Postman.

## Paso 2: Generar peticiones en Postman.
Ya que sabemos que nuestra API esta en ejecución nos dirigimos a la aplicación de Postman.

•	Una vez dentro daremos click en nueva petición HTTP.

![image](https://github.com/user-attachments/assets/778e217c-f3d1-4919-ba71-f95eef4c815d)


•	Para fines de esta guía únicamente haremos una petición GET, para ello pegaremos la URL que nos arrojo nuestra terminal además de unos prefijos por lo que se vería algo así : 

![image](https://github.com/user-attachments/assets/d425a993-facb-4b7d-9e3f-edcf1ec82620)


Y daremos clic en SEND



•	La respuesta de nuestra API debería ser un listado de todos los horarios dentro de nuestra base de datos

 ![image](https://github.com/user-attachments/assets/91605fb8-22e6-47f3-8896-8de4920514fa)


Y eso seria todo el contenido de la guía, a continuación, estarán los métodos posibles para peticiones con la API. ¡Suerte!

Obtener todos los horarios
GET http://127.0.0.1:5000/api/horarios/

Obtener horarios por ID
GET http://127.0.0.1:5000/api/horarios/”id”
Ejemplo: http://127.0.0.1:5000/api/horarios/60

Obtener horarios por salón
GET http://127.0.0.1:5000/api/horarios/”seccion”
Ejemplo: http://127.0.0.1:5000/api/horarios/s6



INSERT nuevo horario
POST http://127.0.0.1:5000/api/horarios/add
Ejemplo:

 ![image](https://github.com/user-attachments/assets/62ea6424-6b4d-4b97-863a-76822c495502)


DELETE Horario por ID
DELETE http://127.0.0.1:5000/api/horarios/delete/”id”
Ejemplo:
DELETE http://127.0.0.1:5000/api/horarios/delete/145

UPDATE Horario por ID
PUT http://127.0.0.1:5000/api/horarios/update/”id”
Ejemplo:

 ![image](https://github.com/user-attachments/assets/d7504678-4247-4439-8a5b-bdfbda4d33a4)


