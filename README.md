
# ❄️ Proyecto: **Automatización de A/C mediante IoT**

Este proyecto tiene como objetivo implementar un sistema inteligente para el encendido y apagado de aires acondicionados dentro de una institución, utilizando tecnologías IoT y hardware adicional.

Actualmente, la API permite:
- Crear **Reglas Manuales**
- Acceder a **horarios registrados**
- Aplicar **Reglas Automáticas** sobre el control del A/C

# 📺 Video de Expliacion del proyecto

Puedes encontrar ademas un video donde explicamos a detalle la instalación y funcionamiento del API mediante el siguiente [enlace](https://drive.google.com/file/d/1jMRnKIJWOciu8km_7vFuX77x7IgEVb8W/view?usp=sharing)

---

## 📦 Instalación del Proyecto

1. Abre la carpeta donde deseas clonar el proyecto.
2. Inicia **Visual Studio Code** en esa carpeta.
3. Abre una terminal e ingresa el siguiente comando:

```bash
git clone https://github.com/alekesadillas/horarios_api.git
```

¡Y listo! El proyecto estará clonado. La estructura se vera asi :

```
/horarios_api
│
├── /src
├── README.md
└── requirements.txt
```

---

## 🧪 Crear entorno virtual

1. En la raíz del proyecto, ejecuta:

```bash
python -m venv .venv
```

2. Activa el entorno con:

```bash
.\.venv\Scripts\Activate.ps1
```

---

## 🛠️ Pre-requisitos

Necesitamos una base de datos **PostgreSQL** escuchando en `localhost:5432`.

### Crear tabla principal


Para crear nuestra tabla ejecutamos la siguiente SQL Query:

```sql
CREATE TABLE public.horario_v2 (
    id SERIAL PRIMARY KEY,
    seccion VARCHAR(10),
    hora_inicio TIME,
    hora_fin TIME,
    estado BPCHAR(1),
    fecha_creacion TIMESTAMP,
    fecha_modificacion TIMESTAMP
);
```


📥 Para poblar la tabla con los datos necesarios, copia y pega el contenido de este archivo y ejecutalo como SQL SCRIPT:

🔗 [insert.txt](https://github.com/user-attachments/files/19805981/insert.txt)  


Y listo! Tendriamos lista nuestra Base de datos.

---




## 📚 Requisitos del proyecto

Para que nuestra app pueda ejecutarse correctamente necesita de ciertos paquetes, dichos paquetes se tienen que instalar mediante `pip` en el terminal.
Afortunadamente encontraras tambien un archivo con todos los paquetes que necesitas para poder ejecutarla:

```
/horarios_api
│
├── /src
├── .env
├── README.md
└── requirements.txt   <---
```

Para la instalacion abre una terminal dentro del proyecto en VSCode y ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

---




## 🚀 Uso de la API

Esta API permite realizar operaciones **GET, POST, PUT y DELETE** sobre la base de datos `horario_v2`.

### ▶️ Paso 1: Iniciar la API

1. Abre el archivo `app.py` dentro de la carpeta `/src`.
2. Haz clic en el botón **Run** (icono de ▶️ en la parte superior).

Deberías ver un mensaje en la terminal similar a:

```
Running on http://127.0.0.1:5000/
```  

> La URL que nos marca es la direccion HTTP por la cual podemos acceder a nuestra API y realizar las peticiones mediante Postman.

---
 

### 🧪 Paso 2: Realizar peticiones con Postman

1. Abre Postman y crea una nueva petición HTTP.
   - ![image](https://github.com/user-attachments/assets/301df238-f5cd-4b7a-8c6b-6977d92f2d50)

2. Para fines de esta guía únicamente haremos una petición GET, para ello pegaremos la URL proporcionada en la terminal con los siguientes endpoints (ejemplos más abajo):
   - ![image](https://github.com/user-attachments/assets/8b43b66a-1efd-4b70-b3d3-217f65ac2ae8)
  
3. Haz clic en **SEND**

La respuesta de nuestra API debería ser un listado de todos los horarios dentro de nuestra base de datos
 - ![image](https://github.com/user-attachments/assets/155e618a-6de9-4e98-8d1a-2f447a49a478)



Y eso seria todo el contenido de la guía, a continuación, estarán los métodos posibles para peticiones con la API. ¡Suerte!  

## 📡 Endpoints disponibles

### 📥 Obtener datos

- **Todos los horarios**
  ```http
  GET http://127.0.0.1:5000/api/horarios/
  ```

- **Horario por ID**
  ```http
  GET http://127.0.0.1:5000/api/horarios/60 <---- Aqui puedes reemplazar por el id del horario
  ```

- **Horarios por salón (sección)**
  ```http
  GET http://127.0.0.1:5000/api/horarios/s6 <---- Aqui puedes remplazar por el salon que busques
  ```

---

### ➕ Insertar nuevo horario

- **Endpoint**
  ```http
  POST http://127.0.0.1:5000/api/horarios/add
  ```
- Ejemplo:
   - ![image](https://github.com/user-attachments/assets/bf55e903-2d41-4b8e-8f61-4077e65bab1c)

  - **Respuesta esperada**
  ```json
  {
    "id": 145
  }
  ```

---

### 🗑️ Eliminar horario por ID

- **Endpoint**
  ```http
  DELETE http://127.0.0.1:5000/api/horarios/delete/"id"  <--- Äqui indicamos un id del horario a eliminar
  ```
- Ejemplo:
  ```http
  DELETE http://127.0.0.1:5000/api/horarios/delete/145
  ```

  - **Respuesta esperada**
  ```json
  {
    "id": 145
  }
  ```

---


### 🛠️ Actualizar horario por ID

- **Endpoint**
  ```http
  PUT http://127.0.0.1:5000/api/horarios/update/145
  ```
- Ejemplo:
   - ![image](https://github.com/user-attachments/assets/a3376827-ee24-44a2-a75f-12d4fdc3d334)

- **Respuesta esperada**
  ```json
  {
    "id": 145
  }
  ```

### 🛜 Modo de Uso Web App


- **Una vez en la ventana del navegador nos dirijimos a la siguiente URL**
  ```http
  http://127.0.0.1:5000/index 
  ```

  Esto nos llevara a la interfaz grafica y de inicio de sesion donde accederemos al panel de administracion

  Las credenciales de acceso son las siguientes:

   ```
    Usuario: admin

   ```
   ```
    password: 12345

   ```  



--- 
## 👨‍💻 Integrantes del Equipo

| Nombre completo                              | Usuario de GitHub                         |
|---------------------------------------------|-------------------------------------------|
| Santiago Sánchez Kevin Alejandro            | [alekesadillas](https://github.com/alekesadillas) |
| Segovia Cazares Isaac                       | [isaacsego](https://github.com/isaacsego) |
| Padrón Zaleta Jared Alfredo                 | [Jaresito2024](https://github.com/Jaresito2024) |
| Sordel Guzmán Andrea                        | [andysordel](https://github.com/andysordel) |
| Márquez Ruiz José De Jesús                  | [VIIIMaus](https://github.com/VIIIMaus) |
| Flores Torres José Gerardo                  | [GerFlo0](https://github.com/GerFlo0) |
| Garibaldi Zúñiga Daniel                     | [DanielGaribaldiZ](https://github.com/DanielGaribaldiZ) |
| Zaleta Diaz Dalia Nohemí                    | [DaliaN303](https://github.com/DaliaN303) |
| Avalos Pérez Juan Felipe                    | [Iron-Spider2099](https://github.com/Iron-Spider2099) |
| Gallegos Rodríguez Jessica Rubí             | [taesi23](https://github.com/taesi23) |
| Caudillo Luna Obet Yahir                    | [HarushiFPS](https://github.com/HarushiFPS) |

---

### 🎓 Instituto Tecnológico de Matamoros  
**Ingeniería en Sistemas Computacionales**  
**Materia: Programación Backend**


