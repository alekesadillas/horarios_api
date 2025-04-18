
# Proyecto “Automatización de A/C mediante IoT”

Mediante el uso de la siguiente API se planea implementar un sistema de automatización
para el encendido y apagado de A/C dentro la institución mediante tecnologías IoT y hardware adicional.

Actualmente al APi cuenta con la capacidad de crear Reglas Manuales y acceder a los
horarios registrados para aplicar Reglas Automaticas sobre el control del A/C.


## Instrucciones de Instalacion


Para la clonacion de nuestro proyecto abrimos la carpeta donde queramos alamacenar el proyecto y abriremos Visual Studio Code en ella.

Una vez dentro la carpeta en VSCode, abriremos una terminal y ejecutaremos el siguiente comando de GIT

`git clone https://github.com/alekesadillas/horarios_api.git`

Y .... listo! Ya tendremos nuestro proyecto clonado exitosamente.

Ahora te daras cuenta que la estructrura de nuestro proyecto es la siguiente:


```
}
    /src
    .env
    README.md
    requirements.txt
}
```

Necesitamos crear un entorno virtual donde almacenaremos nuestros paquetes y ejecutaremos nuestra app,
por lo que abriremos una terminal en la raiz de la carpeta de nuestro proyecto y ejecutaremos el siguiente comando: `python -m venv .venv`
Y lo inicializaremos con:

`.\.venv\Scripts\Activate.ps1 `


## Pre-requisitos


Para el uso del API Necesitamos crear una base de datos PostgreSQL hosteada mediante localhost.


>  En este proyecto se esta escuchando mediante el puerto 5432:5432 en localhost


Para crear nuestra tabla ejecutamos la siguiente SQL Query:

`CREATE TABLE public.horario_v2 (
    id SERIAL PRIMARY KEY,
    seccion VARCHAR(100),
    hora_inicio TIME,
    hora_fin TIME,
    estado VARCHAR(50),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
`


Una vez creada, en el siguiente archivo se encuentra la INSERT QUERY para llenar la tabla.

[insert.txt](https://github.com/user-attachments/files/19805981/insert.txt)

Y listo! Tendriamos lista nuestra Base de datos.






## Requisitos


Para que nuestra app pueda ejecutarse correctamente necesita de ciertos paquetes, dichos paquetes se tienen que instalar mediante `pip` en el terminal.
Afortunadamente encontraras tambien un archivo con todos los paquetes que necesitas para poder ejecutarla:

```
}
    /src
    .env
    README.md
    requirements.txt    <--
}
```

Para la instalacion abre una terminal dentro del proyecto en VSCode y ejecuta el siguiente comando:

`pip install -r requirements.txt`

Acontinuacion se instalaran todos los paquetes necesarios para la ejecucion.




# Uso del API

Ahora SI pasemos al uso de nuestra API.
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

`GET http://127.0.0.1:5000/api/horarios/`


Obtener horarios por ID

`GET http://127.0.0.1:5000/api/horarios/”id”`
Ejemplo: `http://127.0.0.1:5000/api/horarios/60`


Obtener horarios por salón

`GET http://127.0.0.1:5000/api/horarios/”seccion”
`
Ejemplo: `http://127.0.0.1:5000/api/horarios/s6`


INSERT nuevo horario

`POST http://127.0.0.1:5000/api/horarios/add`

Ejemplo:

 ![image](https://github.com/user-attachments/assets/62ea6424-6b4d-4b97-863a-76822c495502)


DELETE Horario por ID

`DELETE http://127.0.0.1:5000/api/horarios/delete/”id”`

Ejemplo: `DELETE http://127.0.0.1:5000/api/horarios/delete/145`


UPDATE Horario por ID

`PUT http://127.0.0.1:5000/api/horarios/update/”id”`
Ejemplo:

 ![image](https://github.com/user-attachments/assets/d7504678-4247-4439-8a5b-bdfbda4d33a4)


