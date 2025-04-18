
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
Y lo inicializaremos con: `.\.venv\Scripts\Activate.ps1 `


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

![image](https://github.com/user-attachments/assets/1f78a89d-0329-4664-b7b2-20ca04a056f0)


Una vez abierto en la barra superior de nuestro archivo daremos click en el botón **RUN** (icono play), y esperaremos que nos muestre el siguiente output en la terminal:

![image](https://github.com/user-attachments/assets/540fb4ba-7e31-4f04-9373-353e401ce4f1)

 
La URL que nos marca es la direccion HTTP por la cual podemos acceder a nuestra API y realizar las peticiones mediante Postman.

## Paso 2: Generar peticiones en Postman.
Ya que sabemos que nuestra API esta en ejecución nos dirigimos a la aplicación de Postman.

* Una vez dentro daremos click en nueva petición HTTP
* ![image](https://github.com/user-attachments/assets/301df238-f5cd-4b7a-8c6b-6977d92f2d50)

* Para fines de esta guía únicamente haremos una petición GET, para ello pegaremos la URL que nos arrojo nuestra terminal además de unos prefijos por lo que se vería algo así :
  ![image](https://github.com/user-attachments/assets/8b43b66a-1efd-4b70-b3d3-217f65ac2ae8)


Y daremos clic en SEND


* La respuesta de nuestra API debería ser un listado de todos los horarios dentro de nuestra base de datos
  ![image](https://github.com/user-attachments/assets/155e618a-6de9-4e98-8d1a-2f447a49a478)



Y eso seria todo el contenido de la guía, a continuación, estarán los métodos posibles para peticiones con la API. ¡Suerte!  

## Metodos


- GET todos los horarios
    - `GET http://127.0.0.1:5000/api/horarios/`


- GET horarios por ID
    - `GET http://127.0.0.1:5000/api/horarios/”id”`
    - Ejemplo: `http://127.0.0.1:5000/api/horarios/60`


- GET horarios por salón
    - `GET http://127.0.0.1:5000/api/horarios/”seccion”`
    - Ejemplo: `http://127.0.0.1:5000/api/horarios/s6`


- INSERT nuevo horario
    - `POST http://127.0.0.1:5000/api/horarios/add`
    - Ejemplo:
      ![image](https://github.com/user-attachments/assets/bf55e903-2d41-4b8e-8f61-4077e65bab1c)

      Lo que nos obtendria como respuesta un JSON retornando el ID del nuevo elemento
      Ejemplo:

      ```
      {
          145
      }
      ```


- DELETE Horario por ID
    - `DELETE http://127.0.0.1:5000/api/horarios/delete/”id”`
    - Ejemplo: `DELETE http://127.0.0.1:5000/api/horarios/delete/145`

      Lo que nos obtendria como respuesta un JSON retornando el ID del elemento eliminado
      Ejemplo:

      ```
      {
          145
      }
      ```

- UPDATE Horario por ID
    - `PUT http://127.0.0.1:5000/api/horarios/update/”id”`
    - Ejemplo:
      ![image](https://github.com/user-attachments/assets/a3376827-ee24-44a2-a75f-12d4fdc3d334)

      Lo que nos obtendria como respuesta un JSON retornando el ID del elemento modificado
      Ejemplo:

      ```
      {
          145
      }
      ```


