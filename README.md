# Django Hotel-Reservas

Aplicación web Django que permite a los usuarios hacer reservas en un hotel y dejar reseñas.

---
## Instalación y ejecución

Pasos para instalar el proyecto:

- Clone este repositorio en su máquina local usando el comando `git clone https://github.com/MiguelRizzi/django-hotel-reservas.git`.

- Si usa Visual Studio Code, abra el archivo `requirements.txt` y haga clic en Crear ambiente, luego elegir Venv y el intérprete Python, y finalmente pregunta por las dependencias: elegimos `requirements.txt`. Esto creara el entorno virtual e instalará todas las librerías necesarias para ejecutar el proyecto.

- Si prefiere instalarlo de manera manual, use el comando `python -m venv .venv`. Esto creará una carpeta llamada `.venv` dentro del directorio del proyecto.
Active el entorno virtual usando el comando `source .venv/bin/activate` en Linux o Mac, o `.venv\Scripts\activate` en Windows.
Instale las dependencias del proyecto usando el comando `pip install -r requirements.txt`. 

- Ejecute las migraciones de la base de datos usando los comandos `python manage.py makemigrations` y `python manage.py migrate`. Esto creará las tablas necesarias en la base de datos.

- Para ejecutar el servidor de desarrollo, muévase hasta el directorio del proyecto usando el comando `cd project` y use el comando `python manage.py runserver`. Esto iniciará el servidor en el puerto 8000 de su máquina local. Abre tu navegador y navega a `http://localhost:8000` para ver la aplicación en acción.

- Si quiere detener el servidor, simplemente presione `CTRL + C` en la consola donde está ejecutándose.

---
## Funcionalidades

- Registro e inicio de sesión de usuario.
- Personalización del modelo de usuario de Django usando relación uno a uno.
- Operaciones CRUD para tipos de habitaciones, habitaciones, reservas y reseñas.
- Permisos para controlar el acceso a las vistas.
- Aplicación de blog para dejar reseñas del hotel.
- Aplicación de contacto para enviar consultas.

---
## Uso

Para utilizar la aplicación, primero crea una cuenta haciendo clic en el enlace "Registrarse" en la página de inicio. Una vez que tengas una cuenta, puedes iniciar sesión y comenzar a hacer reservas y dejar reseñas.

Para poder modificar y eliminar tipos de habitaciones, habitaciones y reservas, así como eliminar reseñas de otros usuarios, es necesario estar autenticado con un superusuario o con un usuario que tenga permisos para hacerlo. Para crear un superusuario, utiliza el comando `python manage.py createsuperuser`. Una vez creado el superusuario, puedes iniciar sesión con estas credenciales y acceder al panel de administración de Django para gestionar los modelos y los permisos de los usuarios